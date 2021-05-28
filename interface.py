#coding:utf-8
import pygame, time

class interface():
    
    def __init__(self):
        pygame.init()
        
        self.launched=True

        self.black = (0,0,0)
        self.white = (255, 255, 255)
        self.blue = (37, 191, 244)
        self.red = (244, 39, 39)
        self.grey = (178,190,181)

        self.font = pygame.font.SysFont("arial", 25)
        self.fontTitre = pygame.font.SysFont("arialbd", 50)
        
        self.fond = pygame.image.load("img/BattleShip.png")
        
        self.tir_son = pygame.mixer.Sound("son/Tir.mp3")
        self.coule_son = pygame.mixer.Sound("son/Coule.wav")
        self.touche_son = pygame.mixer.Sound("son/Touche.mp3")
        self.eau_son = pygame.mixer.Sound("son/Eau.wav")
        self.perdu_son = pygame.mixer.Sound("son/Perdu.wav")
        self.gagne_son = pygame.mixer.Sound("son/Gagne.wav")

        pygame.display.set_caption("Bataille Navale")
        
        self.window_surface = pygame.display.set_mode((1366, 768), pygame.RESIZABLE)
        self.window_surface.fill(self.white)
        
        self.clock = pygame.time.Clock()
        
        print('init')    

    def menu(self):
        self.window_surface.blit(self.fond, (0,0))
        
        mode1 = pygame.Rect(200, 100, 458, 150)
        mode2 = pygame.Rect(200, 350, 458, 150)
        mode3 = pygame.Rect(708, 350, 458, 150)
        mode4 = pygame.Rect(708, 100, 458, 150)

        pygame.draw.rect(self.window_surface, self.black, mode1, 5)
        pygame.draw.rect(self.window_surface, self.black, mode2, 5)
        pygame.draw.rect(self.window_surface, self.black, mode3, 5)
        pygame.draw.rect(self.window_surface, self.black, mode4, 5)

        textMode1 = self.fontTitre.render("1. Mode 1 ordinateur", True, self.black)
        textMode2 = self.fontTitre.render("3. Mode réseau (serveur)", True, self.black)
        textMode3 = self.fontTitre.render("4. Mode réseau (client)", True, self.black)
        textMode4 = self.fontTitre.render("2. Mode contre ordinateur", True, self.black)

        self.window_surface.blit(textMode1, (240, 150))
        self.window_surface.blit(textMode2, (240, 400))
        self.window_surface.blit(textMode3, (748, 400))
        self.window_surface.blit(textMode4, (728, 150))

        pygame.display.flip()
        

        launched = True
        while launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mode1.collidepoint(event.pos):
                        print('1')
                        return 1
                    elif mode2.collidepoint(event.pos):
                        print('2')
                        return 2
                    elif mode3.collidepoint(event.pos):
                        print('3')
                        return 3
                    elif mode4.collidepoint(event.pos):
                        print('4')
                        return 4
            self.clock.tick(30)
        
        pygame.quit()
        
    def ipAdresse(self):
        text = pygame.Rect(383, 200, 600, 100)
        ip = pygame.Rect(533, 350, 300, 50)
        adresse=''
        
        launched=True
        while launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(adresse)
                        return adresse
                    elif event.key == pygame.K_BACKSPACE:
                        adresse = adresse[:-1]
                    else:
                        adresse += event.unicode
                            
            self.window_surface.fill(self.white)
            
            pygame.draw.rect(self.window_surface, self.black, ip, 5)
            pygame.draw.rect(self.window_surface, self.black, text, 6)
            
            self.window_surface.blit(self.font.render(adresse, True, self.black), (553, 360))
            self.window_surface.blit(self.fontTitre.render("Entrez adresse IP du serveur :", True, self.black), (443, 230))
            
            
            pygame.display.flip()
            self.clock.tick(30)
            
        pygame.quit()    
            
    def affichage(self, joueur, joueurTir, joueurTir_2, message, input):
        if message==None:
            message="Dans l'eau !"
    
        self.window_surface.fill(self.white)
        
        x=[170, 220, 270, 320, 370, 420, 470, 520, 570, 620]
        y=[60, 110, 160, 210, 260, 310, 360, 410, 460, 510]
        
        grilleX = {'A': pygame.Rect(610, 170, 500, 50), 'B': pygame.Rect(610, 220, 500, 50), 'C': pygame.Rect(610, 270, 500, 50), 'D': pygame.Rect(610, 320, 500, 50), 'E': pygame.Rect(610, 370, 500, 50), 'F': pygame.Rect(610, 420, 500, 50), 'G': pygame.Rect(610, 470, 500, 50), 'H': pygame.Rect(610, 520, 500, 50), 'I': pygame.Rect(610, 570, 500, 50), 'J': pygame.Rect(610, 620, 500, 50)}
        
        grilleY = {'1': pygame.Rect(610, 170, 50, 500), '2': pygame.Rect(660, 170, 50, 500), '3': pygame.Rect(710, 170, 50, 500), '4': pygame.Rect(760, 170, 50, 500), '5': pygame.Rect(810, 170, 50, 500), '6': pygame.Rect(860, 170, 50, 500), '7': pygame.Rect(910, 170, 50, 500), '8': pygame.Rect(960, 170, 50, 500), '9': pygame.Rect(1010, 170, 50, 500), '10': pygame.Rect(1060, 170, 50, 500)}



        messageRect = pygame.Rect(10, 10, 1346, 100)

        pygame.draw.rect(self.window_surface, self.black, messageRect, 5)
        
        pygame.draw.rect(self.window_surface, self.black, grilleX['A'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleX['B'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleX['C'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleX['D'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleX['E'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleX['F'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleX['G'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleX['H'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleX['I'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleX['J'], 5)
        
        pygame.draw.rect(self.window_surface, self.black, grilleY['1'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleY['2'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleY['3'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleY['4'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleY['5'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleY['6'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleY['7'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleY['8'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleY['9'], 5)
        pygame.draw.rect(self.window_surface, self.black, grilleY['10'], 5)
        

        self.window_surface.blit(self.font.render("A", True, self.black), (10, 175))
        self.window_surface.blit(self.font.render("B", True, self.black), (10, 225))
        self.window_surface.blit(self.font.render("C", True, self.black), (10, 275))
        self.window_surface.blit(self.font.render("D", True, self.black), (10, 325))
        self.window_surface.blit(self.font.render("E", True, self.black), (10, 375))
        self.window_surface.blit(self.font.render("F", True, self.black), (10, 425))
        self.window_surface.blit(self.font.render("G", True, self.black), (10, 475))
        self.window_surface.blit(self.font.render("H", True, self.black), (10, 525))
        self.window_surface.blit(self.font.render("I", True, self.black), (10, 575))
        self.window_surface.blit(self.font.render("J", True, self.black), (10, 625))
        
        self.window_surface.blit(self.font.render("1", True, self.black), (65, 120))
        self.window_surface.blit(self.font.render("2", True, self.black), (115, 120))
        self.window_surface.blit(self.font.render("3", True, self.black), (165, 120))
        self.window_surface.blit(self.font.render("4", True, self.black), (215, 120))
        self.window_surface.blit(self.font.render("5", True, self.black), (265, 120))
        self.window_surface.blit(self.font.render("6", True, self.black), (315, 120))
        self.window_surface.blit(self.font.render("7", True, self.black), (365, 120))
        self.window_surface.blit(self.font.render("8", True, self.black), (415, 120))
        self.window_surface.blit(self.font.render("9", True, self.black), (465, 120))
        self.window_surface.blit(self.font.render("10", True, self.black), (515, 120))
        
        
        
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(60, 170, 500, 50), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(60, 220, 500, 50), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(60, 270, 500, 50), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(60, 320, 500, 50), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(60, 370, 500, 50), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(60, 420, 500, 50), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(60, 470, 500, 50), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(60, 520, 500, 50), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(60, 570, 500, 50), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(60, 620, 500, 50), 5)
               
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(60, 170, 50, 500), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(110, 170, 50, 500), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(160, 170, 50, 500), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(210, 170, 50, 500), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(260, 170, 50, 500), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(310, 170, 50, 500), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(360, 170, 50, 500), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(410, 170, 50, 500), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(460, 170, 50, 500), 5)
        pygame.draw.rect(self.window_surface, self.black, pygame.Rect(510, 170, 50, 500), 5)
        
        
        self.window_surface.blit(self.font.render(message, True, self.black), (50, 50))
        
        for i in range(len(joueur)):
            for j in range(len(joueur)):
                if joueur[i][j]!=0:
                    pygame.draw.rect(self.window_surface, self.grey, pygame.Rect(y[j], x[i], 50, 50))
                if joueurTir[i][j]==1:
                    pygame.draw.rect(self.window_surface, self.blue, pygame.Rect(y[j]+550, x[i], 50, 50))
                elif joueurTir[i][j]==2:
                    pygame.draw.rect(self.window_surface, self.red, pygame.Rect(y[j]+550, x[i], 50, 50))
                if joueurTir_2[i][j]==2:
                    pygame.draw.rect(self.window_surface, self.red, pygame.Rect(y[j], x[i], 50, 50))

        pygame.display.flip()
        
        case=[]
        echec=True
        while self.launched and input and echec:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.launched = False
                    interface.stop()
                
                elif input:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for cle,valeur in grilleX.items():
                            if valeur.collidepoint(event.pos):
                                case.append(cle)
                        for cle,valeur in grilleY.items():
                            if valeur.collidepoint(event.pos):
                                case.append(cle)
                                print(case)
                                echec=False
                                if joueurTir[ord(case[0])-65][int(case[1])-1]!=0:
                                    print('utilisé')
                                    case=[]
                                    echec=True
                                else:
                                    return case  
            self.clock.tick(30)
        nb=0     
        while self.launched and not input and nb<15:
            nb+=1
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.launched = False
                    interface.stop()
            self.clock.tick(30)
            
            
    def son(self, son):
        if son==None:
            self.tir_son.play()
            time.sleep(self.tir_son.get_length())
            self.eau_son.play()
        elif son=='Touché':
            self.tir_son.play()
            time.sleep(self.tir_son.get_length())
            self.touche_son.play()
        elif son=='Coulé':
            self.tir_son.play()
            time.sleep(self.tir_son.get_length())
            self.touche_son.play()
            self.coule_son.play()
            
    def sonPerdu(self, son):
        if son=="Vous avez perdu !":
            self.perdu_son.play()
        else:
            self.gagne_son.play()
            
    def stop():
        pygame.display.quit()
        pygame.quit()    
        