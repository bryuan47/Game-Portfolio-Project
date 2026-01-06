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

screen = pygame.display.set_mode((s_width, s_height))
clock = pygame.time.Clock()
walkRight = [pygame.image.load(f"Run ({i}).png") for i in range(1,15)]



pygame.display.set_caption("Samurai Showdown")
bg = pygame.image.load("orig.png")
bg = pygame.transform.scale(bg,(s_width, s_height))
boy = pygame.image.load("Idle (1).png").convert_alpha()
boy = pygame.transform.scale(boy,(100,100))

def Gameloop():
    global walkCount
    if walkCount +1 >= 15:
        walkCount = 0
    
    if right == True:
        screen.blit(walkRight[walkCount],(x,y))
        walkCount = walkCount +1 




#Game Loop 
done = True
while done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    keys= pygame.key.get_pressed()
    screen.blit(bg,(0,0))
    screen.blit(boy,(x,y))
    if keys[pygame.K_LEFT]:
        x = x - vel
        left = True
        right = False
    if keys[pygame.K_RIGHT]:
        x = x + vel
        left = False 
        right = True
    else: 
        right = False
        left = False
        walkCount = 0 
    
    
    

    Gameloop()

    pygame.display.flip()



