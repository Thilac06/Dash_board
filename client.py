import socket
while True:

    host = '127.0.0.1'
    port = 12345


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")


    message = "Hello, server!"
    client_socket.sendall(message.encode('utf-8'))
    print(f"Sent data: {message}")


    data = client_socket.recv(1024)
    print(f"Received echoed data: {data.decode('utf-8')}")

    x = data.decode('utf-8')




    client_socket.close()
