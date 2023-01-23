import os #Integra o sistema operacional
import time #Tempo de execução

with open('hosts.txt') as file: #Com a abertura do "hosts.txt" como arquivo
    dump = file.read() #Ler o arquivo e jogar os dados dentro do dump
    dump = dump.splitlines() #Organizar as linhas na horizontal
    print('Dumping...')
    for ip in dump: #Para cada IP no dump
        os.system('ping -c 2 {}'.format(ip)) #Apresenta o Ping de cada host
        time.sleep(5) #Intervalo de 5 segundos para cada Ping