#coding:utf-8
import socket, time
import interface as inter

host, port =('localhost',5566) #localhost

class serveur():
    
    def __init__(self, adresse):
        self.sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockt.bind((adresse, port))
        self.sockt.listen(5)
        print('listen')
        try:
            self.conn, self.adress = self.sockt.accept()
            print('client connecté')
        except:
            print('erreur connexion')
        

    def input_serveur(self, joueur, joueurTir, joueurTir_2, message, inp):
        testt=True
        if message=='Vous avez gagné !' or message=='Vous avez perdu !':
            testt=False
        #print('serveur démarré')
    
        try:
            message = (joueur, joueurTir, joueurTir_2, message, inp)
            message = str(message)
            message = message.encode("utf-8")
            self.conn.sendall(message)
            print('send')
        except:
            print("erreur envoi")
        print(inp)  
        if testt:
            print('in')
            inpt=''
            while inpt=='':
                inpt = self.conn.recv(1024)
            
            inpt = inpt.decode("utf-8")
            inpt = eval(inpt)
            print(inpt)
            print("test")
        
            return inpt
        
    def stop(self):
        self.sockt.close()
        self.conn.close()


class client():
    
    def __init__(self, adresse):
        self.sockt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.etat = False 
                
        try:
            self.sockt.connect((adresse, port))
            print("Client conn")
                #    connection=True
        
        except ConnectionRefusedError:
            print('erreur conn')
                #    connection=False
        

    def input_client(self, selfIn):
        self.etat = True  
        case=[]
        inpt=''
        while inpt=='':
            try:
                inpt = self.sockt.recv(2048)
                inpt = inpt.decode("utf-8")
                inpt = eval(inpt)
                print(inpt)
            except:
                print("error recv")
                
        if inpt[3]=='Vous avez gagné !' or inpt[3]=='Vous avez perdu !':
            #case=inter.interface.affichage(selfIn, inpt[0], inpt[1],  "{} a perdu !".format(inpt[2]), inpt[3])
            inter.interface.affichage(selfIn, inpt[0], inpt[1], inpt[2], inpt[3], inpt[4])
            self.etat = False
            return True
        
        else:
            inter.interface.son(selfIn, inpt[3])
            case=inter.interface.affichage(selfIn, inpt[0], inpt[1], inpt[2], inpt[3], inpt[4])

        if case!=[]:
            try:
                case = str(case)
                case = case.encode("utf-8")
                self.sockt.sendall(case)
    
            except ConnectionRefusedError:
                print('erreur send')
            self.etat = False
            return False
        self.etat = False
  
    def stop(self):
        self.sockt.close()

