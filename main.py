import pygame
import random
import sys
import math

players = [{"name":"Varshith",
            "role":None,
            "pid":0},
            
            {"name":"Venu",
             "role":None,
             "pid":1},
             
            {"name":"Bhargav",
            "role":None,
            "pid":2},

            {"name":"Abhilash",
            "role":None,
            "pid":3},

            {"name":"Nagendra",
            "role":None,
            "pid":4}]




pygame.init()
textfont = pygame.font.SysFont("Comic Sans MS",14)
warnFont = pygame.font.SysFont("Comic Sans MS",30)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

positions = [(370,450,180),(542.13485,322.6269,108),(473.2437,122.5526,36),(199.80665639212296,328.6022678022882,252),(261.6732958326313,126.24560819148729,324)]
positions = random.sample(positions,5)

class Player():
    radius = 180
    def __init__(self,p):
        self.playerX = p[0]
        self.playerY = p[1]        
        self.angle = p[2]
        self.p = p
    
    

    
    def pShow(self):
        player(self.playerImg,self.playerX,self.playerY)
MOVE_SPEED = 4
class Character(pygame.sprite.Sprite,Player):
    
    
    def __init__(self, imgDir,p,role):
        
        super().__init__()
        Player.__init__(self,p)
        self.image = pygame.image.load(imgDir)
        self.name = role
        # self.pos = self.playerX,self.playerY
        self.rect = self.image.get_rect()  
        self.rect.center = self.playerX,self.playerY  
        self.target_position = None   
        self.initial_position = p[0],p[1]
        

    def move_to_position(self, target_position):
        self.target_position = target_position
        
    
    def update(self):
        if self.target_position:
            dx = self.target_position[0] - self.playerX
            dy = self.target_position[1] - self.playerY
            distance = math.sqrt(dx**2 + dy**2)

            if distance > MOVE_SPEED:
                angle = math.atan2(dy, dx)
                self.playerX += MOVE_SPEED * math.cos(angle)
                self.playerY += MOVE_SPEED * math.sin(angle)
                self.keep_track()
            else:
                self.playerX, self.playerY = self.target_position
                self.rect.center = self.target_position
                self.target_position = None

    def keep_track(self):
        self.rect.center = self.playerX,self.playerY
        
        



class Cursor(pygame.sprite.Sprite):
    
    def __init__(self,imgDir):
        super().__init__()
        self.image = pygame.image.load(imgDir)
        self.rect = self.image.get_rect()
    
            
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        # events = pygame.event.get()
        
    def clicked(self,characters,events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for character in characters:
                    if character.rect.collidepoint(pos) and pygame.sprite.spritecollide(cursor,characters,False):
                        # print(character.name)
                        return(character.name)

                # get a list of all sprites that are under the mouse cursor
                
            


bg = (0,0,0)
cpt = (370,270,0)
pos1 = []
pos2 = []
pos3 = []
pos4 = []
pos5 = []
def update_positions(positions):
    global pos1,pos2,pos3,pos4,pos5
    pos1 = positions[0]
    pos2 = positions[1]
    pos3 = positions[2]
    pos4 =positions[3]
    pos5 = positions[4]
update_positions(positions)

pygame.display.set_caption("Raju Rani Manthri Police Donga")
icon = pygame.image.load("tower.png")
pygame.display.set_icon(icon)

running = True



def player(playerImg,playerX,playerY):
    screen.blit(playerImg,(playerX,playerY))



cursor_group = pygame.sprite.Group()
cursor = Cursor("crosshair.png")
cursor_group.add(cursor)

pygame.mouse.set_visible(False)


campfire = Character("bonfire.png",cpt,"campfire")
king = Character("king.png",pos1,"king")
queen = Character("queen.png",pos2,"queen")
minister = Character("saint-patrick.png",pos3,"minister")
police = Character("police.png",pos4,"police")
thief = Character("thief.png",pos5,"thief")

# print(thief.target_position)


characters = pygame.sprite.Group()
char_list = king,queen,minister,police,thief
char_list = random.sample(char_list,5)
characters.add(campfire,king,queen,minister,police,thief)

for i in range(5):
    players[i]["role"] = char_list[i].name


#player order
def player_order_sort(players):
    global order
    order = [-1,-1,-1,-1,-1]
    for pl in players:
        match pl["role"]:
            case "king":
                order[0] = pl["pid"]
            case  "queen":
                order[1] = pl["pid"]
            case  "minister":
                order[2] = pl["pid"]
            case  "police":
                order[3] = pl["pid"]
            case  "thief":
                order[4] = pl["pid"]
    return(order)




def kings_guessed(result):
    guessed = False
    if result == "queen":
        guessed = True
    if guessed:
        
        print("guessed")
        return(True)
        
def get_player(players,pid=-1,role=-1,name=-1):
    if role == -1:
        for player in players:
            if player['pid'] == pid:
                return(player['name'],player["pid"],player["role"])
    
    if pid == -1:
        for player in players:
            if player["role"] == role:
                return(player["name"],player["pid"],player["role"])
    
    if pid == -1:
        for player in players:
            if player["name"] == name:
                return(player["name"],player["pid"],player["role"])
    

def guessed(role,result):
    answer = ""
    match role:
        case "king":
            answer = "queen"
        case "queen":
            answer = "minister"
        case "minister":
            answer = "police"
        case "police":
            answer = "thief"
        case "thief":
            answer = "Game Over"
    if result == answer:
        return True
    
def pos_of_role(role):
    match role:
        case "king":
            return 0
        case "queen":
            return 1
        case "minister":
            return 2
        case "police":
            return 3
        case "thief":
            return 4
        


def shift_positions(role1,role2):
    global characters,pos1,pos2,pos3,pos4,pos5
    for ch in characters:
        if ch.name == role1:
            ch1 = ch
        if ch.name ==role2:
            ch2 = ch
    temp_position = ch1.initial_position
    temp2 = ch2.initial_position
    ch1.move_to_position(ch2.initial_position)
    ch2.move_to_position(ch1.initial_position)
    ch1.initial_position = temp2
    ch2.initial_position = temp_position
      
    


    
    

def exchange_roles(role1,role2):
    global characters,players
    for ch in characters:
        if ch.name == role1:
            ch1 = ch
        if ch.name ==role2:
            ch2 = ch

    pl1 = get_player(players,role=role1)
    pl2 = get_player(players,role=role2)
    
    
    for player in players:
        if player["name"] == pl1[0]:
            
            player["role"] = role2
            # print(player)
            
            
        if player["name"] == pl2[0]:
            # print(player)
            player["role"] = role1
            # print(player)
    # print("exchange roles successful")
     
    
    # print(pl1[0],pl1[2])
    # print(pl2[0],pl2[2])
def highlight_player(role):
    global king,queen,minister,police,thief
    match role:
        case "king":
            pygame.draw.rect(screen,(255,0,0),(king.playerX -32,king.playerY -34,king.image.get_width()+3,king.image.get_height()+10),2)
        case "queen":
            pygame.draw.rect(screen,(255,0,0),(queen.playerX -32,queen.playerY -34,queen.image.get_width()+3,queen.image.get_height()+10),2)
        case "minister":
            pygame.draw.rect(screen,(255,0,0),(minister.playerX -32,minister.playerY -34,minister.image.get_width()+3,minister.image.get_height()+10),2)
        case "police":
            pygame.draw.rect(screen,(255,0,0),(police.playerX -32,police.playerY -34,police.image.get_width()+3,police.image.get_height()+10),2)
        case "thief":
            pygame.draw.rect(screen,(255,0,0),(thief.playerX -32,thief.playerY -34,thief.image.get_width()+3,thief.image.get_height()+10),2)
    


def next_role(current_role):
    match current_role:
        case "king":
            answer = "queen"
        case "queen":
            answer = "minister"
        case "minister":
            answer = "police"
        case "police":
            answer = "thief"
        case "thief":
            answer = "Game Over"
    return answer
game_over = False
start_time = 0
message_end_time = 0
moving = False
next_same_role = False
guessed_incorrectly = False    
guessed_correctly = False
is_clicked = False
order  = player_order_sort(players)
changed_positions = False
repeat = False
display_warn = False
warnMessage = warnFont.render("Guessed correctly",1,(255,0,0))
def player_play(role):
    # warn = False
    global running,next_same_role,guessed_incorrectly,guessed_correctly,is_clicked,order,king,queen,minister,police,thief,changed_positions,moving,repeat,message_end_time,display_warn,warnMessage,start_time,game_over
    pl = get_player(players,role=role)
    if not repeat:
        nRole = next_role(role)
        print("Current PLayer",pl[0])
        print("Role:", pl[2]) 
        print("Guess where is",nRole,"\n")   

    while running:
        
        clock.tick(60)
        
        screen.fill((255,255,255))
        # king.move_to_position((pos3[0],pos3[1]))
        events = pygame.event.get()
        # king.move_to_position()
        if guessed_incorrectly:
            guessed_incorrectly = False
            next_same_role = True
            # changed_positionts = True
            moving = False
        
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if game_over:
                    sys.exit()
            
            result = cursor.clicked(characters,events)
            
            if (not is_clicked or next_same_role):
                if event.type == pygame.MOUSEBUTTONUP and result:
                    is_clicked = True 
                    
                    
                    if guessed(pl[2],result):
                        print("Guessed correctly")
                        start_time = pygame.time.get_ticks()
                        warnMessage = warnFont.render("Guessed correctly",1,(255,0,0))
                        display_warn = True
                        guessed_correctly = True
                        is_clicked=False
                        # nRole = next_role(role)
                        if nRole!="thief":
                            repeat = False
                            player_play(nRole)
                        else:
                            start_time = pygame.time.get_ticks()
                            warnMessage = warnFont.render("Game Over",1,(255,0,0))
                            display_warn = True
                            game_over = True
                            
                    elif result == pl[2]:
                        start_time = pygame.time.get_ticks()
                        warnMessage = warnFont.render(("Guess the "+nRole+"!!"),1,(255,0,0))
                        # global display_warn
                        display_warn = True
                        is_clicked= False
                        
                    else:
                        # prirolnt(order)
                        print("GUessed incorrectly, changing roles")
                        start_time = pygame.time.get_ticks()
                        warnMessage = warnFont.render("Guessed incorrectly,changing roles",1,(255,0,0))
                        display_warn = True
                        pl = get_player(players,role=role)
                        
                        shift_positions(pl[2],result)
                        
                        
                        guessed_incorrectly = True

                    
                        exchange_roles(pl[2],result)
                        pl = get_player(players,role=role)
                        print("Current PLayer",pl[0])
                        print("Role:", pl[2])  
                        print("Guess where is",nRole,"\n")
                        order = player_order_sort(players)
                        repeat = True
                
        
        
        player1NameText = textfont.render(get_player(players,role="king")[0],1,[0,0,0])
        screen.blit(player1NameText,(king.initial_position[0]-28,king.initial_position[1]+50))

        player2NameText = textfont.render(get_player(players,role="queen")[0],1,[0,0,0])
        screen.blit(player2NameText,(queen.initial_position[0]-28,queen.initial_position[1]+50))

        player3NameText = textfont.render(get_player(players,role="minister")[0],1,[0,0,0])
        screen.blit(player3NameText,(minister.initial_position[0]-28,minister.initial_position[1]+50))

        player4NameText = textfont.render(get_player(players,role="police")[0],1,[0,0,0])
        screen.blit(player4NameText,(police.initial_position[0]-28,police.initial_position[1]+50))

        player5NameText = textfont.render(get_player(players,role="thief")[0],1,[0,0,0])
        screen.blit(player5NameText,(thief.initial_position[0]-28,thief.initial_position[1]+50))
        current_player = textfont.render(("Current player : "+get_player(players,role=role)[0]),1,(255,0,0))
        screen.blit(current_player,(300,300))
        guess = textfont.render(("Guess the "+nRole),1,(255,0,0))
        screen.blit(guess,(330,330))

        if display_warn:
            screen.blit(warnMessage,(270,20))

            if pygame.time.get_ticks()-start_time>1500:
                display_warn = False
                if game_over:
                    sys.exit()  
                
                
        
        
        characters.update()
        cursor_group.update()
        # events = pygame.event.get()
        highlight_player(role)
        # screen.blit(king.rect)
        characters.draw(screen)
        cursor_group.draw(screen)
        pygame.display.update()
        # pygame.display.flip()
    
player_play("king")



