import http.server
import socketserver
import webbrowser

# Configura el puerto en el que deseas ejecutar el servidor
PORT = 6368

# Genera el contenido HTML
mensaje = """<html>
<head>
</head>
<body>
<h1>Hola mundo! </h1>
    <p>afk</p>
    <p>Hola colombia</p>
    <p>Felipe Quevedo</p>
    <p>2558346.</p>
</body>
</html>"""

# Guarda el contenido HTML en un archivo dentro del contenedor
with open('/app/holamundo.html', 'w') as f:
    f.write(mensaje)

# Define el controlador de solicitudes HTTP
class MyHandler(http.server.SimpleHTTPRequestHandler):
    pass

# Configura el servidor en el puerto especificado
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Servidor HTTP activo en el puerto", PORT)
    # Abre el navegador en la dirección del servidor
    webbrowser.open_new_tab(f'http://localhost:{PORT}/holamundo.html')
    # Inicia el servidor y espera las solicitudes
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Servidor detenido.")
