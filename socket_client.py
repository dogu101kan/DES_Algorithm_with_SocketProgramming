import socket
import des


def client_program():

    key = "abcdefgh"

    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")
    message = des.DES_Encrypt(message, key)
    print("Şifrelenmiş mesaj : ", message)

    while des.DES_Decrypt(message, key).lower().strip() != '-1':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print("Serverden gelen şifrelenmiş mesaj : ", data)
        print('Received from server: ' + des.DES_Decrypt(data, key))

        message = input(" -> ")
        message = des.DES_Encrypt(message, key)
        print("Şifrelenmiş mesaj : ", message)

    client_socket.close()


if __name__ == '__main__':
    client_program()