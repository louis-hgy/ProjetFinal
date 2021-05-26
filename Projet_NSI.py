import client_serveur as serv
import interface as inter
import time


joueur1=([[0 for x in range(10)]for x in range(10)])
joueur2=([[0 for x in range(10)]for x in range(10)])
joueur1Tir=([[0 for x in range(10)]for x in range(10)])
joueur2Tir=([[0 for x in range(10)]for x in range(10)])
bateaux1={'porte-avion': 5, 'croiseur': 4, 'sous-marin': 3, 'contre-torpilleur': 3, 'torpilleur': 2}
bateaux2={'porte-avion': 5, 'croiseur': 4, 'sous-marin': 3, 'contre-torpilleur': 3, 'torpilleur': 2}

#bateaux2={'porte-avion': 5}

def initialisation (joueur):
    for cle,valeur in bateaux2.items():
        case=False
        while not case:
            bateau1 = inter.interface.affichage(selfIn, joueur, joueur1Tir, joueur2Tir, "Cliquez sur la première extrémité du {} ({} cases)".format(cle, valeur), True)
            bateau2 = inter.interface.affichage(selfIn, joueur, joueur1Tir, joueur2Tir, "Cliquez sur la dernière extrémité du {} ({} cases)".format(cle, valeur), True)
            if bateau1[0]==bateau2[0]:
                if int(bateau1[1])-1-int(bateau2[1])==-valeur:
                    for i in range(int(bateau1[1])-1,int(bateau2[1])):
                        joueur[ord(bateau1[0])-65][i]=cle
                    case=True
                elif int(bateau1[1])+1-int(bateau2[1])==valeur:
                    for i in range(int(bateau2[1])-1,int(bateau1[1])):
                        joueur[ord(bateau1[0])-65][i]=cle
                    case=True
            elif bateau1[1]==bateau2[1]:
                if ord(bateau1[0])-65-(ord(bateau2[0])-64)==valeur or ord(bateau1[0])-65-(ord(bateau2[0])-64)==-valeur:
                    for i in range(ord(bateau1[0])-65, ord(bateau2[0])-64):
                        joueur[i][int(bateau1[1])-1]=cle
                    case=True
            
            if not case:
                inter.interface.affichage(selfIn, joueur, joueur1Tir, joueur2Tir, "Réessayez", False)
                time.sleep(2)
            

    inter.interface.affichage(selfIn, joueur, joueur1Tir, joueur2Tir, "Veuilllez patienter...", False)
                
def initialisation_client (self, joueur):
    
    for cle,valeur in bateaux2.items():
        bateau1, bateau2 = [], []
        while bateau1==[]:
            bateau1 = serv.serveur.input_serveur(self, joueur, joueur1Tir, joueur2Tir, "Entrez la première extrémité du {} ({} cases)".format(cle, valeur), True)
        while bateau2==[]:
            bateau2 = serv.serveur.input_serveur(self, joueur, joueur1Tir, joueur2Tir, "Entrez la dernière extrémité du {} ({} cases)".format(cle, valeur), True)
        if bateau1[0]==bateau2[0]:
            for i in range(int(bateau1[1])-1,int(bateau2[1])):
                joueur[ord(bateau1[0])-65][i]=cle
        else:
            for i in range(ord(bateau1[0])-65, ord(bateau2[0])-64):
                joueur[i][int(bateau1[1])-1]=cle
    serv.serveur.input_serveur(self, joueur, joueur2Tir, joueur1Tir, "Veuilllez patienter...", False)
                
   
   
   
def tir(joueurTir, case, bataille):
    if bataille!=None:
        joueurTir[ord(case[0])-65][int(case[1])-1]=2
    else:
        joueurTir[ord(case[0])-65][int(case[1])-1]=1
        

def bataille(joueur, bateaux, case):
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
    if bateaux1['porte-avion']==0 and bateaux1['croiseur']==0 and bateaux1['sous-marin']==0 and bateaux1['contre-torpilleur']==0 and bateaux1['torpilleur']==0:
        return 'Joueur 1'
    elif bateaux2['porte-avion']==0 and bateaux2['croiseur']==0 and bateaux2['sous-marin']==0 and bateaux2['contre-torpilleur']==0 and bateaux2['torpilleur']==0:
        return 'Joueur 2'
    else:
        return False
        



  
selfIn=inter.interface()
mode=inter.interface.menu(selfIn)

if mode==1:

    initialisation(joueur1)
    time.sleep(3)
    inter.interface.affichage(selfIn, [[0]], [[0]], [[0]], "Passez l'odinateur au Joueur 2", False)
    time.sleep(5)
    initialisation(joueur2)
    time.sleep(3)
    
    inter.interface.affichage(selfIn, [[0]], [[0]], [[0]], "Passez l'odinateur au Joueur 1", False)
    time.sleep(5)
    
    while perdu()==False:
        navale=""
        print(perdu())
        while navale!=None and perdu()==False:
            case = inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, "Joueur 1, cliquez sur une case", True)
            navale=bataille(joueur2, bateaux2, case)
            print(navale)
            print( bateaux2['porte-avion'])
            tir(joueur1Tir, case, navale)
            inter.interface.son(selfIn, navale)
            inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, navale, False)
            time.sleep(3)
        
        navale=""
        inter.interface.affichage(selfIn, [[0]], [[0]], [[0]], "Passez l'odinateur au Joueur 2", False)
        time.sleep(5)
        while navale!=None and perdu()==False:
            case = inter.interface.affichage(selfIn, joueur2, joueur2Tir, joueur1Tir, "Joueur 2, cliquez sur une case", True)
            navale=bataille(joueur1, bateaux1, case)
            tir(joueur2Tir, case, navale)
            inter.interface.son(selfIn, navale)
            inter.interface.affichage(selfIn, joueur2, joueur2Tir, joueur1Tir, navale, False)
            time.sleep(3)
            
        inter.interface.affichage(selfIn, [[0]], [[0]], [[0]], "Passez l'odinateur au Joueur 1", False)
        time.sleep(5)
            
    print(perdu(), "a perdu !")
    inter.interface.affichage(selfIn, [[0]], [[0]], [[0]], perdu() + ' a perdu !', False)
    time.sleep(5)
    
    inter.interface.stop()
            
elif mode==2:
    
    adresse=inter.interface.ipAdresse(selfIn)
    inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, "Veuillez patienter...", False)
    self=serv.serveur(adresse)
    
    initialisation(joueur1)
    initialisation_client(self, joueur2)
    
    while perdu()==False:
        navale=""
        print(perdu())
        while navale!=None and perdu()==False:    
            case = inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, "Cliquez sur une case :", True)
            
            navale=bataille(joueur2, bateaux2, case)
            tir(joueur1Tir, case, navale)
            
            inter.interface.son(selfIn, navale)
            inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, navale, False)
            serv.serveur.input_serveur(self, joueur2, joueur2Tir, joueur1Tir, navale, False)
            time.sleep(2)
            serv.serveur.input_serveur(self, joueur2, joueur2Tir, joueur1Tir, "Veuillez patienter...", False)
            
        inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, "Veuillez patienter...", False)
        navale=""
        while navale!=None and perdu()==False:
            case2=[]
            while case2==[]:
                case2 = serv.serveur.input_serveur(self, joueur2, joueur2Tir, joueur1Tir, "Cliquez sur une case :", True)
        
            navale=bataille(joueur1, bateaux1, case2)
            tir(joueur2Tir, case2, navale)
            serv.serveur.input_serveur(self, joueur2, joueur2Tir, joueur1Tir, navale, False)
            inter.interface.son(selfIn, navale)
            inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, navale, False)
            time.sleep(2)
            inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, "Veuillez patienter...", False)
        
        serv.serveur.input_serveur(self, joueur2, joueur2Tir, joueur1Tir, "Veuillez patienter...", False)
    
    if perdu()=='Joueur 1':
        perdu1="Vous avez perdu !"
        perdu2="Vous avez gagné !"
    else:
        perdu1="Vous avez gagné !"
        perdu2="Vous avez perdu !"
        
    serv.serveur.input_serveur(self, joueur2, joueur2Tir, joueur1Tir, perdu2, False)
    inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, perdu1, False)
    time.sleep(5)
    print(perdu(), 'a perdu !')
    inter.interface.stop()
    serv.serveur.stop(self)
    
elif mode==3:
    
    adresse=inter.interface.ipAdresse(selfIn)
    inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, "Veillez patienter...", False)
    self=serv.client(adresse)
    
    perdu=False
    while not perdu:
        perdu=serv.client.input_client(self, selfIn)
    time.sleep(5)
    
    print(perdu, 'a perdu !')
    inter.interface.stop()
    serv.client.stop(self)
    
elif mode==4:
    print("mode contre ordinateur")
    
        
   
