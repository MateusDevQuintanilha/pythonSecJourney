import os # Integra o sistema operacional

print('#' * 40) # Customização
ip_ou_host = input('Digite o IP ou Host a ser verificado: ') # Recebimento da informação

print('-' * 55) # Customização
os.system('ping -c 6 {}'.format(ip_ou_host)) # Velocidade de processamento
print('-' * 55) # Customização
