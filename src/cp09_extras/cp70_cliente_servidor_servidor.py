import socket

# Crear socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto
server_address = ('localhost', 10000)
sock.bind(server_address)

print('Servidor iniciado, host {} puerto {}'.format(*server_address))

# A escucha de conexiones
sock.listen(1)
while True:
    # Esperar una conexión
    print('Esperando una nueva conexión')
    connection, client_address = sock.accept()
    try:
        print('Conexión desde', client_address)
        # Recibir la información y retransmitirla
        while True:
            data = connection.recv(512)
            if data != b'':
                print(client_address, 'Recibido {!r}'.format(data))
            if data:
                print('Reenviando información al cliente', client_address)
                resp = 'Respuesta del servidor: ' + data.decode('utf-8')
                resp = resp.encode('utf-8')
                connection.sendall(resp)
            else:
                print('Sin datos desde', client_address)
                break
    finally:
        print('Cerrando la conexión con ', client_address)
        connection.close()
