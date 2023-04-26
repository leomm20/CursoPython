import socket

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor
server_address = ('localhost', 10000)

print('Conectando con el servidor. Host {} puerto {}'.format(*server_address))

sock.connect(server_address)

try:
    # Enviar datos
    message = b'Este es el mensaje.'
    print('Enviando {!r}'.format(message))
    sock.sendall(message)
    # Esperar la respuesta
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(512)
        amount_received += len(data)
        print('Recibido {!r}'.format(data))
finally:
    print('Cerrando socket')
    sock.close()
