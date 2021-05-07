#coding:utf-8
import socket

host, port =('localhost',5566)


#sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def serveur(joueur, joueurTir):
    serv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((host, 5560))
    #print('serveur démarré')

    while True:
        serv.listen(5)
        conn, adress = serv.accept()
        #print('client connecté')
    
        joueur = str(joueur)
        joueur = joueur.encode("utf-8")
        conn.sendall(joueur)
        
        joueurTir = str(joueurTir)
        joueurTir = joueurTir.encode("utf-8")
        conn.sendall(joueurTir)
        
    conn.close()
    serv.close()
        
    
def input_serveur(message):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sock.bind((host, port))
    #print('serveur démarré')

    sock.listen(5)
    conn, adress = sock.accept()
    #print('client connecté')
    
    message = message.encode("utf-8")
    conn.sendall(message)
    
    input=''
    while input=='':
        input = conn.recv(1024)
        input = input.decode("utf-8")
        #print(input)
        #print("test")
        

    conn.close()
    sock.close()
       
    return input
    


def client():
    serv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    serv.connect((host, 5560))
    while True:
        joueur = serv.recv(1024)
        joueur = joueur.decode("utf-8")
        joueur = eval(joueur)
        #print(joueur)
        
        joueurTir = serv.recv(1024)
        joueurTir = joueurTir.decode("utf-8")
        joueur = eval(joueur)
        #print(joueurTir)
        
    serv.close()
    return Joueur, joueurTir

def input_client():
    sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sockt.connect((host, port))
        #print("Client conn")
    
    except ConnectionRefusedError:
        print('erreur')
        
    inpt=''
    while inpt=='':
        try:
            inpt = sockt.recv(1024)
            inpt = inpt.decode("utf-8")
            print(inpt)
        except:
            None
        
    case=input(inpt)
    
    try:
        case = case.encode("utf-8")
        sockt.sendall(case)
    
    except ConnectionRefusedError:
        print('erreur')
    sockt.close()

    

  
"""
if input('rrr')=='s':
    serveur()
elif input('eee')=='c':
    client()
"""

#conn.close()
#socket.close()


