import pygame 
pygame.init()

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



neg = 1

screen = pygame.display.set_mode((s_width, s_height))
clock = pygame.time.Clock()
walkRight = [pygame.transform.scale(pygame.image.load(f"Game_portfolio\Game-Portfolio-Project\Run ({i}).png").convert_alpha(),(100,100)) for i in range(1,9)]
walkLeft = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(f"Game_portfolio\Game-Portfolio-Project\Run ({i}).png").convert_alpha(),(100,100)), True, False) for i in range(1,9)]
font = pygame.font.SysFont("helvetica", 30,1,1)
score = 0



pygame.display.set_caption("Jumping Kid")
bg = pygame.image.load("Game_portfolio\orig.png")
bg = pygame.transform.scale(bg,(s_width, s_height))

idle_img = pygame.transform.scale(pygame.image.load(f"Game_portfolio\Game-Portfolio-Project\Idle (1).png").convert_alpha(),(100,100))

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

class Projectiles():
    def __init__(self, x ,y, radius, color, directions):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.directions = directions 
        self.vel = 8 *directions

    def draw2(self,screen):
         pygame.draw.circle(screen,self.color,(self.x,self.y), self.radius)




def Gameloop():
    clock.tick(60)
    screen.blit(bg,(0,0))
    boy.draw(screen)
    text = font.render("Score: " + str(score), 1, "red")
    screen.blit(text,(0,10))
    pygame.display.flip()
    for bullet in bullets:
        bullet.draw2(screen)
    
    



boy = Player(50,300,64,64)
bullets =[]
#Game Loop 
done = True
while done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    
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

  



