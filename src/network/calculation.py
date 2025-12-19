import ipaddress
from .validation import validate_ip, validate_prefix

def prefix_to_subnet_mask(prefix, version=4):
    if version == 4:
        mask = (0xffffffff >> (32 - prefix)) << (32 - prefix)
        return f"{(mask >> 24) & 0xff}.{(mask >> 16) & 0xff}.{(mask >> 8) & 0xff}.{mask & 0xff}"
    else:
        return prefix

def subnet_mask_to_prefix(mask_str, version=4):
    if version == 4:
        try:
            mask = ipaddress.IPv4Address(mask_str)
            bin_str = bin(int(mask))[2:].zfill(32)
            if '01' in bin_str:
                return None
            return bin_str.count('1')
        except ipaddress.AddressValueError:
            return None
    else:
        return None

def wildcard_mask(subnet_mask, version=4):
    if version == 4:
        mask_int = int(ipaddress.IPv4Address(subnet_mask))
        wildcard_int = (~mask_int) & 0xffffffff
        return str(ipaddress.IPv4Address(wildcard_int))
    else:
        return "N/A"

def calculate_network_info(ip_str, subnet_input):
    ip = ipaddress.ip_address(ip_str)
    version = ip.version
    if isinstance(subnet_input, int):
        prefix = subnet_input
        subnet_mask = prefix_to_subnet_mask(prefix, version)
    elif isinstance(subnet_input, str):
        if subnet_input.startswith('/'):
            prefix = int(subnet_input[1:])
            subnet_mask = prefix_to_subnet_mask(prefix, version)
        else:
            prefix = subnet_mask_to_prefix(subnet_input, version)
            subnet_mask = subnet_input
    else:
        prefix = None
        subnet_mask = None

    if version == 4:
        net = ipaddress.IPv4Network(f"{ip_str}/{prefix}", strict=False)
        network_address = str(net.network_address)
        broadcast_address = str(net.broadcast_address)
        num_hosts = net.num_addresses - 2 if net.num_addresses > 2 else 1
        first_usable = str(next(net.hosts())) if num_hosts >= 1 else network_address
        last_usable = str(list(net.hosts())[-1]) if num_hosts > 1 else broadcast_address
        wildcard = wildcard_mask(subnet_mask, version)
        cidr = f"/{prefix}"
    else:
        net = ipaddress.IPv6Network(f"{ip_str}/{prefix}", strict=False)
        network_address = str(net.network_address)
        broadcast_address = "N/A for IPv6"
        num_hosts = net.num_addresses
        first_usable = network_address
        last_usable = "N/A"
        wildcard = "N/A"
        cidr = f"/{prefix}"

    return {
        "IP Address": ip_str,
        "Version": f"IPv{version}",
        "Subnet Mask": subnet_mask if version == 4 else "N/A",
        "CIDR Notation": cidr,
        "Network Address": network_address,
        "Broadcast Address": broadcast_address,
        "Number of Usable Hosts": num_hosts,
        "First Usable IP": first_usable,
        "Last Usable IP": last_usable,
        "Wildcard Mask": wildcard,
    }
