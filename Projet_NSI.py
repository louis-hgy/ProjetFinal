def initialisation ():
    bateaux=['porte-avion', 'croiseur', 'contre-torpilleur', 'sous-marin', 'torpilleur']
    joueur1=[]
    for i in range(10):
        joueur1.append([0 for x in range(10)])
    for i in bateaux:
        bateaux1 = list(input("Entrez la première extrémité du {}".format(i)))
        bateaux2 = list(input("Entrez la dernière extrémité du {}".format(i)))
        if bateaux1[0]==bateaux2[0]:
            for i in range(int(bateaux1[1]),int(bateaux2[1])+1):
                joueur1[ord(bateaux1[0])-65][i]=1
        else:
            for i in range(ord(bateaux1[0])-65, ord(bateaux2[0])-64):
                joueur1[i][int(bateaux1[1])-1]=1
    joueur2=[]
    for i in range(10):
        joueur2.append([0 for x in range(10)])
    for i in bateaux:
        bateaux1 = list(input("Entrez la première extrémité du {}".format(i)))
        bateaux2 = list(input("Entrez la dernière extrémité du {}".format(i)))
        if bateaux1[0]==bateaux2[0]:
            for i in range(int(bateaux1[1]),int(bateaux2[1])+1):
                joueur2[ord(bateaux1[0])-65][i]=1
        else:
            for i in range(ord(bateaux1[0])-65, ord(bateaux2[0])-64):
                joueur2[i][int(bateaux1[1])-1]=1

            

            