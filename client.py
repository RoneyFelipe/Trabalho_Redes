from socket import *

# STUDENTS - replace your server machine's name 
serverName = "127.0.0.1" # ou "localhost" ou o IP do servidor

# STUDENTS - you should randomize your port number.         
# This port number in practice is often a "Well Known Number"  
serverPort = 12000

# create TCP socket on client to use for connecting to remote
# server.  Indicate the server's remote listening port
# Error in textbook?   socket(socket.AF_INET, socket.SOCK_STREAM)  Amer 4-2013 
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName,serverPort))

# interactively get user's line to be converted to upper case
# authors' use of raw_input changed to input for Python 3  Amer 4-2013
print("--------------- Conexão feita! -------------------")

def autenticaoSelecionada():

    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())

    usuario = input()

    clientSocket.send(usuario.encode())

    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())

    senha = input()

    clientSocket.send(senha.encode())

    modifiedSentence = clientSocket.recv(1024)

    print(modifiedSentence.decode())


def cadastroSelecionado():

    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())

    usuario = input()

    clientSocket.send(usuario.encode())

    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())

    senha = input()

    clientSocket.send(senha.encode())

    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())

    ip = input()

    clientSocket.send(ip.encode())

    modifiedSentence = clientSocket.recv(1024)

    print(modifiedSentence.decode())

    porta = input()

    clientSocket.send(porta.encode())

    modifiedSentence = clientSocket.recv(1024)

    print(modifiedSentence.decode())

def selecionandoOpcao():

    opcaoselecionada = input("Selecione uma das opcoes acima:")
    clientSocket.send(opcaoselecionada.encode())

    if opcaoselecionada == '1':
        autenticaoSelecionada()
        print('-------------- Fim autenticação --------------')

    elif opcaoselecionada == '2':
        cadastroSelecionado()
        print('-------------- Fim Cadastro --------------')


while 1:
#output to console what is sent to the server

# get user's line back from server having been modified by the server
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())

    selecionandoOpcao()

# close the TCP connection
clientSocket.close()

