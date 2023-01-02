import hashlib

#Transformando os arquivos em objetos
txt1 = 'hash1.txt'
txt2 = 'hash2.txt'

file1 = open(txt1, 'rb').read()
file2 = open(txt2, 'rb').read()
file_list = [file1, file2]

m = hashlib.new('ripemd160')

for i in file_list:
    m.update(i)

    print(m.digest())


#Algoritmo de Hash que será usado
# hash1 = hashlib.new('ripemd160').hexdigest()
# hash2 = hashlib.new('ripemd160').hexdigest()

# hash1.update(open(txt1, 'rb').read()) #Gerar o hash do arquivo 1
# hash2.update(open(txt2, 'rb').read()) #Gerar o hash do arquivo 2

# if hash1.digest() != hash2.digest():
#     print(f'The archive {txt1} is different than archieve {txt2}')
# else:
#     print('Both archives have the same Hash')