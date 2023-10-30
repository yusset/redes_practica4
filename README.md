# Práctica 4: Programación de un cliente de HTTP y uso de contenedores.
## Funcionamiento 
1.Simplemente se debe descargar este repositorio. 

1. Asegurarse de instalar Dockerfile, yo utilicé Windows ya que accidentalmente se borró mi sispetema operativo Linux, [aquí] (https://docs.docker.com/desktop/install/windows-install/) las instrucciones para hacerlo.
1. Después en la Powershell se correrá:
   
 `docker build -t nombre_de_la_imagen .`
1. Y para ejecutar el programa:
   
 `docker run -it --rm nombre_de_la_imagen argumentos `
 
Recordemos que los argumentos son: 

`host http_method url user_agent encoding connection `

Ejemplo:
` `
## Evaluación 

- ¿Cual es la funcion de los métodos de HTTP *HEAD* *GET* *POST* *PUT* *DELETE*?

 GET: Solicita la recuperación de un recurso específico, generalmente identificado por una URL. El servidor responde enviando el recurso solicitado en el cuerpo de la respuesta. Es un método seguro y no debe tener ningún efecto secundario en el servidor ni en los datos.
   
HEAD: Similar a GET, pero solicita solo los encabezados de la respuesta, sin el cuerpo del recurso. Se utiliza para obtener información sobre el recurso, como el tipo de contenido o la última fecha de modificación, sin descargar el recurso completo.
  
POST: Envia datos al servidor para que los procese. A menudo se utiliza para enviar datos del usuario al servidor, como formularios web. Puede tener efectos secundarios en el servidor, como la creación de un nuevo recurso, la actualización de datos o el procesamiento de una acción específica.
  
PUT: Actualiza un recurso existente o crea uno nuevo si no existe en la ubicación especificada. El cuerpo de la solicitud contiene la representación completa del recurso actualizado o nuevo.
    
DELETE: Solicita la eliminación de un recurso en la ubicación especificada. El servidor debe eliminar el recurso si es posible.


- Investigue y enliste junto con sus significado las categorias de los codigos de estado que utiliza HTTP.

1. **Success - 2xx**:
   - 200 OK: La solicitud se ha completado con éxito. El servidor ha devuelto la respuesta solicitada.
   - 201 Created: La solicitud ha resultado en la creación exitosa de un nuevo recurso.
   - 204 No Content: La solicitud se ha completado con éxito, pero no hay contenido en la respuesta.

2. **Redirection - 3xx**:
   - 301 Moved Permanently: La página solicitada ha sido trasladada permanentemente a una nueva ubicación.
   - 302 Found (o 303 See Other): La página solicitada se ha trasladado temporalmente a una nueva ubicación.
   - 304 Not Modified: El recurso no ha cambiado desde la última solicitud, por lo que no se envía de nuevo.

3. **Client Errors - 4xx**:
   - 400 Bad Request: La solicitud es incorrecta o no se puede entender por el servidor.
   - 401 Unauthorized: Se requiere autenticación para acceder al recurso.
   - 403 Forbidden: El servidor entiende la solicitud, pero no la va a cumplir.
   - 404 Not Found: El recurso solicitado no se encuentra en el servidor.

4. **Server Errors - 5xx**:
   - 500 Internal Server Error: El servidor ha encontrado una situación imprevista que le impide cumplir con la solicitud.
   - 502 Bad Gateway: El servidor, mientras actuaba como puerta de enlace o proxy, recibió una respuesta no válida del servidor ascendente.
   - 503 Service Unavailable: El servidor no está disponible temporalmente, generalmente debido a una sobrecarga o mantenimiento.

5. **Informational - 1xx**:
   - 100 Continue: El servidor ha recibido la solicitud y está esperando que el cliente continúe con la solicitud.
   - 101 Switching Protocols: El servidor acepta cambiar el protocolo solicitado.

- ¿Para qué se usan los campos de *encoding* y *connection*?  
Los campos `Encoding` y `Connection` son cabeceras HTTP que se utilizan para controlar aspectos relacionados con la codificación de contenido y la conexión entre el cliente y el servidor. 

1. **`Encoding`**:

   - **Accept-Encoding**: El cliente puede enviar esta cabecera en una solicitud HTTP para indicar al servidor qué algoritmos de compresión de contenido (codificación) puede entender. Algunos de los valores comunes incluyen "gzip," "deflate," y "br" (Brotli). El servidor puede comprimir el contenido de la respuesta antes de enviarlo al cliente si es compatible con la codificación especificada. Esto reduce el tamaño de los datos transmitidos y acelera la transferencia.

   - **Content-Encoding**: El servidor utiliza esta cabecera en la respuesta para indicar que el contenido de la respuesta ha sido comprimido con un algoritmo específico antes de ser enviado al cliente. El cliente debe descomprimir el contenido para acceder a los datos.

   - **Transfer-Encoding**: Indica cómo se ha codificado el contenido en la respuesta, como chunked (dividido en fragmentos), gzip, deflate, etc.

2. **`Connection`**:

   - **Connection**: Esta cabecera se utiliza para controlar la persistencia de la conexión entre el cliente y el servidor. Los valores comunes incluyen "keep-alive" y "close."
     - "keep-alive": Indica que la conexión debe mantenerse abierta para permitir la reutilización de la misma conexión para varias solicitudes y respuestas. Esto puede mejorar el rendimiento, ya que evita la sobrecarga de abrir y cerrar conexiones para cada solicitud.
     - "close": Indica que la conexión debe cerrarse después de la respuesta, lo que significa que no se reutilizará.

   - **Proxy-Connection**: Esta cabecera es similar a "Connection" pero se usa cuando un cliente se conecta a través de un proxy. Puede controlar si la conexión se mantiene viva o se cierra en la comunicación entre el cliente, el proxy y el servidor.
