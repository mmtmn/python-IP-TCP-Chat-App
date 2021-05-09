import socket
import threading
import os

print("\n Seja bem vindo ou bem vinda ao software de conversas da APS 2021!")
input("\n\n Aperte qualquer coisa para continuar...")
os.system('cls || clear')

quit = print("[PARA SAIR, APERTE CONTROL E C AO MESMO TEMPO]")
username = input("\nEscolha um nome de usuário: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 42))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'USER':
                    client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print("Um erro ocorreu!")
            client.close()
            break

def write():
    while True:
        text_message=input("Mande uma mensagem: ")
        # --- emojis ---
        if text_message == ":feliz:":
            text_message = ":)"
        elif text_message == ":triste:":
            text_message = "):"
        elif text_message == ":tedio:":
            text_message = ":|"
        elif text_message == ":raiva:":
            text_message = ">:O"
        elif text_message == ":surpresa:":
            text_message = ":O"
        elif text_message == ":rawr:":
            text_message = "*-*"
        elif text_message == ":lol:":
            text_message = ":P"
        else:
            pass
        message = f'{username}: {text_message}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()