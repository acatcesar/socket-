import socket
HOST = 'localhost'
PORT = 8003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria uma conexão

sock.bind((HOST, PORT))

sock.listen(5) #suporta até 5 clientes

while True:
    novoSock, _ = sock.accept()
    nomeArquivo = novoSock.recv(1024).decode()
    novoArquivo = novoSock.recv(100000000)

    # print(mensagem)
    # novoSock.send(b'ok')

    with open(f'arquivos/{nomeArquivo}.png', 'wb') as arq:
        arq.write(novoArquivo)

    novoSock.send(b'ok')

