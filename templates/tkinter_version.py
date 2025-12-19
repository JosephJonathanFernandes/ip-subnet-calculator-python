import tkinter as tk
from tkinter import messagebox
import ipaddress

def validate_ip(ip_str):
    try:
        ipaddress.IPv4Address(ip_str)
        return True
    except ipaddress.AddressValueError:
        return False

def validate_prefix(prefix_str):
    try:
        prefix = int(prefix_str)
        return 0 <= prefix <= 32
    except ValueError:
        return False

def prefix_to_subnet_mask(prefix):
    mask = (0xffffffff >> (32 - prefix)) << (32 - prefix)
    return f"{(mask >> 24) & 0xff}.{(mask >> 16) & 0xff}.{(mask >> 8) & 0xff}.{mask & 0xff}"

def subnet_mask_to_prefix(mask_str):
    try:
        mask = ipaddress.IPv4Address(mask_str)
        bin_str = bin(int(mask))[2:].zfill(32)
        if '01' in bin_str:
            return None  # invalid mask (non-contiguous ones)
        return bin_str.count('1')
    except ipaddress.AddressValueError:
        return None

def wildcard_mask(subnet_mask):
    mask_int = int(ipaddress.IPv4Address(subnet_mask))
    wildcard_int = (~mask_int) & 0xffffffff
    return str(ipaddress.IPv4Address(wildcard_int))

def calculate_network_info(ip_str, subnet_mask_str):
    ip = ipaddress.IPv4Address(ip_str)
    net = ipaddress.IPv4Network(f"{ip_str}/{subnet_mask_str}", strict=False)

    network_address = str(net.network_address)
    broadcast_address = str(net.broadcast_address)
    num_hosts = net.num_addresses - 2 if net.num_addresses > 2 else 1
    first_usable = str(next(net.hosts())) if num_hosts >= 1 else network_address
    last_usable = str(list(net.hosts())[-1]) if num_hosts > 1 else broadcast_address
    prefix = net.prefixlen
    wildcard = wildcard_mask(subnet_mask_str)

    return {
        "IP Address": ip_str,
        "Subnet Mask": subnet_mask_str,
        "CIDR Notation": f"/{prefix}",
        "Network Address": network_address,
        "Broadcast Address": broadcast_address,
        "Number of Usable Hosts": num_hosts,
        "First Usable IP": first_usable,
        "Last Usable IP": last_usable,
        "Wildcard Mask": wildcard,
    }

def on_calculate():
    ip = ip_entry.get().strip()
    subnet_input = subnet_entry.get().strip()

    if not validate_ip(ip):
        messagebox.showerror("Error", "Invalid IP address!")
        return

    # Parse subnet input
    if subnet_input.startswith('/'):
        prefix_str = subnet_input[1:]
        if not validate_prefix(prefix_str):
            messagebox.showerror("Error", "Invalid CIDR prefix! Enter 0-32.")
            return
        prefix = int(prefix_str)
        subnet_mask = prefix_to_subnet_mask(prefix)
    else:
        if not validate_ip(subnet_input):
            messagebox.showerror("Error", "Invalid subnet mask!")
            return
        prefix = subnet_mask_to_prefix(subnet_input)
        if prefix is None:
            messagebox.showerror("Error", "Subnet mask is not contiguous!")
            return
        subnet_mask = subnet_input

    info = calculate_network_info(ip, subnet_mask)

    # Display results
    result_text = ""
    for k, v in info.items():
        result_text += f"{k}: {v}\n"

    result_label.config(text=result_text)

# Tkinter GUI setup
root = tk.Tk()
root.title("IP & Subnet Calculator")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# IP input
tk.Label(frame, text="IP Address:").grid(row=0, column=0, sticky="e")
ip_entry = tk.Entry(frame, width=20)
ip_entry.grid(row=0, column=1)

# Subnet input
tk.Label(frame, text="Subnet Mask or CIDR (/24):").grid(row=1, column=0, sticky="e")
subnet_entry = tk.Entry(frame, width=20)
subnet_entry.grid(row=1, column=1)

# Calculate button
calc_btn = tk.Button(frame, text="Calculate", command=on_calculate)
calc_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Result display
result_label = tk.Label(frame, text="", justify="left", font=("Courier", 10), bg="white", relief="sunken", width=45, height=10, anchor="nw")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
