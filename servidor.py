"""
Para rodar o projeto, rode em um terminal:
python servidor.py

Em seguida, rode em dois terminais:
python client.py

Por fim, teste a funcionalidade dos dois clientes
com o terminal do servidor avisando o que esta acontecendo

para testar emoji, mande:
:feliz:
:triste:
(para encontrar mais comando do emoji, 
é só dar uma olhada no arquivo do cliente)

----
Caso, alguma biblioteca não funcionar
por favor importe a biblioteca utilizando o pip

bibliotecas utilizadas nos dois arquivos:
pip install socket
pip install threading
----
"""

import threading, socket

host = "127.0.0.1"
porta = 42

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, porta))
servidor.listen()

usuários = []
cliente = []

def transmissão(message):
    for client in cliente:
        client.send(message)

def alça(client):
    while True:
        try:
            message = client.recv(1024)
            transmissão(message)
        except:
            index = cliente.index(client)
            cliente.remove(client)
            client.close()
            username = usuários[index]
            transmissão(f'{username} saiu do chat'.encode('ascii'))
            usuários.remove(username)
            break

def receber():
    while True:
        client, address = servidor.accept()
        print(f'conectado com {str(address)}')

        client.send('USER'.encode('ascii'))
        username = client.recv(1024).decode("ascii")
        usuários.append(username)
        cliente.append(client)

        print(f'O nome de usuário do cliente é {username}!')
        transmissão(f'{username} Entrou no grupo! Seja bem vindo ao software de conversas da APS!'.encode('ascii'))
        client.send('connectado ao servidor!'.encode('ascii'))

        thread = threading.Thread(target=alça, args=(client,))
        thread.start()

print("O servidor esta escutando...\n")
print("[Para fechar o servidor, por favor feche o terminal]\n")
receber()