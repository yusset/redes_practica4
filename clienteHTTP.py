
import socket
import argparse

def constructHTTPRequest(host, http_method, url, user_agent, encoding, connection):
    # Construcción de la solicitud HTTP
    request_line = f"{http_method} {url} HTTP/1.1\r\n"
    header_lines = f"Host: {host}\r\nUser-Agent: {user_agent}\r\nAccept-Encoding: {encoding}\r\nConnection: {connection}\r\n\r\n"
    HTTP_request = request_line + header_lines
    return HTTP_request

def TCPconnection(host, HTTP_request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 80))
    s.send(HTTP_request.encode())

    while True:
        HTTP_response = s.recv(1024)
        if not HTTP_response:
            break
        print(HTTP_response.decode())
    
    s.close()
    print("\n\nConexión con el servidor finalizada\n")

def main():
    parser = argparse.ArgumentParser(description="Cliente HTTP simple")
    parser.add_argument("host", help="Host del servidor")
    parser.add_argument("http_method", help="Método HTTP (por ejemplo, GET)")
    parser.add_argument("url", help="URL del recurso")
    parser.add_argument("user_agent", help="User-Agent")
    parser.add_argument("encoding", help="Accept-Encoding")
    parser.add_argument("connection", help="Connection")
    args = parser.parse_args()

    HTTP_request = constructHTTPRequest(args.host, args.http_method, args.url, args.user_agent, args.encoding, args.connection)
    TCPconnection(args.host, HTTP_request)

if __name__ == "__main__":
    main()
