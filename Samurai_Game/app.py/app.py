import pygame 
pygame.init()

#making the main loop
s_width = 600
s_height = 400
x= 0
y = 0
vel = 5

screen = pygame.display.set_mode((s_width, s_height))
clock = pygame.time.Clock



pygame.display.set_caption("Samurai Showdown")
bg = pygame.image.load("orig.png")
bg = pygame.transform.scale(bg,(s_width, s_height))
boy = pygame.image.load("Idle (1).png").convert_alpha()
boy = pygame.transform.scale(boy,(100,100))






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
    if keys[pygame.K_RIGHT]:
        x = x + vel
    
    
    



    pygame.display.flip()



