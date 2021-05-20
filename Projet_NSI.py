import client_serveur as serv
import threading
import time
import interface as inter

joueur1=([[0 for x in range(10)]for x in range(10)])
joueur2=([[0 for x in range(10)]for x in range(10)])
joueur1Tir=([[0 for x in range(10)]for x in range(10)])
joueur2Tir=([[0 for x in range(10)]for x in range(10)])
bateaux1={'porte-avion': 5, 'croiseur': 4, 'sous-marin': 3, 'contre-torpilleur': 3, 'torpilleur': 2}
bateaux2={'porte-avion': 5, 'croiseur': 4, 'sous-marin': 3, 'contre-torpilleur': 3, 'torpilleur': 2}

bateaux2={'porte-avion': 5}

def initialisation (joueur):
    for cle,valeur in bateaux2.items():
        #bateau1 = list(input("Entrez la première extrémité du {} ({} cases)".format(cle, valeur)))
        #bateau2 = list(input("Entrez la dernière extrémité du {} ({} cases)".format(cle, valeur)))
        bateau1 = inter.interface.affichage(selfIn, joueur, joueur1Tir, "Entrez la première extrémité du {} ({} cases)".format(cle, valeur), True)
        bateau2 = inter.interface.affichage(selfIn, joueur, joueur1Tir, "Entrez la dernière extrémité du {} ({} cases)".format(cle, valeur), True)
        if bateau1[0]==bateau2[0]:
            for i in range(int(bateau1[1])-1,int(bateau2[1])):
                joueur[ord(bateau1[0])-65][i]=cle
        else:
            for i in range(ord(bateau1[0])-65, ord(bateau2[0])-64):
                joueur[i][int(bateau1[1])-1]=cle
                
def initialisation_client (self, joueur):
    
    for cle,valeur in bateaux2.items():
        bateau1, bateau2 = [], []
        while bateau1==[]:
            bateau1 = serv.serveur.input_serveur(self, joueur, joueur1Tir, "Entrez la première extrémité du {} ({} cases)".format(cle, valeur), True)
        while bateau2==[]:
            bateau2 = serv.serveur.input_serveur(self, joueur, joueur1Tir, "Entrez la dernière extrémité du {} ({} cases)".format(cle, valeur), True)
        if bateau1[0]==bateau2[0]:
            for i in range(int(bateau1[1])-1,int(bateau2[1])):
                joueur[ord(bateau1[0])-65][i]=cle
        else:
            for i in range(ord(bateau1[0])-65, ord(bateau2[0])-64):
                joueur[i][int(bateau1[1])-1]=cle
                
    
#initialisation()
#print(joueur1)
#joueur1[0][0]='sous-marin'
#joueur1[1][1]='torpilleur'
def tir(joueurTir, case, bataille):
    if bataille!=None:
        joueurTir[ord(case[0])-65][int(case[1])-1]=2
    else:
        joueurTir[ord(case[0])-65][int(case[1])-1]=1
        



def bataille(joueur, bateaux, case):
    #list(case)
    if joueur[ord(case[0])-65][int(case[1])-1] != 0 :
        if bateaux[joueur[ord(case[0])-65][int(case[1])-1]]-1 == 0:
            bateaux[joueur[ord(case[0])-65][int(case[1])-1]]=0
            return 'Coulé'
        else:
            bateaux[joueur[ord(case[0])-65][int(case[1])-1]] -= 1
            return 'Touché'
    else:
        return None

def perdu():
    if bateaux1['porte-avion']==0:
    #and bateaux1['croiseur']==0 and bateaux1['sous-marin']==0 and bateaux1['contre-torpilleur']==0 and bateaux1['torpilleur']==0:
        return 'Joueur 1'
    elif bateaux2['porte-avion']==0 :
    #and bateaux2['croiseur']==0 and bateaux2['sous-marin']==0 and bateaux2['contre-torpilleur']==0 and bateaux2['torpilleur']==0:
        return 'Joueur 2'
    else:
        return False
        
#bataille(joueur1, 'A1')
#bataille(joueur1, 'B2')
#bataille(joueur1, 'C3')

"""   
class Thread2 (threading.Thread):
    def __init__(self):     
        threading.Thread.__init__(self) 
        self.running = True
        
    def run(self):
        self2=serv.clientIn()
        while self.running:
            serv.clientIn.client_send(self2)
        
            #time.sleep(0.08)
        print('fffffff')
        serv.clientIn.stop(self2)
        
    def stop(self):
        self.running = False
"""        
class Thread3 (threading.Thread):
    def __init__(self):     
        threading.Thread.__init__(self) 
        
    def run(self):
        inter.interface.stop(selfIn)
        
            #time.sleep(0.08)
        print('fffffff')

            

s = Thread3()

     

    
  
selfIn=inter.interface()
#selfLaunch = inter.lauched()
#selfLaunch.start()
mode=inter.interface.menu(selfIn)
#mode=int(input("1. mode 1 ordinateur \n 2. mode réseau (serveur) \n 3. mode réseau (client)"))

if mode==1:

    initialisation(joueur1)
    initialisation(joueur2)
    #inter.interface.affichage(selfIn, joueur2, joueur2Tir, "Joueur 2", False)

    while perdu()==False:
        navale=""
        print(perdu())
        while navale!=None and perdu()==False:
            case = inter.interface.affichage(selfIn, joueur1, joueur1Tir, "Joueur 1, entrez une case", True)
            navale=bataille(joueur2, bateaux2, case)
            print(navale)
            print( bateaux2['porte-avion'])
            tir(joueur1Tir, case, navale)
            inter.interface.affichage(selfIn, joueur1, joueur1Tir, navale, False)
            time.sleep(3)
        
        navale=""
        while navale!=None and perdu()==False:
            case = inter.interface.affichage(selfIn, joueur2, joueur2Tir, "Joueur 2, entrez une case", True)
            navale=bataille(joueur1, bateaux1, case)
            tir(joueur2Tir, case, navale)
            inter.interface.affichage(selfIn, joueur2, joueur2Tir, navale, False)
            time.sleep(3)
            
    print(perdu(), "a perdu !")
    inter.interface.affichage(selfIn, [[0]], [[0]], perdu() + ' a perdu !', False)
    time.sleep(3)
    
    inter.lauched.stop(selfLaunch)
            
elif mode==2:
    
    #s.start()
    self=serv.serveur()
    
    #s.start()
    """
    self2=serv.serveurOut()
    """
    initialisation(joueur1)
    initialisation_client(self, joueur2)
    """
    serv.serveurOut.serv_send(self2, joueur2, joueur2Tir)
    """
    while perdu()==False:
        #serv.serveur(joueur2, joueur2Tir)
        navale=""
        print(perdu())
        while navale!=None and perdu()==False:    
            case = inter.interface.affichage(selfIn, joueur1, joueur1Tir, "Joueur 1, entrez une case", True)
            navale=bataille(joueur2, bateaux2, case)
            #print(navale)
            #print( bateaux2['porte-avion'])
            tir(joueur1Tir, case, navale)
            """
            serv.serveurOut.serv_send(self2, joueur2, joueur2Tir)
            """
            inter.interface.affichage(selfIn, joueur1, joueur1Tir, navale, False)
            time.sleep(3)
            
        #serv.serveur(joueur2, joueur2Tir)
        navale=""
        while navale!=None and perdu()==False:
            case2=[]
            while case2==[]:
                case2 = serv.serveur.input_serveur(self, joueur2, joueur2Tir, "Joueur 2, entrez une case", True)
        
            navale=bataille(joueur1, bateaux1, case2)
            tir(joueur2Tir, case2, navale)
            """
            serv.serveurOut.serv_send(self2, joueur2, joueur2Tir)
            """
            
    serv.serveur.input_serveur(self, joueur2, joueur2Tir, perdu(), False)
    print(perdu(), 'a perdu !')
    
elif mode==3:
    #while perdu()==False:
        #serv.client()
    self=serv.client()
    #self2=serv.clientIn()
    """
    i= Thread2()
    i.start()
    """
    #serv.client()
    perdu=False
    while not perdu:
        perdu=serv.client.input_client(self, selfIn)
    """
    Thread2().stop()
    """
    print(perdu, 'a perdu !')
    
        
   
