import socket 

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print ("El nombre de su equipo es: " + hostname)
print ("La direccion ip de su equipo es: " + ip)