"""
Para rodar o projeto, rode em um terminal:
python server.py

Em seguida, rode em dois terminais:
python cliente.py

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

import socket
import threading
import os

print("\n Seja bem vindo ou bem vinda ao software de conversas da APS 2021!")
input("\n\n Aperte qualquer coisa para continuar...")
os.system('cls || clear')

sair = print("[PARA SAIR, APERTE CONTROL E C AO MESMO TEMPO]")
usuário = input("\nEscolha um nome de usuário: ")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 42))

def receber():
    while True:
        try:
            mensagem = cliente.recv(1024).decode('ascii')
            if mensagem == 'USER':
                    cliente.send(usuário.encode('ascii'))
            else:
                print(mensagem)
        except:
            print("Um erro ocorreu!")
            cliente.close()
            break

def escrever():
    while True:
        texto_de_mensagem=input("Mande uma mensagem: ")
        # --- emojis ---
        if texto_de_mensagem == ":feliz:":
            texto_de_mensagem = ":)"
        elif texto_de_mensagem == ":triste:":
            texto_de_mensagem = "):"
        elif texto_de_mensagem == ":tedio:":
            texto_de_mensagem = ":|"
        elif texto_de_mensagem == ":raiva:":
            texto_de_mensagem = ">:O"
        elif texto_de_mensagem == ":surpresa:":
            texto_de_mensagem = ":O"
        elif texto_de_mensagem == ":rawr:":
            texto_de_mensagem = "*-*"
        elif texto_de_mensagem == ":lol:":
            texto_de_mensagem = ":P"
        else:
            pass
        mensagem = f'{usuário}: {texto_de_mensagem}'
        cliente.send(mensagem.encode('ascii'))

receber_thread = threading.Thread(target=receber)
receber_thread.start()

escrever_thread = threading.Thread(target=escrever)
escrever_thread.start()