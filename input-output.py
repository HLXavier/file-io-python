print('-'*20)

file = open('text.txt', 'r')
# 'text.txt' é o nome do arquivo dentro da pasta e 'r' é o mode de leitura (reading)

# Nome do arquivo
print(file.name)

# O modo que ele está sendo usado (no exemplo é 'r')
print(file.mode)

# É sempre necessário fechar o aquivo depois de usá-lo
file.close()

print('-'*20)

with open('text.txt', 'r') as file:
    # Esse é outra forma de abrir um arquivo
    # O código pode ser escrito dentro desse bloco que foi criado
    # Dessa forma não é preciso fechar o arquivo depois de usá-lo
    
    # Lendo o conteúdo do arquivo
    # Podemos passar como parâmetro uma quantidade de caracteres a serem lidos do nosso arquivo --> read(100)
    file_content = file.read()
    print(file_content)

    # Fazendo a leitura do arquivo em chunks de 10 caracteres separado por '*'
    '''
    file_content = file.read(10)
    
    while len(file_content) > 0:
        print(file_content, end='*')
        file_content = file.read(10)
    '''

    print('-'*20)

    # A leitura pode ser feita por linhas em caso de arquivos muito grandes
    # Esse método retorna um vetor de linhas do arquivo:
    '''
    file_content = file.readlines()
    print(file_content)
    '''

    # Também é possível ler uma linha de cada vez
    # Cada nova atribuição é uma nova linha do arquivo
    '''
    file_content = file.readline()
    print(file_content)
    '''

    # Para mostrar cada linha do arquivo podemos usar um iterador:
    '''
    for line in file:
        print(line, end='')
    '''

    # Retorna a posição do arquivo que estamos
    print(file.tell())

    # Seek navega pelos caracteres do arquivo e vai para a posição passada por parâmetro
    print(file.seek(0))
    print(file.read(10))

print('-'*20)

# Escrevendo no arquivo

# Fazer isso apaga todo o conteúdo do texto e reescreve o conteúdo passado como argumento
# Usando o nome 'text2.txt' criamos uma novo arquivo de texto e escrevemos nele
with open('text2.txt', 'w') as file:
    file.write('New text file created')
    file.write('\nMore text')

    # Nesse exemplo também é possível usar o seek() para determinar em qual ponto do arquivo queremos escrever

# Copiando arquivos de texto
with open('text.txt', 'r') as file:
    with open('text-copy.txt', 'w') as file_copy:
        for line in file:
            file_copy.write(line)

# Trabalhando com imagens
# 'rb' é usado para fazer a leitua em bytes
# O arquivo não pode ser lido em UTF-8 
with open('mr-potato.jpg', 'rb') as image:
    #print(image.read())




