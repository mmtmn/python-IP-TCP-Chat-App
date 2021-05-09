import socket
import threading

nickname = input("Escolha um nome de usuário: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 42))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                    client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("Um erro ocorreu!")
            client.close()
            break

def write():
    while True:
        a=input("")
        if a == ":feliz:":
            a = ":)"
        elif a == ":triste:":
            a = "):"
        elif a == ":tedio:":
            a = ":|"
        elif a == ":raiva:":
            a = ">:O"
        elif a == ":surpresa:":
            a = ":O"
        elif a == ":rawr:":
            a = "*-*"
        elif a == ":lol:":
            a = ":P"
        else:
            pass
        message = f'{nickname}: {a}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()