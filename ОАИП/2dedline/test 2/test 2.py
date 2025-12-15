logs = [
    "192.168.1.1 - GET /index.html 200",
    "192.168.1.5 - GET /about 404",
    "192.168.1.1 - POST /login 200",
    "10.0.0.1 - GET /admin 500",
    "192.168.1.5 - GET /fail 404",
    "192.168.1.1 - GET /fail 404",
    "10.0.0.1 - GET /admin 500",
    "192.168.1.5 - GET /fail 404",
    "10.0.0.1 - GET /admin 500",
    "10.0.0.1 - GET /admin 500",
]

codes = {}
ips = {}
bad_ips = {}

for log in logs:
    parts = log.split()
    ip = parts[0]
    code = parts[4]
    
    codes[code] = codes.get(code, 0) + 1
    ips[ip] = ips.get(ip, 0) + 1
    if code in ("404", "500"):
        bad_ips[ip] = bad_ips.get(ip, 0) + 1

max_ip = max(ips, key=ips.get)
N = 2
sus = [ip for ip, cnt in bad_ips.items() if cnt > N]

print(f"200: {codes.get('200',0)} 404: {codes.get('404',0)} 500: {codes.get('500',0)}")
print(f"Активный IP: {max_ip}")
print(f"Подозрительные (>2): {sus if sus else 'нет'}")
