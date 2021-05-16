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
        

    def input_serveur(self, message):
    
        #if sock==[]:
        #sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

        #sockt.bind((host, port))
        #print('serveur démarré')
    
        try:
            message = message.encode("utf-8")
            self.conn.sendall(message)
            print('send')
        except:
            print("erreur envoi")
            
        if message!=(b'Joueur 1') and message!=(b'Joueur 2'):
            print('in')
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
        

    def input_client(self):
    
        inpt=''
        while inpt=='':
            try:
                inpt = self.sockt.recv(1024)
                inpt = inpt.decode("utf-8")
                print(inpt)
            except:
                print("error recv")
                
        if inpt=='Joueur 1' or inpt=='Joueur 2':
            return inpt
        
        else:
            case=input(inpt)
    
            try:
                case = case.encode("utf-8")
                self.sockt.sendall(case)
    
            except ConnectionRefusedError:
                print('erreur send')
            return False
        #self.sockt.close()




class clientIn(threading.Thread):
        
    def __init__(self):
        threading.Thread.__init__(self)
        self.sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running=True
                    
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
        if self.running:
            joueur = self.sockt.recv(1024)
            joueur = joueur.decode("utf-8")
            if self.running:
                print(self.running)
                try:
                    joueur = eval(joueur)
                except SyntaxError:
                    self.sockt.close()
                print(joueur)
            
            joueurTir = self.sockt.recv(1024)
            joueurTir = joueurTir.decode("utf-8")
            joueurTir = eval(joueurTir)
            print(joueurTir)
            
            #serv.close()
            return joueur, joueurTir

        
    def stop(self):
        self.running=False
        self.sockt.close()
        


