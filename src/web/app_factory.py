import os
import ipaddress
from flask import Flask, render_template, request, make_response, session
from src.network.validation import validate_ip, validate_prefix
from src.network.calculation import calculate_network_info, subnet_mask_to_prefix
from src.network.csv_export import create_csv

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), '../../config/.env'))
except ImportError:
    pass

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('FLASK_SECRET_KEY', os.urandom(24))

    @app.after_request
    def set_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Referrer-Policy'] = 'no-referrer'
        response.headers['Content-Security-Policy'] = "default-src 'self'; style-src 'self' https://cdn.jsdelivr.net; script-src 'self' https://cdn.jsdelivr.net;"
        return response

    @app.route("/", methods=["GET", "POST"])
    def index():
        result = None
        error = None
        csv_available = False
        if request.method == "POST":
            ip = request.form.get("ip", "").strip()
            subnet_input = request.form.get("subnet", "").strip()

            if not validate_ip(ip):
                error = "Invalid IP address!"
            else:
                ip_obj = ipaddress.ip_address(ip)
                version = ip_obj.version

                if subnet_input.startswith('/'):
                    prefix_str = subnet_input[1:]
                    if not validate_prefix(prefix_str, version):
                        error = "Invalid CIDR prefix!"
                    else:
                        prefix = int(prefix_str)
                        subnet = prefix
                else:
                    if version == 4:
                        if not validate_ip(subnet_input):
                            error = "Invalid subnet mask!"
                        else:
                            prefix = subnet_mask_to_prefix(subnet_input, version)
                            if prefix is None:
                                error = "Subnet mask is not contiguous!"
                            else:
                                subnet = subnet_input
                    else:
                        error = "For IPv6 please use CIDR notation like /64"
                if not error:
                    result = calculate_network_info(ip, subnet)
                    session['csv_data'] = result
                    csv_available = True

        return render_template("index.html", result=result, error=error, csv_available=csv_available)

    @app.route("/download_csv", methods=["GET"])
    def download_csv():
        data = session.get('csv_data')
        if not data:
            return "No data to download", 400
        csv_file = create_csv(data)
        response = make_response(csv_file.getvalue())
        response.headers["Content-Disposition"] = "attachment; filename=subnet_info.csv"
        response.headers["Content-type"] = "text/csv"
        return response

    return app
