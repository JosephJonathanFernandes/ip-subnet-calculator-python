
import pytest
from src.network.validation import validate_ip, validate_prefix
from src.network.calculation import prefix_to_subnet_mask, subnet_mask_to_prefix, wildcard_mask, calculate_network_info
from src.network.csv_export import create_csv

def test_validate_ip():
    assert validate_ip('192.168.1.1')
    assert validate_ip('2001:db8::1')
    assert not validate_ip('999.999.999.999')
    assert not validate_ip('bad_ip')

def test_validate_prefix():
    assert validate_prefix('24', 4)
    assert not validate_prefix('33', 4)
    assert validate_prefix('64', 6)
    assert not validate_prefix('129', 6)

def test_prefix_to_subnet_mask():
    assert prefix_to_subnet_mask(24) == '255.255.255.0'
    assert prefix_to_subnet_mask(16) == '255.255.0.0'

def test_subnet_mask_to_prefix():
    assert subnet_mask_to_prefix('255.255.255.0') == 24
    assert subnet_mask_to_prefix('255.255.0.0') == 16
    assert subnet_mask_to_prefix('255.0.255.0') is None

def test_wildcard_mask():
    assert wildcard_mask('255.255.255.0') == '0.0.0.255'
    assert wildcard_mask('255.255.0.0') == '0.0.255.255'

def test_calculate_network_info_ipv4():
    result = calculate_network_info('192.168.1.10', 24)
    assert result['Network Address'] == '192.168.1.0'
    assert result['Broadcast Address'] == '192.168.1.255'
    assert result['Subnet Mask'] == '255.255.255.0'
    assert result['CIDR Notation'] == '/24'
    assert result['Version'] == 'IPv4'

def test_calculate_network_info_ipv6():
    result = calculate_network_info('2001:db8::1', 64)
    assert result['Network Address'] == '2001:db8::'
    assert result['Version'] == 'IPv6'
    assert result['CIDR Notation'] == '/64'
    assert result['Subnet Mask'] == 'N/A'

def test_create_csv():
    data = {'A': 1, 'B': 2}
    csv_file = create_csv(data)
    content = csv_file.getvalue()
    assert 'A,1' in content and 'B,2' in content
