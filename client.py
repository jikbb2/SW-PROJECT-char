import socket

HOST = '192.168.1.4'
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    command = raw_input('Enter your commad:')
    s.send(command)
    reply = s.recv(1024)
    if reply == 'Terminating':
        print reply
        break
    print reply
