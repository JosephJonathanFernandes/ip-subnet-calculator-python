import ipaddress

def validate_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def validate_prefix(prefix_str, version=4):
    try:
        prefix = int(prefix_str)
        if version == 4:
            return 0 <= prefix <= 32
        else:
            return 0 <= prefix <= 128
    except ValueError:
        return False
