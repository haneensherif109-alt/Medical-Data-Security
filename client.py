import socket
import time

def xor_cipher(data, key):
    return "".join(chr(ord(c) ^ key) for c in data)

def start_device():
    server_ip = "127.0.0.1"
    server_port = 5000
    secret_key = 42
    
    print("=== [طريقة متقدمة] جهاز المريض الذكي بدأ العمل ===")
    heart_rates = ["72 BPM", "85 BPM", "90 BPM", "68 BPM"]
    
    for rate in heart_rates:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip, server_port))
            
            print(f"\n[+] البيانات الأصلية: {rate}")
            encrypted_data = xor_cipher(rate, secret_key)
            print(f"[!] البيانات بعد التشفير: {encrypted_data.encode('utf-8')}")
            
            client_socket.send(encrypted_data.encode('utf-8'))
            print("[->] تم إرسال البيانات المشفرة بنجاح عبر الشبكة.")
            client_socket.close()
        except ConnectionRefusedError:
            print("[-] السيرفر مش شغال! يرجى تشغيل server.py أولاً.")
            break
        time.sleep(3)

if __name__ == "__main__":
    start_device()
