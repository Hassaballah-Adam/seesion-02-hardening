import socket

target_ip = "192.168.1.1"
ports = [22, 80, 443]

print(f"--- Performing Surgical Scan on Gateway: {target_ip} ---")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    result = s.connect_ex((target_ip, port))
    
    if result == 0:
        print(f"🌟 SUCCESS: Port {port} is OPEN on {target_ip}")
    else:
        print(f"❌ CLOSED: Port {port} is not responding.")
        
    s.close()
