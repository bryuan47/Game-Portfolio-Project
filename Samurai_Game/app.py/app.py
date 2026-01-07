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

neg = 1

screen = pygame.display.set_mode((s_width, s_height))
clock = pygame.time.Clock()
walkRight = [pygame.transform.scale(pygame.image.load(f"Game-Portfolio-Project\Run ({i}).png").convert_alpha(),(100,100)) for i in range(1,9)]
walkLeft = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(f"Game-Portfolio-Project\Run ({i}).png").convert_alpha(),(100,100)), True, False) for i in range(1,9)]



pygame.display.set_caption("Samurai Showdown")
bg = pygame.image.load("orig.png")
bg = pygame.transform.scale(bg,(s_width, s_height))
boy = pygame.image.load("Game-Portfolio-Project\Idle (1).png").convert_alpha()
boy = pygame.transform.scale(boy,(100,100))

def Gameloop():
    clock.tick(60)
    global walkCount
    if walkCount +1 >= 9:
        walkCount = 0
    

    if right == True:
        screen.blit(walkRight[walkCount //2],(x,y))
        walkCount = walkCount +1 
       
    elif left == True:
        screen.blit(walkLeft[walkCount //2],(x,y))
        walkCount = walkCount +1 
       
    else: 
        walkCount = 0
        screen.blit(boy,(x,y))
    

    
    pygame.display.flip()
    
    
        
        
is_jump = False
jump_count = 10


#Game Loop 
done = True
while done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    keys= pygame.key.get_pressed()
    screen.blit(bg,(0,0))
   
    if keys[pygame.K_LEFT] and x > 0:
        x = x - vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < s_width -100:
        x = x + vel
        left = False 
        right = True
    else:
        right = False
        left = False
    
    
    
    
 
    if keys[pygame.K_SPACE] and not is_jump and y < s_height:
        is_jump = True
        
    
    
    if is_jump:
            if jump_count >= -10:
                neg = 1
                if jump_count <0:
                    neg = -1
                y = y - (jump_count ** 2) * neg * 0.5 # reduce jump height by dividing by 2
                jump_count= jump_count -1   
            else: 
                jump_count = 10
                is_jump = False
        

   
    
    
    
    

    Gameloop()

  



