import ipaddress

# 1. 개별 IP 분석
ip = ipaddress.ip_address('114.71.220.95')
print(f"IP 버전: IPv{ip.version}")  # 출력: IPv4

# 2. 네트워크 대역 확인
net = ipaddress.ip_network('114.71.220.0/24')
print(f"호스트 수: {net.num_addresses}")  # 출력: 256
print(f"첫 5개 호스트: {list(net.hosts())[:5]}")  # 114.71.220.1 ~ 114.71.220.5

# 3. IP 소속 확인
print('114.71.220.95' in net)  # True