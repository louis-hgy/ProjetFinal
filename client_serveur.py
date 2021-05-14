#coding:utf-8
import socket, threading, time

host, port =('localhost',5566)
#sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class serveur(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockt.bind((host, port))
        self.sockt.listen(5)
        print('listen')
        try:
            self.conn, self.adress = self.sockt.accept()
            print('client connecté')
        except:
            print('erreur connexion')
        print('ffggtrrthyhyt')
        
    """
    def run(self):
        
        self.sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockt.bind((host, port))
        self.sockt.listen(5)
        print('listen')
        try:
            self.conn, self.adress = self.sockt.accept()
            print('client connecté')
        except:
            print('erreur connexion')
        print('ffggtrrthyhyt')
        return self
    """
    
    def serv_send(joueur, joueurTir):
        serv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.bind((host, 5576))
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

    def input_serveur(self, message):
    
        #if sock==[]:
        #sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

        #sockt.bind((host, port))
        #print('serveur démarré')
        """
        sockt.listen(5)
        print('listen')
        try:
            conn, adress = sockt.accept()
            print('client connecté')
        except:
            print('erreur connexion')
        print('ffggtrrthyhyt')
        """
        try:
            message = message.encode("utf-8")
            self.conn.sendall(message)
            print('send')
        except:
            print("erreur envoi")
        
        input=''
        while input=='':
            input = self.conn.recv(1024)
            
        input = input.decode("utf-8")
        print(input)
        print("test")
        

        #conn.close()
        #sockt.close()
       
        return input

class serveurOut(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockt.bind((host, 5576))
        self.sockt.listen(5)
        print('listen')
        try:
            self.conn, self.adress = self.sockt.accept()
            print('client connecté')
        except:
            print('erreur connexion')
        print('ffggtrrthyhyt')

    def serv_send(self, joueur, joueurTir):
            print(joueur)
            joueur = str(joueur)
            joueur = joueur.encode("utf-8")
            self.conn.sendall(joueur)
            time.sleep(0.08)
    
            joueurTir = str(joueurTir)
            joueurTir = joueurTir.encode("utf-8")
            self.conn.sendall(joueurTir)
    
        #conn.close()
        #serv.close()





class client(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
            #connection=False
            #while connection==False:
        try:
            self.sockt.connect((host, port))
            print("Client conn")
                #    connection=True
        
        except ConnectionRefusedError:
            print('erreur conn')
                #    connection=False
        
                
    def client_send():
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

    def input_client(self):
        """
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        connection=False
        while connection==False:
            try:
                sockt.connect((host, port))
                print("Client conn")
                connection=True
    
            except ConnectionRefusedError:
                print('erreur conn')
                connection=False
        """

        
        inpt=''
        while inpt=='':
            try:
                inpt = self.sockt.recv(1024)
                inpt = inpt.decode("utf-8")
                print(inpt)
            except:
                print("error recv")
                
       
        
        case=input(inpt)
    
        try:
            case = case.encode("utf-8")
            self.sockt.sendall(case)
    
        except ConnectionRefusedError:
            print('erreur send')
        #self.sockt.close()




class clientIn(threading.Thread):
        
    def __init__(self):
        threading.Thread.__init__(self)
        self.sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    
            #connection=False
            #while connection==False:
        try:
            self.sockt.connect((host, 5576))
            print("Client conn 5576")
                #    connection=True
        
        except ConnectionRefusedError:
            print('erreur conn')
                #    connection=False
        
                
    def client_send(self):
        #while True:
        joueur = self.sockt.recv(1024)
        joueur = joueur.decode("utf-8")
        joueur = eval(joueur)
        print(joueur)
            
        joueurTir = self.sockt.recv(1024)
        joueurTir = joueurTir.decode("utf-8")
        joueurTir = eval(joueurTir)
        print(joueurTir)
            
        #serv.close()
        return joueur, joueurTir


















"""
def init():
    print('ttt')
    sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockt.bind((host, port))

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
 
#sock=[]
def input_serveur(message):
    
    #if sock==[]:
        #sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

    #sockt.bind((host, port))
    #print('serveur démarré')




    sockt.listen(5)
    conn, adress = sockt.accept()
    #print('client connecté')
    try:
        message = message.encode("utf-8")
        conn.sendall(message)
    except:
        print("err")
        
    input=''
    while input=='':
        input = conn.recv(1024)
        input = input.decode("utf-8")
        #print(input)
        #print("test")
        

    conn.close()
    sockt.close()
       
    return input
"""

"""
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
    connection=False
    while connection==False:
        try:
            sockt.connect((host, port))
        #print("Client conn")
            connection=True
    
        except ConnectionRefusedError:
            print('erreur1')
            connection=False
        
        
    inpt=''
    while inpt=='':
        try:
            inpt = sockt.recv(1024)
            inpt = inpt.decode("utf-8")
            #print(inpt)
        except:
            print("error")
        
    case=input(inpt)
    
    try:
        case = case.encode("utf-8")
        sockt.sendall(case)
    
    except ConnectionRefusedError:
        print('erreur2')
    sockt.close()

"""

  
"""
if input('rrr')=='s':
    serveur()
elif input('eee')=='c':
    client()
"""

#conn.close()
#socket.close()


