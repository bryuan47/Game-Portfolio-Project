import pygame 
import time 
pygame.init()
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR,"Game")
#making the main loop
s_width = 600
s_height = 400
x= 50
y = 300
vel = 5
left = False
right = False
walkCount = 0
width = 100
height = 100



neg = 1 #gravity 

screen = pygame.display.set_mode((s_width, s_height))
clock = pygame.time.Clock()
walkRight = [pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, f"Run ({i}).png")).convert_alpha(),(100,100)) for i in range(1,9)]
walkLeft = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR,f"Run ({i}).png")).convert_alpha(),(100,100)), True, False) for i in range(1,9)]
font = pygame.font.SysFont("helvetica", 30,1,1)
score = 0
time_left = 60
pygame.time.set_timer(pygame.USEREVENT,1000)



pygame.display.set_caption("Jumping Kid")
bg = pygame.image.load(os.path.join(BASE_DIR,f"orig.png"))
bg = pygame.transform.scale(bg,(s_width, s_height))

idle_img = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR,f"Idle (1).png")).convert_alpha(),(100,100))
game_over = False


    

#player class 
class Player:
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
        self.left = False
        self.right = False
        self.jump_count = 10
        self.is_jump = False
        self.walkCount = 0
        self.vel = 5
        self.standing = True
    def draw(self,screen):
        if self.walkCount +1 >= 9:
            self.walkCount = 0
    #Animation logic for running right and left
        if not(self.standing):
            if self.right == True:
                screen.blit(walkRight[self.walkCount //2],(self.x,self.y))
                self.walkCount = self.walkCount +1 
        
            elif self.left == True:
                screen.blit(walkLeft[self.walkCount //2],(self.x,self.y))
                self.walkCount = self.walkCount +1 
        
        else: 
            if self.right:
               screen.blit(walkRight[0],(self.x,self.y))   
            else:
                screen.blit(walkLeft[0],(self.x,self.y))

#Projectiles Class 
class Projectiles():
    def __init__(self, x ,y, radius, color, directions):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.directions = directions 
        self.vel = 8 *directions
    #Draw method to show projectiles
    def draw2(self,screen):
         pygame.draw.circle(screen,self.color,(self.x,self.y), self.radius)



#GameLoop
def Gameloop():
    global done
    global score
    global time_left
    clock.tick(60)
    screen.blit(bg,(0,0))
    boy.draw(screen)
    text = font.render("Score: " + str(score), 1, "red")
    screen.blit(text,(0,10))
    
    timer_text = font.render(f"Time: {time_left}", True ,"red")
    screen.blit(timer_text,(0,100))
     
    for bullet in bullets:
        bullet.draw2(screen)
    
    if time_left <= 0:
        pygame.time.set_timer(pygame.USEREVENT, 0)
        #game over restart sequence
        game_over = True
        if game_over:
            play_again = font.render("Press Esc to play again! Press Enter to quit!", True, "red")
            screen.blit(play_again,(50,150))
            
            if keys[pygame.K_ESCAPE]:          
                score = 0
                time_left = 60
                pygame.time.set_timer(pygame.USEREVENT,1000)
                
            elif keys[pygame.K_RETURN]:
                done = False
    

    pygame.display.flip()


boy = Player(50,300,64,64)
bullets =[]
#Game Loop 
done = True
while done: 
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.USEREVENT:
            time_left = time_left -1
        if time_left <= 0:
            game_over == True
          
            

    for bullet in bullets:
        if bullet.x < 400 and bullet.x > 0:
            bullet.x = bullet.x + vel
        else:
            bullets.pop(bullets.index(bullet))
    
    
    keys= pygame.key.get_pressed()
  
   #direction logic
    if keys[pygame.K_LEFT] and boy.x > 0:
        boy.x = boy.x - vel
        boy.left = True
        boy.right = False
        boy.standing = False
    elif keys[pygame.K_RIGHT] and boy.x < s_width -100:
        boy.x = boy.x + vel
        boy.left = False 
        boy.right = True
        boy.standing = False
    else:
        boy.standing = True
        boy.walkCount = 0

    if keys[pygame.K_TAB]:
        if boy.left: 
            directions = -1
        else: 
            directions = 1
        if len(bullets) < 5:
            bullets.append(Projectiles((boy.x + boy.width//2),(boy.y +boy.height//2),6,"black",directions))
   
   
    #Jump logic
    if keys[pygame.K_SPACE] and not boy.is_jump and boy.y < s_height:
        boy.is_jump = True
        score += 1
    
    if boy.is_jump:
            if boy.jump_count >= -10:
                neg = 1
                if boy.jump_count <0:
                    neg = -1
                boy.y = boy.y - (boy.jump_count ** 2) * neg * 0.5 # reduce jump height by dividing by 2
                boy.jump_count= boy.jump_count -1   
            else: 
                boy.jump_count = 10
                boy.is_jump = False
        
 
    
            
    
    
    

    Gameloop()

  



