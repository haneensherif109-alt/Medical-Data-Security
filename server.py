import socket

def xor_cipher(cipher_text, key):
    return "".join(chr(ord(c) ^ key) for c in cipher_text)

def start_server():
    host = "127.0.0.1"
    port = 5000
    secret_key = 42
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print("=== [طريقة متقدمة] سيرفر المستشفى يعمل الآن وينتظر البيانات... ===")
    
    while True:
        conn, addr = server_socket.accept()
        encrypted_data = conn.recv(1024).decode('utf-8')
        if not encrypted_data:
            break
            
        decrypted_data = xor_cipher(encrypted_data, secret_key)
        print(f"\n[+] اتصال مستلم من جهاز مريض: {addr}")
        print(f"[!] البيانات المستلمة مشفرة: {encrypted_data.encode('utf-8')}")
        print(f"[✔] فك التشفير بنجاح! القراءة الحقيقية: {decrypted_data}")
        conn.close()

if __name__ == "__main__":
    start_server()
