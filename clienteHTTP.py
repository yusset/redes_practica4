# paquetes necesatios
import socket
import argparse

# Opciones predefinidas para User-Agent con windows
user_agent_options = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"
]

def constructHTTPRequest(host, http_method, url, user_agent_choice, encoding, connection):
    # Selecciona el User-Agent según el número elegido por el usuario
    user_agent = user_agent_options[user_agent_choice - 1]

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
    parser.add_argument("user_agent_choice", type=int, choices=[1, 2, 3], help="Elija una opción para User-Agent (1, 2 o 3)")
    parser.add_argument("encoding", help="Accept-Encoding")
    parser.add_argument("connection", help="Connection")
    args = parser.parse_args()

    HTTP_request = constructHTTPRequest(args.host, args.http_method, args.url, args.user_agent_choice, args.encoding, args.connection)
    TCPconnection(args.host, HTTP_request)

if __name__ == "__main__":
    main()
