#(i) create a connection socket when contacted by a client (browser);
#(ii) receive the HTTP requestfrom this connection;
#(iii) parse the request to determine the specific file being requested; 
#(iv) get the requested file from the server’s file system; 
#(v) create an HTTP response message consisting of the requested file preceded by header lines;
#(vi) send the response over the TCP connection to the requesting browser

import socket
# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Parse HTTP headers
    headers = request.split('\n')
    filename = headers[0].split()[1]

    # Get the content of the file
    if filename == '/':
      filename = '/index.html'
      
    try:
      fin = open('files' + filename)
      content = fin.read()
      fin.close()
      
      # Send HTTP response
      response = 'HTTP/1.0 200 OK\n\n' + content
      
    except FileNotFoundError:
      response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
      
    client_connection.sendall(response.encode())
    client_connection.close()
    
    print("break the loop")

# Close socket
server_socket.close()