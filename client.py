import socket


# Client socket instance
client_socket_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Target server ip address and port
ip_address = "127.0.0.1"
port = 55800

# Client trying to connect to server
client_socket_object.connect((ip_address, port))

# Receiving initial message from the server
data_received = client_socket_object.recv(1024)

if data_received:
    print("CLIENT CONNECTED TO SERVER")
    print(f"SERVER MESSAGE: {data_received.decode('utf-8')}")

    while data_received:
        client_input = input().encode('utf-8')
        client_socket_object.send(client_input)

        data_received = client_socket_object.recv(1024)
        if data_received:
            print(f"SERVER MESSAGE: {data_received.decode('utf-8')}")

    client_socket_object.close()
    print("SERVER CLIENT CONNECTION CLOSED")
