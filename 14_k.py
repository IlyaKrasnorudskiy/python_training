from ipaddress import ip_network, ip_address
ip = '206.158.124.67'
mask = '255.255.224.0'
net = ip_network(f'{ip}/{mask}',0)
count = 0
for i in net:
    count+=1

print(count)
print(net)
print(ip_address(ip))
print(int(ip_address(ip)))
print(net.network_address)
print(int(net.network_address))