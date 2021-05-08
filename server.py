import threading, socket

host = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'conectado com {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)



        print(f'O nome de usuário do cliente é {nickname}!')
        broadcast(f'{nickname} Entrou no grupo!'.encode('ascii'))
        client.send('connectado ao servidor!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("O servidor esta na escuta...")
receive()



