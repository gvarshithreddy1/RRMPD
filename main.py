import pygame
import random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

positions = [(370,450,180),(542.13485,322.6269,108),(473.2437,122.5526,36),(199.80665639212296,328.6022678022882,252),(261.6732958326313,126.24560819148729,324)]
positions = random.sample(positions,5)


bg = (0,0,0)
cpt = (370,270,0)
pos1 = positions[0]
pos2 = positions[1]
pos3 = positions[2]
pos4 =positions[3]
pos5 = positions[4]

pygame.display.set_caption("Raju Rani Manthri Police Donga")
icon = pygame.image.load("tower.png")
pygame.display.set_icon(icon)
running = True



def player(playerImg,playerX,playerY):
    screen.blit(playerImg,(playerX,playerY))

class Player():
    radius = 180
    def __init__(self,img,p):
        self.playerX = p[0]
        self.playerY = p[1]
        self.playerImg = img
        self.angle = p[2]
    
    

    def pRot(self,pos):
        if self.angle != pos[2]:
            p1_vec = pygame.math.Vector2(0, -self.radius).rotate(self.angle)
            pt_x, pt_y = cpt[0] + p1_vec.x, cpt[1] + p1_vec.y
            self.playerX = pt_x
            self.playerY = pt_y
            
            
            self.angle += 1  
            # print(self.angle)   
            if self.angle >= 360:
                self.angle = 0
            if self.angle ==324:
                print(pt_x,pt_y)
    def pShow(self):
        player(self.playerImg,self.playerX,self.playerY)



forest_image = pygame.image.load("forest.png")
forest = pygame.transform.scale(forest_image,(800,600))        
tree = Player(forest,bg)
campfire = Player(pygame.image.load("bonfire.png"),cpt)
king = Player(pygame.image.load("king.png"),pos1)
queen = Player(pygame.image.load("queen.png"),pos2)
minister = Player(pygame.image.load("saint-patrick.png"),pos3)
police = Player(pygame.image.load("police.png"),pos4)
thief = Player(pygame.image.load("thief.png"),pos5)



while running:
    clock.tick(60)
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    queen.pRot(pos1)

    king.pShow()
    campfire.pShow()
    queen.pShow()
    minister.pShow()
    police.pShow()
    thief.pShow()
    pygame.display.update()