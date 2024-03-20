import http.server
import socketserver
import webbrowser

# Configura el puerto en el que deseas ejecutar el servidor
PORT = 6368

# Define el controlador de solicitudes HTTP
class MyHandler(http.server.SimpleHTTPRequestHandler):
    pass

# Configura el servidor en el puerto especificado
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Servidor HTTP activo en el puerto", PORT)
    # Abre el navegador en la dirección del servidor
    webbrowser.open_new_tab(f'http://localhost:{PORT}/PythonDocker.py')
    # Inicia el servidor y espera las solicitudes
    httpd.serve_forever()

f = open('holamundo.html','w')

mensaje = """<html>
<head></head>
<body><p>Hola Mundo!</p>
<p>Hola ficha</p>
<p>2558346</p></body>
</html>"""

f.write(mensaje)
f.close()


webbrowser.open_new_tab('holamundo.html')
