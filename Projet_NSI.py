#coding:utf-8
import client_serveur as serv
import interface as inter
import time
from random import randint

caseordi=[['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10'],['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10'],['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10'],['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10'],['E1','E2','E3','E4','E5','E6','E7','E8','E9','E10'],['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10'],['G1','G2','G3','G4','G5','G6','G7','G8','G9','G10'],['H1','H2','H3','H4','H5','H6','H7','H8','H9','H10'],['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10'],['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10']]
verif=[]
ordinateur = ([[0 for x in range(10)] for x in range(10)])
ordinateurTir = ([[0 for x in range(10)] for x in range(10)])

                   

joueur1=([[0 for x in range(10)]for x in range(10)])
joueur2=([[0 for x in range(10)]for x in range(10)])
joueur1Tir=([[0 for x in range(10)]for x in range(10)])
joueur2Tir=([[0 for x in range(10)]for x in range(10)])
bateaux1={'porte-avion': 5, 'croiseur': 4, 'sous-marin': 3, 'contre-torpilleur': 3, 'torpilleur': 2}
bateaux2={'porte-avion': 5, 'croiseur': 4, 'sous-marin': 3, 'contre-torpilleur': 3, 'torpilleur': 2}


def initialisation (joueur):
    for cle,valeur in bateaux2.items():
        case=False
        while not case:
            case=True
            bateau1 = inter.interface.affichage(selfIn, joueur, joueur1Tir, joueur2Tir, "Cliquez sur la première extrémité du {} ({} cases)".format(cle, valeur), True)
            bateau2 = inter.interface.affichage(selfIn, joueur, joueur1Tir, joueur2Tir, "Cliquez sur la dernière extrémité du {} ({} cases)".format(cle, valeur), True)
            if bateau1[0]==bateau2[0]:
                if int(bateau1[1])-1-int(bateau2[1])==-valeur:
                    for i in range(int(bateau1[1])-1,int(bateau2[1])):
                        if joueur[ord(bateau1[0])-65][i]!=0:
                            case=False                        
                    if case==True:    
                        for i in range(int(bateau1[1])-1,int(bateau2[1])):
                            joueur[ord(bateau1[0])-65][i]=cle
                        
                elif int(bateau1[1])+1-int(bateau2[1])==valeur:
                    for i in range(int(bateau2[1])-1,int(bateau1[1])):
                        if joueur[ord(bateau1[0])-65][i]!=0:
                            case=False                        
                    if case==True:    
                        for i in range(int(bateau2[1])-1,int(bateau1[1])):
                            joueur[ord(bateau1[0])-65][i]=cle
                else:
                    case=False            
                    
            elif bateau1[1]==bateau2[1]:
                if ord(bateau1[0])-65-(ord(bateau2[0])-64)==-valeur:
                    for i in range(ord(bateau1[0])-65, ord(bateau2[0])-64):
                        if joueur[i][int(bateau1[1])-1]!=0:
                            case=False                        
                    if case==True:    
                        for i in range(ord(bateau1[0])-65, ord(bateau2[0])-64):
                            joueur[i][int(bateau1[1])-1]=cle
                        
                    
                elif ord(bateau1[0])-63-(ord(bateau2[0])-64)==valeur:
                    for i in range(ord(bateau2[0])-65, ord(bateau1[0])-64):
                        if joueur[i][int(bateau1[1])-1]!=0:
                            case=False                        
                    if case==True:    
                        for i in range(ord(bateau2[0])-65, ord(bateau1[0])-64):
                            joueur[i][int(bateau1[1])-1]=cle
                else:
                    case=False   
            else:
                case=False
            
            if not case:
                inter.interface.affichage(selfIn, joueur, joueur1Tir, joueur2Tir, "Réessayez", False)
                time.sleep(2)

    inter.interface.affichage(selfIn, joueur, joueur1Tir, joueur2Tir, "Veuilllez patienter...", False)
       
       
def initialisation_client (self, joueur):
    for cle,valeur in bateaux2.items():
        case=False
        while not case:
            case=True
            bateau1, bateau2 = [], []
            while bateau1==[]:
                bateau1 = serv.serveur.input_serveur(self, joueur, joueur1Tir, joueur2Tir, "Entrez la première extrémité du {} ({} cases)".format(cle, valeur), True)
            while bateau2==[]:
                bateau2 = serv.serveur.input_serveur(self, joueur, joueur1Tir, joueur2Tir, "Entrez la dernière extrémité du {} ({} cases)".format(cle, valeur), True)
            if bateau1[0]==bateau2[0]:
                if int(bateau1[1])-1-int(bateau2[1])==-valeur:
                    for i in range(int(bateau1[1])-1,int(bateau2[1])):
                        if joueur[ord(bateau1[0])-65][i]!=0:
                            case=False                        
                    if case==True:    
                        for i in range(int(bateau1[1])-1,int(bateau2[1])):
                            joueur[ord(bateau1[0])-65][i]=cle
                        
                elif int(bateau1[1])+1-int(bateau2[1])==valeur:
                    for i in range(int(bateau2[1])-1,int(bateau1[1])):
                        if joueur[ord(bateau1[0])-65][i]!=0:
                            case=False                        
                    if case==True:    
                        for i in range(int(bateau2[1])-1,int(bateau1[1])):
                            joueur[ord(bateau1[0])-65][i]=cle
                else:
                    case=False              
                    
            elif bateau1[1]==bateau2[1]:
                if ord(bateau1[0])-65-(ord(bateau2[0])-64)==-valeur:
                    for i in range(ord(bateau1[0])-65, ord(bateau2[0])-64):
                        if joueur[i][int(bateau1[1])-1]!=0:
                            case=False                        
                    if case==True:    
                        for i in range(ord(bateau1[0])-65, ord(bateau2[0])-64):
                            joueur[i][int(bateau1[1])-1]=cle
                        
                    
                elif ord(bateau1[0])-63-(ord(bateau2[0])-64)==valeur:
                    for i in range(ord(bateau2[0])-65, ord(bateau1[0])-64):
                        if joueur[i][int(bateau1[1])-1]!=0:
                            case=False                        
                    if case==True:    
                        for i in range(ord(bateau2[0])-65, ord(bateau1[0])-64):
                            joueur[i][int(bateau1[1])-1]=cle
                else:
                    case=False    
            else:
                case=False
           
            if not case:
                serv.serveur.input_serveur(self, joueur, joueur2Tir, joueur1Tir, "Réessayez", False)
            time.sleep(2)
                   
    serv.serveur.input_serveur(self, joueur, joueur2Tir, joueur1Tir, "Veuilllez patienter...", False)
            
            
def initialisation_ordinateur():
    for cle, valeur in bateaux2.items():
        echec=True
        print('test début')
        while echec==True:
            echec=False
            nb1=randint(0,9)
            nb2=randint(0,9)
            while nb1>=valeur and nb2>=valeur:
                nb1=randint(0,9)
                nb2=randint(0,9)
            bateau1=list(caseordi[nb1][nb2])

            if nb1>=valeur:
                bateau2=list(caseordi[nb1][nb2+valeur-1])
                for i in range(int(bateau1[1]) - 1, int(bateau2[1])):
                    print('test1')
                    if ordinateur[ord(bateau1[0]) - 65][i] !=0:
                        print('déjà pris')
                        echec=True
                               
                if echec==False:    
                    for i in range(int(bateau1[1]) - 1, int(bateau2[1])):
                        ordinateur[ord(bateau1[0]) - 65][i] = cle
                
            else:
                bateau2=list(caseordi[nb1+valeur-1][nb2])
                for i in range(ord(bateau1[0]) - 65, ord(bateau2[0]) - 64):
                    print('test 2')
                    if ordinateur[i][int(bateau1[1])-1] !=0:
                        print('déjà pris')
                        echec=True       
                if echec==False:        
                    for i in range(ord(bateau1[0]) - 65, ord(bateau2[0]) - 64):
                        ordinateur[i][int(bateau1[1])-1] = cle
   
   
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
        


#programme principal
  
selfIn=inter.interface()
mode=inter.interface.menu(selfIn)

if mode==1:

    initialisation(joueur1)
    time.sleep(3)
    inter.interface.affichage(selfIn, [[0]], [[0]], [[0]], "Passez l'ordinateur au Joueur 2", False)
    time.sleep(5)
    initialisation(joueur2)
    time.sleep(3)
    
    inter.interface.affichage(selfIn, [[0]], [[0]], [[0]], "Passez l'ordinateur au Joueur 1", False)
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
        inter.interface.affichage(selfIn, [[0]], [[0]], [[0]], "Passez l'ordinateur au Joueur 2", False)
        time.sleep(5)
        while navale!=None and perdu()==False:
            case = inter.interface.affichage(selfIn, joueur2, joueur2Tir, joueur1Tir, "Joueur 2, cliquez sur une case", True)
            navale=bataille(joueur1, bateaux1, case)
            tir(joueur2Tir, case, navale)
            inter.interface.son(selfIn, navale)
            inter.interface.affichage(selfIn, joueur2, joueur2Tir, joueur1Tir, navale, False)
            time.sleep(3)
            
        inter.interface.affichage(selfIn, [[0]], [[0]], [[0]], "Passez l'ordinateur au Joueur 1", False)
        time.sleep(5)
            
    print(perdu(), "a perdu !")
    inter.interface.sonPerdu(selfIn, perdu())
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
    inter.interface.sonPerdu(selfIn, perdu1)
    inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, perdu1, False)
    time.sleep(5)
    inter.interface.stop()
    serv.serveur.stop(self)
    
elif mode==3:
    
    adresse=inter.interface.ipAdresse(selfIn)
    inter.interface.affichage(selfIn, joueur1, joueur1Tir, joueur2Tir, "Veuillez patienter...", False)
    self=serv.client(adresse)
    
    perdu=False
    while not perdu:
        perdu=serv.client.input_client(self, selfIn)
    inter.interface.sonPerdu(selfIn, perdu)
    time.sleep(5)
    
    print(perdu, 'a perdu !')
    inter.interface.stop()
    serv.client.stop(self)
    
elif mode==4:
    initialisation_ordinateur()
    initialisation(joueur1)
    

    while perdu()==False:
        navale=""
        while navale!=None and perdu()==False:
            case = inter.interface.affichage(selfIn, joueur1, joueur1Tir, ordinateurTir, "Cliquez sur une case :", True)
            navale=bataille(ordinateur, bateaux2, case)
            print(navale)
            tir(joueur1Tir, case, navale)
            inter.interface.son(selfIn, navale)
            inter.interface.affichage(selfIn, joueur1, joueur1Tir, ordinateurTir, navale, False)
            time.sleep(3)
        
        navale=""
        inter.interface.affichage(selfIn, joueur1, joueur1Tir, ordinateurTir, "Veuillez patienter...", False)
        while navale!=None and perdu()==False:
            echec=True
            while echec:
                echec=False
                nb1case=randint(0,9)
                nb2case=randint(0,9)
                if ordinateurTir[nb1case][nb2case]!=0:
                    print('utilisé')
                    case=[]
                    echec=True
                else:  
                    case=list(caseordi[nb1case][nb2case])
                    print(case)
                    navale=bataille(joueur1, bateaux1, case)
                    tir(ordinateurTir, case, navale)
                    inter.interface.son(selfIn, navale)
                    inter.interface.affichage(selfIn, joueur1, joueur1Tir, ordinateurTir, navale, False)
                    time.sleep(2)
                
    
    if perdu()=='Joueur 1':
        perdu1="Vous avez perdu !"
    else:
        perdu1="Vous avez gagné !"
        
    inter.interface.sonPerdu(selfIn, perdu1)
    inter.interface.affichage(selfIn, [[0]], [[0]], [[0]], perdu1, False)
    time.sleep(5)
    
    inter.interface.stop()        
   
