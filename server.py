
from socket import *

# STUDENTS: randomize this port number (use same one that client uses!)
serverPort = 12000


serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))


serverSocket.listen(1)


print ("The Make Upper Case Server running over TCP is ready to receive ... ")



opcoes = '\n1 - Autentificar\n2 - Cadastrar \n3- Lista de usuarios Ativos \n4 - Lista de usuarios em jogo'

user = {
    'usuario':'usuario',
    'senha': 'senha',
    'ip':'ip',
    'status':'status',
}

listaUsuariosCadastrados = []
listaUsuariosAtivos = []
listaUsuariosJogando = []

connectionSocket, addr = serverSocket.accept()

def enviarParaUsuario(connectionSocket, mensagem):

    connectionSocket.send(mensagem.encode())


while 1:

    # convert the sentence to upper case
	 
    # send back modified sentence over the TCP connection
    enviarParaUsuario(connectionSocket, opcoes)

    opcaoSelecionada = int(connectionSocket.recv(1024))

    if opcaoSelecionada == 1:

        print('------- Iniciando Autenticação -----')
        enviarParaUsuario(connectionSocket, 'Digite seu usuario: ')
        user['usuario'] = str(connectionSocket.recv(1024))
        enviarParaUsuario(connectionSocket, 'Digite sua senha: ')
        user['senha'] = str(connectionSocket.recv(1024)) 

        if len(listaUsuariosCadastrados) > 0:
            for i in listaUsuariosCadastrados:
                if user['usuario'] == listaUsuariosCadastrados[i]['usuario']:
                    if user['senha'] == listaUsuariosCadastrados[i]['senha']:
                        print("Autenticado")
                        listaUsuariosAtivos.append(user)
                        enviarParaUsuario(connectionSocket, 'Autenticado com sucesso')

                else:
                    print("Nao encontrado")
                    enviarParaUsuario(connectionSocket, 'Usuario não cadastrado')

        else:
            print("Não cadastrado")
            enviarParaUsuario(connectionSocket, 'Usuario não cadastrado')

        print("----------------- Fim da autenticação -----------------")

    
    if opcaoSelecionada == 2:

        print('------- Iniciando Cadastro ------- ')
        enviarParaUsuario(connectionSocket, 'Digite seu usuario: ')
        user['usuario'] = str(connectionSocket.recv(1024))
        enviarParaUsuario(connectionSocket, 'Digite sua senha: ')
        user['senha'] = str(connectionSocket.recv(1024)) 

        enviarParaUsuario(connectionSocket, 'Digite seu IP: ')
        user['ip'] = str(connectionSocket.recv(1024))
        enviarParaUsuario(connectionSocket, 'Digite sua porta: ')
        user['porta'] = str(connectionSocket.recv(1024)) 

        listaUsuariosCadastrados.append(user)

        enviarParaUsuario(connectionSocket, 'Cadastro Realizado com sucesso!')

    # output to console the sentence sent back to the client 
    
	 
    # close the TCP connection; the welcoming socket continues
connectionSocket.close()


