import socket
import des


def server_program():

    key = "abcdefgh"

    
    host = socket.gethostname()
    port = 5000 

    server_socket = socket.socket()
    
    server_socket.bind((host, port))

    
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
       
        data = conn.recv(1024).decode()
        if not data:
            
            break

        print("Kullanıcıdan gelen şifrelenmiş mesaj : ", str(data))
        print("from connected user: " + str(des.DES_Decrypt(data, key)))
        data = input(' -> ')
        data = des.DES_Encrypt(data, key)
        print("Şifrelenmiş mesaj : ", data)
        conn.send(data.encode())  

    conn.close() 


if __name__ == '__main__':
    server_program()