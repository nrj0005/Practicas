from http.server import BaseHTTPRequestHandler, HTTPServer

# Definimos un manejador simple
class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respuesta 200 OK
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Contenido que se mostrará en la página
        self.wfile.write(b"<html><body><h1>Hello World!</h1></body></html>")

# Iniciar el servidor
if __name__ == "__main__":
    puerto = 8000
    servidor = HTTPServer(('', puerto), HelloHandler)
    print(f"Servidor en marcha en http://localhost:{puerto}")
    servidor.serve_forever()
    
