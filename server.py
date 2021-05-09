import threading, socket

host = "127.0.0.1"
port = 42

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

usernames = []
clients = []

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
            username = usernames[index]
            broadcast(f'{username} saiu do chat'.encode('ascii'))
            usernames.remove(username)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'conectado com {str(address)}')

        client.send('USER'.encode('ascii'))
        username = client.recv(1024).decode("ascii")
        usernames.append(username)
        clients.append(client)

        print(f'O nome de usuário do cliente é {username}!')
        broadcast(f'{username} Entrou no grupo! Seja bem vindo ao software de conversas da APS!'.encode('ascii'))
        client.send('connectado ao servidor!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("O servidor esta escutando...\n")
print("[Para fechar o servidor, por favor feche o terminal]\n")
receive()