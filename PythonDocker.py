import webbrowser

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