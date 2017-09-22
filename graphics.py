import pygame,sys,time
pygame.init()

"""class board:
    int x
    int y
    char color

    def _init_ (self, x):
        self.color = x"""
    

alive= True
size=(1000,1000)
WHITE=(255,255,255)
RED= (255, 0, 0)
BLACK=(0,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Assignment-2 :Ludo Bot")
 
# Used to manage how fast the screen updates
clocktime = pygame.time.Clock()
 
while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
            pygame.quit()
            
            
   
    for p in range(24):
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK , [50,50,604,604],1)
        pygame.draw.rect(screen, BLACK , [52,52,600,600],1)

        #left boxes (RED)
        pygame.draw.rect(screen, BLACK , [54,292, 40,40],1)
        pygame.draw.rect(screen, BLACK , [134,292, 40,40],1)
        pygame.draw.rect(screen, BLACK , [174,292, 40,40],1)
        pygame.draw.rect(screen, BLACK , [214,292, 40,40],1)
        pygame.draw.rect(screen, BLACK , [254,292, 40,40],1)
        
        #filled with red
        pygame.draw.rect(screen, RED, [94,332, 40,40],0)
        pygame.draw.rect(screen, RED, [134,332, 40,40],0)
        pygame.draw.rect(screen, RED, [174,332, 40,40],0)
        pygame.draw.rect(screen, RED, [214,332, 40,40],0)
        pygame.draw.rect(screen, RED, [254,332, 40,40],0)
        pygame.draw.rect(screen, RED, [94,292, 40,40],0)
        pygame.draw.rect(screen, RED, [55,55 ,238 ,235],0)

        #########################
        pygame.draw.rect(screen, BLACK , [94,292, 40,40],1)
        pygame.draw.rect(screen, BLACK , [54,332, 40,40],1)
        pygame.draw.rect(screen, BLACK , [94,332, 40,40],1)
        pygame.draw.rect(screen, BLACK , [134,332, 40,40],1)
        pygame.draw.rect(screen, BLACK , [174,332, 40,40],1)
        pygame.draw.rect(screen, BLACK , [214,332, 40,40],1)
        pygame.draw.rect(screen, BLACK , [254,332, 40,40],1)
        pygame.draw.rect(screen, BLACK , [54,372, 40,40],1)
        pygame.draw.rect(screen, BLACK , [94,372, 40,40],1)
        pygame.draw.rect(screen, BLACK , [134,372, 40,40],1)
        pygame.draw.rect(screen, BLACK , [174,372, 40,40],1)
        pygame.draw.rect(screen, BLACK , [214,372, 40,40],1)
        pygame.draw.rect(screen, BLACK , [254,372, 40,40],1)
        pygame.draw.rect(screen, WHITE , [95,95 ,150 ,150],0)
        
        pygame.draw.ellipse(screen, RED, [115,120,40,40],0)
        pygame.draw.ellipse(screen, RED, [185,120,40,40],0)
        pygame.draw.ellipse(screen, RED, [115,180,40,40],0)
        pygame.draw.ellipse(screen, RED, [185,180,40,40],0)


        #RIGHT boxes (GREEN)
        pygame.draw.rect(screen, BLACK , [414,292, 40,40],1)
        pygame.draw.rect(screen, BLACK , [454,292, 40,40],1)
        pygame.draw.rect(screen, BLACK , [494,292, 40,40],1)
        pygame.draw.rect(screen, BLACK , [534,292, 40,40],1)
        pygame.draw.rect(screen, BLACK , [574,292, 40,40],1)
        pygame.draw.rect(screen, BLACK , [614,292, 40,40],1)
        
        #filled with GREEN
        pygame.draw.rect(screen, GREEN, [414,332, 40,40],0)
        pygame.draw.rect(screen, GREEN, [454,332, 40,40],0)
        pygame.draw.rect(screen, GREEN, [494,332, 40,40],0)
        pygame.draw.rect(screen, GREEN, [534,332, 40,40],0)
        pygame.draw.rect(screen, GREEN, [574,332, 40,40],0)
        pygame.draw.rect(screen, GREEN, [574,372, 40,40],0)
        pygame.draw.rect(screen, GREEN, [415,415 ,235 ,235],0)

        #########################
        pygame.draw.rect(screen, BLACK , [454,292, 40,40],1)
        pygame.draw.rect(screen, BLACK , [414,332, 40,40],1)
        pygame.draw.rect(screen, BLACK , [454,332, 40,40],1)
        pygame.draw.rect(screen, BLACK , [494,332, 40,40],1)
        pygame.draw.rect(screen, BLACK , [534,332, 40,40],1)
        pygame.draw.rect(screen, BLACK , [574,332, 40,40],1)
        pygame.draw.rect(screen, BLACK , [614,332, 36,40],1)
        pygame.draw.rect(screen, BLACK , [414,372, 40,40],1)
        pygame.draw.rect(screen, BLACK , [454,372, 40,40],1)
        pygame.draw.rect(screen, BLACK , [494,372, 40,40],1)
        pygame.draw.rect(screen, BLACK , [534,372, 40,40],1)
        pygame.draw.rect(screen, BLACK , [574,372, 40,40],1)
        pygame.draw.rect(screen, BLACK , [614,372, 40,40],1)
        pygame.draw.rect(screen, WHITE , [455,455 ,150 ,150],0)
        
        pygame.draw.ellipse(screen, GREEN, [475,475,40,40],0)
        pygame.draw.ellipse(screen, GREEN, [540,475,40,40],0)
        pygame.draw.ellipse(screen, GREEN, [475,540,40,40],0)
        pygame.draw.ellipse(screen, GREEN, [540,540,40,40],0)



        #UP boxes (BLUE)
        pygame.draw.rect(screen, BLACK , [295,54, 40,40],1)
        pygame.draw.rect(screen, BLACK , [295,94, 40,40],1)
        pygame.draw.rect(screen, BLACK , [295,134, 40,40],1)
        pygame.draw.rect(screen, BLACK , [295,174, 40,40],1)
        pygame.draw.rect(screen, BLACK , [295,214, 40,38],1)
        pygame.draw.rect(screen, BLACK , [295,252, 40,38],1)
        
        #filled with BLUE
        pygame.draw.rect(screen, BLUE, [335,94, 40,40],0)
        pygame.draw.rect(screen, BLUE, [335,134, 40,40],0)
        pygame.draw.rect(screen, BLUE, [335,174, 40,40],0)
        pygame.draw.rect(screen, BLUE, [335,214, 40,38],0)
        pygame.draw.rect(screen, BLUE, [335,252, 40,38],0)
        pygame.draw.rect(screen, BLUE, [375,94, 38,40],0)
        pygame.draw.rect(screen, BLUE, [ 415,55 ,235 ,235],0)

        #########################
        pygame.draw.rect(screen, BLACK , [335,54, 40,40],1)
        pygame.draw.rect(screen, BLACK , [335,94, 40,40],1)
        pygame.draw.rect(screen, BLACK , [335,134, 40,40],1)
        pygame.draw.rect(screen, BLACK , [335,174, 40,40],1)
        pygame.draw.rect(screen, BLACK , [335,214, 40,38],1)
        pygame.draw.rect(screen, BLACK , [335,252, 40,38],1)
        pygame.draw.rect(screen, BLACK , [375,54, 38,40],1)
        pygame.draw.rect(screen, BLACK , [375,94, 38,40],1)
        pygame.draw.rect(screen, BLACK , [375,134, 38,40],1)
        pygame.draw.rect(screen, BLACK , [375,174, 38,40],1)
        pygame.draw.rect(screen, BLACK , [375,214, 38,38],1)
        pygame.draw.rect(screen, BLACK , [375,252, 38,38],1)
        pygame.draw.rect(screen, BLACK , [614,372, 40,40],1)
        pygame.draw.rect(screen, WHITE , [455,95 ,150 ,150],0)
        
        pygame.draw.ellipse(screen, BLUE, [475,120,40,40],0)
        pygame.draw.ellipse(screen, BLUE, [475,180,40,40],0)
        pygame.draw.ellipse(screen, BLUE, [540,120,40,40],0)
        pygame.draw.ellipse(screen, BLUE, [540,180,40,40],0)

        #DOWN boxes (YELLOW)
        pygame.draw.rect(screen, BLACK , [295,414, 40,40],1)
        pygame.draw.rect(screen, BLACK , [295,454, 40,40],1)
        pygame.draw.rect(screen, BLACK , [295,494, 40,40],1)
        pygame.draw.rect(screen, BLACK , [295,534, 40,40],1)
        pygame.draw.rect(screen, BLACK , [295,574, 40,38],1)
        pygame.draw.rect(screen, BLACK , [295,612, 40,38],1)
        
        #filled with YELLOW
        pygame.draw.rect(screen, YELLOW, [335,414, 40,40],0)
        pygame.draw.rect(screen, YELLOW, [335,454, 40,40],0)
        pygame.draw.rect(screen, YELLOW, [335,494, 40,40],0)
        pygame.draw.rect(screen, YELLOW, [335,534, 40,40],0)
        pygame.draw.rect(screen, YELLOW, [335,574, 40,38],0)
        pygame.draw.rect(screen, YELLOW, [295,574, 40,38],0)
        pygame.draw.rect(screen, YELLOW, [55,415 ,238 ,235],0)


        #########################
        pygame.draw.rect(screen, BLACK , [335,414, 40,40],1)
        pygame.draw.rect(screen, BLACK , [335,454, 40,40],1)
        pygame.draw.rect(screen, BLACK , [335,494, 40,40],1)
        pygame.draw.rect(screen, BLACK , [335,534, 40,40],1)
        pygame.draw.rect(screen, BLACK , [335,574, 40,38],1)
        pygame.draw.rect(screen, BLACK , [335,612, 40,38],1)
        pygame.draw.rect(screen, BLACK , [375,414, 38,40],1)
        pygame.draw.rect(screen, BLACK , [375,454, 38,40],1)
        pygame.draw.rect(screen, BLACK , [375,494, 38,40],1)
        pygame.draw.rect(screen, BLACK , [375,534, 38,40],1)
        pygame.draw.rect(screen, BLACK , [375,574, 38,38],1)
        pygame.draw.rect(screen, BLACK , [375,612, 38,38],1)
        pygame.draw.rect(screen, BLACK , [295,574, 40,38],1)
        pygame.draw.rect(screen, WHITE , [95,455 ,150 ,150],0)
        
        pygame.draw.ellipse(screen, YELLOW, [115,475,40,40],0)
        pygame.draw.ellipse(screen, YELLOW, [185,475,40,40],0)
        pygame.draw.ellipse(screen, YELLOW, [115,540,40,40],0)
        pygame.draw.ellipse(screen, YELLOW, [185,540,40,40],0)

        #pygame.draw.ellipse(screen, BLACK, [96,296,35,35],0)
        
        position=[{'x':96,'y': 296},{'x':136,'y':296},{'x':176,'y':296},{'x':216,'y':296},{'x':256,'y':296},{'x':297,'y':254},
                  {'x':297,'y': 216},{'x':297,'y':176},{'x':297,'y':136},{'x':297,'y':96},{'x':297,'y':56},{'x':337,'y':56},
                  {'x':337,'y': 96},{'x':337,'y':136},{'x':337,'y':176},{'x':337,'y':216},{'x':337,'y':254},{'x':377,'y':56},
                  {'x':377,'y': 96},{'x':377,'y':136},{'x':377,'y':176},{'x':377,'y':216},{'x':377,'y':216},{'x':416,'y':296},
                  ]

        rx=position[p]['x']
        ry=position[p]['y']
        pygame.draw.ellipse(screen, BLACK, [rx,ry,35,35],0)
        pygame.display.update()
        time.sleep(0.2)
    
    pygame.display.flip()
    clocktime.tick(60)
