#coding:utf-8
import socket, threading, time
import interface as inter

host, port =('localhost',5566) #localhost
#sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class serveur():
    
    def __init__(self, adresse):
        #threading.Thread.__init__(self)
        self.sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockt.bind((adresse, port))
        self.sockt.listen(5)
        print('listen')
        try:
            self.conn, self.adress = self.sockt.accept()
            print('client connecté')
        except:
            print('erreur connexion')
        

    def input_serveur(self, joueur, joueurTir, message, inp):
        testt=True
        if message=='Vous avez gagné !' or message=='Vous avez perdu !':
            testt=False
        #if sock==[]:
        #sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

        #sockt.bind((host, port))
        #print('serveur démarré')
    
        try:
            message = (joueur, joueurTir, message, inp)
            message = str(message)
            message = message.encode("utf-8")
            self.conn.sendall(message)
            print('send')
        except:
            print("erreur envoi")
        print("ttttttttttttttttt", inp)  
        if testt:
            print('in')
            inpt=''
            while inpt=='':
                inpt = self.conn.recv(1024)
            
            inpt = inpt.decode("utf-8")
            inpt = eval(inpt)
            print(inpt)
            print("test")
        

        #conn.close()
        #sockt.close()
       
            return inpt

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
    
    def __init__(self, adresse):
        threading.Thread.__init__(self)
        self.sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
            #connection=False
            #while connection==False:
        try:
            self.sockt.connect((adresse, port))
            print("Client conn")
                #    connection=True
        
        except ConnectionRefusedError:
            print('erreur conn')
                #    connection=False
        

    def input_client(self, selfIn):
        case=[]
        inpt=''
        while inpt=='':
            try:
                inpt = self.sockt.recv(1024)
                inpt = inpt.decode("utf-8")
                inpt = eval(inpt)
                print(inpt)
            except:
                print("error recv")
                
        if inpt[2]=='Vous avez gagné !' or inpt[2]=='Vous avez perdu !':
            #case=inter.interface.affichage(selfIn, inpt[0], inpt[1],  "{} a perdu !".format(inpt[2]), inpt[3])
            inter.interface.affichage(selfIn, inpt[0], inpt[1], inpt[2], inpt[3])
            return True
        
        else:
            #case=input(inpt[2])
            case=inter.interface.affichage(selfIn, inpt[0], inpt[1], inpt[2], inpt[3])

        if case!=[]:
            try:
                case = str(case)
                case = case.encode("utf-8")
                self.sockt.sendall(case)
    
            except ConnectionRefusedError:
                print('erreur send')
            return False
        
    def stop(self):
        self.sockt.close()




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
                    print("erreur fin")
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
        


