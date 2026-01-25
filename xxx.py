from ipaddress import ip_network, ip_address
ip_b = ip_address('206.123.210.118')
for mask in range(32, -1, -1):
    net = ip_network(f'206.123.209.193/{mask}',0)
    if ip_b in net:
        for ip in net:
            print(net.num_addresses//2)
