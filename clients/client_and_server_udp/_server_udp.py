import socket

        ### CRIANDO OBJETO DE CONEXÃO ####

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket is on')

host = 'localhost' #Rede interna da máquina
port = 5432 #Porta do servidor

s.bind((host, port)) #Conectando cliente e servidor

message = "\nServer: Don't talk with me, i'm sleeping"


while 1:

    data, address = s.recvfrom(4096) #Dados e endereço do server

    if data:
        print('Server is sending a message...')
        s.sendto(data + (message.encode()), address) #Enviando mensagem ao cliente com o endereço do server

