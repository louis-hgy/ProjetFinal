#coding:utf-8
import socket

host, port =('localhost',5566)

socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def serveur(joueur, joueurTir):
    socket.bind((host, port))
    print('serveur démarré')

    while True:
        socket.listen(5)
        conn, adress = socket.accept()
        print('client connecté')
    
        joueur = joueur.encode("utf-8")
        conn.sendall(joueur)
        
        joueurTir = joueurTir.encode("utf-8")
        conn.sendall(joueurTir)
        
    
def input_serveur(message):
    
    socket.bind((host, port))
    print('serveur démarré')

    socket.listen(5)
    conn, adress = socket.accept()
    print('client connecté')
    
    message = message.encode("utf-8")
    conn.sendall(message)
    
    input=''
    while input=='':
        input = conn.recv(1024)
        input = input.decode("utf-8")
        print(input)
        print("test")
        

    conn.close()
    socket.close()
       
    return input
    


def client():
    socket.connect((host, port))
    while True:
        joueur = socket.recv(1024)
        joueur = joueur.decode("utf-8")
        print(joueur)
        
        joueurTir = socket.recv(1024)
        joueurTir = joueurTir.decode("utf-8")
        print(joueurTir)
    
    return Joueur, joueurTir

def input_client():
    socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket.connect((host, port))
        print("Client conn")
    
    except ConnectionRefusedError:
        print('erreur')
        
    inpt=''
    while inpt=='':
        inpt = socket.recv(1024)
        inpt = inpt.decode("utf-8")
        print(inpt)
        
    case=input(inpt)
    
    try:
        case = case.encode("utf-8")
        socket.sendall(case)
    
    except ConnectionRefusedError:
        print('erreur')
    socket.close()

    

  
"""
if input('rrr')=='s':
    serveur()
elif input('eee')=='c':
    client()
"""

#conn.close()
#socket.close()


