import socket

    ### CRIANDO OBJETO DE CONEXÃO ####
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Recebe o protocólo e IP e Datagram IPv4
print('Socket is on')

host = 'localhost' #Rede interna da máquina
port = 5433 #Porta do cliente
message = 'Hi, server!'

try:
    s.sendto(message.encode(), (host, 5432)) #Empacotando e enviando mensagem para o servidor como um datagrama

    data, server = s.recvfrom(4096) #Receber dados em 4096 bytes do servidor
    data = data.decode() #Desempacotando dados
    print('Client: ' + data) #Apresentando dados em forma de mmensagem

finally: #Finalizando a conexão
    print('-' * 35)
    print('Client: Ending the connection...')
    s.close()