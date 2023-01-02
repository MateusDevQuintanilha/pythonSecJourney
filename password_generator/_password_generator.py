import random, string

height = 16 #Tamanho da senha
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;:/?'#Estrutura exigida para a senha
rnd = random.SystemRandom() #Gerador de números aleatórios fornecidos pelo sistema operacional

#Gerando a senha
print(''.join(rnd.choice(chars) for i in range(height)))