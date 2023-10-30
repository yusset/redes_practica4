# Módulos de Python
import socket
import sys

def processArguments():
    # Recibe de la línea de comandos un argumento
    host_server = sys.argv[1]

    arguments = [host_server]

    return arguments

def constructHTTPRequest(host_server):
    # Construcción de la línea de solicitud HTTP
    http_method = "GET"
    url = "/"
    version = "HTTP/1.1"
    request_line = http_method + " " + url + " " + version + "\r\n"

    # Construcción de las cabeceras HTTP
    # Cada parámetro debe terminar con un retorno de carro
    # y un salto de línea
    host = "Host: " + host_server
    user_agent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299 Firefox/74.0"
    accept_encoding = "Accept-Encoding: identity"
    accept_language = "Accept-Language: en-US"

    header_lines = host + "\r\n" + \
        user_agent + "\r\n" + \
        accept_encoding + "\r\n" + \
        accept_language + "\r\n"

    # Que termine con un retorno de carro y salto de línea
    blank_line = "\r\n"

    # Concatenación de cada parámetro
    HTTP_request = request_line + \
        header_lines + \
        blank_line
    return HTTP_request

def TCPconnection(host_server, HTTP_request):
    # Crea un socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conexión del cliente al servidor dado con el puerto 80 para HTTP
    s.connect((host_server, 80))

    # Envía la petición HTTP al servidor
    s.send(HTTP_request.encode())

    # Mientras reciba la información del servidor la guardará
    # en HTTP_response e imprimirá en pantalla
    while True:
        HTTP_response = s.recv(1024)
        if not HTTP_response:
            break
        print(HTTP_response.decode())
    # Una vez que ha terminado la recepción de información, se cierra la conexión
    s.close()

    print("\n\nConexión con el servidor finalizada\n")

arguments = processArguments()
HTTP_request = constructHTTPRequest(*arguments)
TCPconnection(arguments[0], HTTP_request)
