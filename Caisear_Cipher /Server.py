import socket

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def server_program():
    host = socket.gethostname()
    port = 12345
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Received from client: " + data)
 
        shift = int(input("Enter the Caesar Cipher key: "))
        encrypted_data = caesar_cipher(data, shift)
        print("Encrypted data: " + encrypted_data)
        conn.send(encrypted_data.encode())
        decrypted_data = caesar_cipher(encrypted_data, -shift)
        print("Decrypted data: " + decrypted_data)
    conn.close()

if __name__ == '__main__':
    server_program()

