if sentence == "1":

        connectionSocket.send("usuario:")
        
        user['usuario'] = connectionSocket.recv(1024)
        connectionSocket.send("senha:")

        user['senha'] = connectionSocket.recv(1024)        
        
        for i in list_user_regisrados:
            if user['usuario'] == list_user_regisrados[i]['usuario']:
                if user['senha'] == list_user_regisrados[i]['senha']:
                    print("Autenticado")
                    list_user_online.append(user)

        else:
            print("Nao encontrado")
            
        opcoes()

        sentence = connectionSocket.recv(1024)

        # pedir conexao p2p
        #if sentence == "5":

    if sentence == '2':

        list_user_regisrados = cadastrar_user(connectionSocket, user)


    if sentence == '3':
        for user in list_user_online:
            print(f"Usuário: {user['usuario']}, Porta: {user['porta']}, IP: {user['ip']}")
    
    # output to console the sentence received from the client 