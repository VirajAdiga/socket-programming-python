"""
Points to remember:

1. Text data is stored as bytes, not as actual texts, everything in the end should be stored in binary
2. When reading from file, we convert those bytes to string by decoding it using particular charset like utf-8, because
programming languages can work with strings
3. Then, if we want to send data over network, it needs to be converted into stream of bytes for which encoding happens
4. In the receiving end, decoding of this byte stream happens to convert it into text data if text data was sent
5. Remember, this encoding decoding is done with text data, binary data such as image, video, audio are directly sent
and stored as binary data most of the times

"""

import socket


# Server Socket instance (socket.SOCK_STREAM is for accepting only TCP connections)
server_socket_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 55800

server_socket_object.bind((ip_address, port))
server_socket_object.listen()

print("SERVER LISTENING")

# Accept the client connections whenever it comes
while True:
    try:
        # Accepting connections from the client if client wants to connect
        connection_object, _ = server_socket_object.accept()

        if connection_object:
            print("SERVER CONNECTED TO CLIENT")

        # Sending message to client
        connection_object.send(b"Type the message")
        # This is equivalent to 'Type the message'.encode(), remember we need to encode while sending byte stream

        # Receiving message from client
        data_received = connection_object.recv(1024)
        # 1024 is the buffer size for accepting data

        # Accept messages from client till it sends 'stop'
        while data_received != b'stop':
            print(f"CLIENT MESSAGE: {data_received.decode('utf-8')}")
            connection_object.send(b"Received your message")
            data_received = connection_object.recv(1024)

        connection_object.close()
        print("SERVER CLIENT CONNECTION CLOSED")

    except KeyboardInterrupt:
        print("SERVER EXITING")
        break

server_socket_object.close()
