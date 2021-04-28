joueur1=([[0 for x in range(10)]for x in range(10)])
joueur2=([[0 for x in range(10)]for x in range(10)])
bateaux={'porte-avion': 5, 'croiseur': 4, 'sous-marin': 3, 'sous-marin': 3, 'torpilleur': 2}

def initialisation ():
    
    for cle,valeur in bateaux.items():
        bateaux1 = list(input("Entrez la première extrémité du {} ({} cases)".format(cle, valeur)))
        bateaux2 = list(input("Entrez la dernière extrémité du {} ({} cases)".format(cle, valeur)))
        if bateaux1[0]==bateaux2[0]:
            for i in range(int(bateaux1[1])-1,int(bateaux2[1])):
                joueur1[ord(bateaux1[0])-65][i]=cle
        else:
            for i in range(ord(bateaux1[0])-65, ord(bateaux2[0])-64):
                joueur1[i][int(bateaux1[1])-1]=cle
                
    for cle, valeur in bateaux.items():
        bateaux1 = list(input("Entrez la première extrémité du {} ({} cases)".format(cle, valeur)))
        bateaux2 = list(input("Entrez la dernière extrémité du {} ({} cases)".format(cle, valeur)))
        if bateaux1[0]==bateaux2[0]:
            for i in range(int(bateaux1[1])-1,int(bateaux2[1])):
                joueur2[ord(bateaux1[0])-65][i]=cle
        else:
            for i in range(ord(bateaux1[0])-65, ord(bateaux2[0])-64):
                joueur2[i][int(bateaux1[1])-1]=cle

#initialisation()
#print(joueur1)
#joueur1[0][0]='sous-marin'
#joueur1[1][1]='torpilleur'



def bataille(joueur, case):
    list(case)
    if joueur[ord(case[0])-65][int(case[1])] != 0 :
        if bateaux[joueur[ord(case[0])-65][int(case[1])]]-1 == 0:
            return 'Coulé'
        else:
            bateaux[joueur[ord(case[0])-65][int(case[1])]] -= 1
            return 'Touché'
    else:
        return None

    
#bataille(joueur1, 'A1')
#bataille(joueur1, 'B2')
#bataille(joueur1, 'C3')

