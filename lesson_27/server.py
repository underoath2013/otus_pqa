import socket
import http.client

end_of_stream = '\r\n\r\n'

def handle_client(connection):
    client_data = ''
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            client_data += data.decode()
            if end_of_stream in client_data:
                break
            
        request_lines = client_data.strip().split('\r\n')
        request_method = request_lines[0].split()[0]
        
        status_code = 200  # Default status code
        
        for line in request_lines:
            if line.startswith("GET /?status="):
                status_param = line.split("?status=")[1].split()[0]
                try:
                    status_code = int(status_param)
                except ValueError:
                    pass
                break
        
        response_status = http.client.responses.get(status_code, 'Unknown')
        
        http_response = (
            f"HTTP/1.0 {status_code} {response_status}\r\n"
            f"Server: Simple echo-server\r\n"
            f"Content-Type: text/plain; charset=UTF-8\r\n"
            f"\r\n"
            f"Request Method: {request_method}\r\n"
            f"Request Source: {connection.getpeername()}\r\n"
            f"Response Status: {status_code} {response_status}\r\n"
        )
        
        connection.send(http_response.encode())

with socket.socket() as serverSocket:
    serverSocket.bind(("127.0.0.1", 40404))
    serverSocket.listen()
    print(f"Listening...")

    try:
        while True:
            (clientConnection, clientAddress) = serverSocket.accept()
            handle_client(clientConnection)
            print(f"Sent data to {clientAddress}")
    except KeyboardInterrupt:
        print("Server stopped by user")
