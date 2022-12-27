import socket #Integrando a API Socket do Sistema Operacional
import sys #Acesso a variáveis e funções que interagem com o Python

def main():
    try:

        #### CRIANDO OBJETO DE CONEXÃO ####
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #A variável vai receber os protocólos IP, TCP

    except socket.error as connectionError:

        print('Failed to load the conection.') #Aviso de erro
        print('Error: {}'.format(connectionError)) #Apresentando o erro
        sys.exit() #Fechar o programa em caso de erro

    print('Socket is on.')

    targetHost = input('Digite o host ou IP a ser conectado: ') #Inserindo o Host
    targetPort = input('Digite a porta a ser conectada: ') #Inserindo o TCP

    try:

        #### REALIZANDO CONEXÃO COM O SERVER ####
        s.connect((targetHost, int(targetPort))) #Conectando-se
        print('-' * 30)
        print('#### TCP Client was connected ####')
        print('Host: ' + targetHost)
        print('Port: ' + targetPort)
        s.shutdown(2) #Desligando a conexão

    except socket.error as connectionError:

        print('-' * 40)
        print('The connection was failed')
        print('Error: {}'.format(connectionError))
        print('Port: {}'.format(targetPort))
        print('Host: {}'.format(targetHost))
        sys.exit(5)

if __name__ == "__main__": #Se o nome da função for main, execute:
    main()