import pygame,sys,time
import random
pygame.init()

def graphics(player_1, player_2, gm ):
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


		#RIGHT boxes (YELLOW)
		pygame.draw.rect(screen, BLACK , [414,292, 40,40],1)
		pygame.draw.rect(screen, BLACK , [454,292, 40,40],1)
		pygame.draw.rect(screen, BLACK , [494,292, 40,40],1)
		pygame.draw.rect(screen, BLACK , [534,292, 40,40],1)
		pygame.draw.rect(screen, BLACK , [574,292, 40,40],1)
		pygame.draw.rect(screen, BLACK , [614,292, 40,40],1)
		
		#filled with YELLOW
		pygame.draw.rect(screen, YELLOW, [414,332, 40,40],0)
		pygame.draw.rect(screen, YELLOW, [454,332, 40,40],0)
		pygame.draw.rect(screen, YELLOW, [494,332, 40,40],0)
		pygame.draw.rect(screen, YELLOW, [534,332, 40,40],0)
		pygame.draw.rect(screen, YELLOW, [574,332, 40,40],0)
		pygame.draw.rect(screen, YELLOW, [574,372, 40,40],0)
		pygame.draw.rect(screen, YELLOW, [415,415 ,235 ,235],0)

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
		
		pygame.draw.ellipse(screen, YELLOW, [475,475,40,40],0)
		pygame.draw.ellipse(screen, YELLOW, [540,475,40,40],0)
		pygame.draw.ellipse(screen, YELLOW, [475,540,40,40],0)
		pygame.draw.ellipse(screen, YELLOW, [540,540,40,40],0)



		#UP boxes (GREEN)
		pygame.draw.rect(screen, BLACK , [295,54, 40,40],1)
		pygame.draw.rect(screen, BLACK , [295,94, 40,40],1)
		pygame.draw.rect(screen, BLACK , [295,134, 40,40],1)
		pygame.draw.rect(screen, BLACK , [295,174, 40,40],1)
		pygame.draw.rect(screen, BLACK , [295,214, 40,38],1)
		pygame.draw.rect(screen, BLACK , [295,252, 40,38],1)
		
		#filled with GREEN
		pygame.draw.rect(screen, GREEN, [335,94, 40,40],0)
		pygame.draw.rect(screen, GREEN, [335,134, 40,40],0)
		pygame.draw.rect(screen, GREEN, [335,174, 40,40],0)
		pygame.draw.rect(screen, GREEN, [335,214, 40,38],0)
		pygame.draw.rect(screen, GREEN, [335,252, 40,38],0)
		pygame.draw.rect(screen, GREEN, [375,94, 38,40],0)
		pygame.draw.rect(screen, GREEN, [ 415,55 ,235 ,235],0)

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
		
		pygame.draw.ellipse(screen, GREEN, [475,120,40,40],0)
		pygame.draw.ellipse(screen, GREEN, [475,180,40,40],0)
		pygame.draw.ellipse(screen, GREEN, [540,120,40,40],0)
		pygame.draw.ellipse(screen, GREEN, [540,180,40,40],0)

		#DOWN boxes (BLUE)
		pygame.draw.rect(screen, BLACK , [295,414, 40,40],1)
		pygame.draw.rect(screen, BLACK , [295,454, 40,40],1)
		pygame.draw.rect(screen, BLACK , [295,494, 40,40],1)
		pygame.draw.rect(screen, BLACK , [295,534, 40,40],1)
		pygame.draw.rect(screen, BLACK , [295,574, 40,38],1)
		pygame.draw.rect(screen, BLACK , [295,612, 40,38],1)
		
		#filled with BLUE
		pygame.draw.rect(screen, BLUE, [335,414, 40,40],0)
		pygame.draw.rect(screen, BLUE, [335,454, 40,40],0)
		pygame.draw.rect(screen, BLUE, [335,494, 40,40],0)
		pygame.draw.rect(screen, BLUE, [335,534, 40,40],0)
		pygame.draw.rect(screen, BLUE, [335,574, 40,38],0)
		pygame.draw.rect(screen, BLUE, [295,574, 40,38],0)
		pygame.draw.rect(screen, BLUE, [55,415 ,238 ,235],0)


		#########################
		for i in range(5):
		    pygame.draw.rect(screen, BLACK , [335,414+(i*40), 40,40],1)
		    pygame.draw.rect(screen, BLACK , [375,414+(i*40), 38,40],1)
		pygame.draw.rect(screen, BLACK , [335,612, 40,38],1)
		pygame.draw.rect(screen, BLACK , [375,612, 38,38],1)
		pygame.draw.rect(screen, BLACK , [295,574, 40,38],1)
		pygame.draw.rect(screen, WHITE , [95,455 ,150 ,150],0)
		
		pygame.draw.ellipse(screen, BLUE, [115,475,40,40],0)
		pygame.draw.ellipse(screen, BLUE, [185,475,40,40],0)
		pygame.draw.ellipse(screen, BLUE, [115,540,40,40],0)
		pygame.draw.ellipse(screen, BLUE, [185,540,40,40],0)


                R_I=[{'x':115,'y': 120},{'x':185,'y': 120},{'x':115,'y': 180},{'x':115,'y': 180}]
                B_I=[{'x':115,'y': 475},{'x':185,'y': 475},{'x':115,'y': 540},{'x':185,'y': 540}]
                G_I=[{'x':475,'y': 120},{'x':475,'y': 180},{'x':540,'y': 120},{'x':540,'y': 180}]
                Y_I=[{'x':475,'y': 475},{'x':540,'y': 475},{'x':475,'y': 540},{'x':540,'y': 540}]
	
		position=[{'x':96,'y': 296},{'x':136,'y':296},{'x':176,'y':296},{'x':216,'y':296},{'x':256,'y':296},{'x':297,'y':254},
		          {'x':297,'y': 216},{'x':297,'y':176},{'x':297,'y':136},{'x':297,'y':96},{'x':297,'y':56},{'x':337,'y':56},
		          {'x':337,'y': 96},{'x':337,'y':136},{'x':337,'y':176},{'x':337,'y':216},{'x':337,'y':254},{'x':377,'y':56},
		          {'x':377,'y': 96},{'x':377,'y':136},{'x':377,'y':176},{'x':377,'y':216},{'x':377,'y':254},{'x':416,'y':296},
			  {'x':456,'y': 296},{'x':496,'y':296},{'x':536,'y':296},{'x':576,'y':296},{'x':616,'y':296},{'x':616,'y':334},
                          {'x':576,'y': 334},{'x':536,'y':334},{'x':496,'y':334},{'x':456,'y':334},{'x':416,'y':334},{'x':616,'y':374},
                          {'x':576,'y': 374},{'x':536,'y':374},{'x':496,'y':374},{'x':456,'y':374},{'x':416,'y':374},{'x':377,'y':614},
                          {'x':377,'y': 576},{'x':377,'y':536},{'x':377,'y':496},{'x':377,'y':456},{'x':377,'y':416},{'x':297,'y':614},
                          {'x':297,'y': 576},{'x':297,'y':536},{'x':297,'y':496},{'x':297,'y':456},{'x':297,'y':416},{'x':256,'y':374},
                          {'x':216,'y': 374},{'x':176,'y':374},{'x':136,'y':374},{'x':96,'y':374},{'x':56,'y':374},{'x':56,'y':334},
                          {'x':66,'y': 334},{'x':136,'y':334},{'x':176,'y':334},{'x':216,'y':334},{'x':256,'y':334},{'x':56,'y':296},
		          ]

		for p in range(4):
                    if(gm==0):
		                if(my_player.ptokenlist[p].location==-1):
		                   coins[p]['x']=R_I[p]['x'] 
		                   coins[p]['y']=R_I[p]['y']   
		                else:
		                   coins[p]['x']=position[my_player.ptokenlist[p].location]['x']
				           coins[p]['y']=position[my_player.ptokenlist[p].location]['y']
		                if(opp_player.ptokenlist[p].location==-1):
		                   coins_o[p]['x']=Y_I[p]['x'] 
		                   coins_o[p]['y']=Y_I[p]['y']   
		                else:
		                   coins_o[p]['x']=position[opp_player.ptokenlist[p].location]['x']
				           coins_o[p]['y']=position[opp_player.ptokenlist[p].location]['y']
                    else:
                        if(my_player.ptokenlist[p].location==-1):
		                   coins[p]['x']=B_I[p]['x'] 
		                   coins[p]['y']=B_I[p]['y']   
		                else:
		                   coins[p]['x']=position[my_player.ptokenlist[p].location]['x']
				           coins[p]['y']=position[my_player.ptokenlist[p].location]['y']
		                if(opp_player.ptokenlist[p].location==-1):
		                   coins_o[p]['x']=G_I[p]['x'] 
		                   coins_o[p]['y']=G_I[p]['y']   
		                else:
		                   coins_o[p]['x']=position[opp_player.ptokenlist[p].location]['x']
				           coins_o[p]['y']=position[opp_player.ptokenlist[p].location]['y']
		        pygame.draw.ellipse(screen, COLOR1, [coins[p]['x'],coins[p]['y'],35,35],0)
			    pygame.draw.ellipse(screen, COLOR2, [coins_o[p]['x'],coins_o[p]['y'],35,35],0)
		    pygame.display.update()
		    time.sleep(0.8)
        pygame.display.flip()
	    clocktime.tick(60)

class Token:

    counter = 0

    def __init__(self, color, id, location):

        self.color = color

        self.id = id

        self.location = location



    def setlocation(self, loc):

        self.location = loc



    def getlocation(self):

        return self.location



    def getid(self):

        return self.id





class Player:



    win_pieces = 0      #number of token reached passed the home lane i;e out of the board

    out_pieces = 0      # number of pieces out of the home state



    def __init__(self, pid, color, ptokenlist):

        self.pid = pid

        self.color = color

        self.ptokenlist = ptokenlist



    @classmethod

    def haswon(self):



        if self.win_pieces == 4:

            return True

        else:

            return False





class Cell:

    color = ''

    safe_state_flag = False

    home_lane_flag = False

    start_state_flag = False

    def __init__(self, color, safe_state_flag, home_lane_flag, start_state_flag):

        # self.index = index      this not required because it can be accessed using list index only

        self.color = color  # assigned to special cell otherwise "W"

        self.safe_state_flag = safe_state_flag

        self.home_lane_flag = home_lane_flag

        self.start_state_flag = start_state_flag



		
		
tl = sys.stdin.readline().strip()

tl1 = int(tl.split(' ')[1])

pid = int(tl.split(' ')[0])

gm = int(tl.split(' ')[2])



sys.stderr.write('Time limit is {} \nGame mode is {}\n'.format(tl1, gm))



counter = -1

tokenID = 0

init_flag = False

if gm == 0:

    color = ['R','Y']

else:

    color = ['B','G']



tokenlist = []



for i in range(4):

    tokenlist.append(Token(color[pid-1], i, -1))    # -1 indicates that token is in home. create object for each token

my_player = Player(pid, color[pid-1], tokenlist)  # object of player 1

opp_player = Player(3-pid, color[2-pid], tokenlist)  # object of player 1

#print(my_player.haswon())



startStates = {'R':0,'G':18,'Y':36,'B': 54}

inside = [0,1,2,3]

outside = []

Board = []

Board.append(Cell("W", True, False, True))  # 0 starts with red start cell



for i in range(1, 8, 1):  # white color

    Board.append(Cell("W", False, False, False))



Board.append(Cell("W", True, False, False))  # green safe state



for i in range(9, 12, 1):

    Board.append(Cell("W", False, False, False))



for i in range(12, 17, 1):  # home lane of green

    Board.append(Cell("G", False, True, False))



Board.append(Cell("W", False, False, False))

Board.append(Cell("W", True, False, True))  # start state of green



for i in range(19, 26, 1):  # white between green start and yellow safe

    Board.append(Cell("W", False, False, False))



Board.append(Cell("W", True, False, False))  # safe state of yellow



for i in range(27, 30, 1):  # white of yellow

    Board.append(Cell("W", False, False, False))



for i in range(30, 35, 1):  # home lane of yellow

    Board.append(Cell("Y", False, True, False))



Board.append(Cell("W", False, False, False))

Board.append(Cell("W", True, False, True))  # start state of yellow



for i in range(37, 44, 1):  # white between yellow start and blue safe

    Board.append(Cell("W", False, False, False))



Board.append(Cell("W", True, False, False))  # safe state of blue



for i in range(45, 48, 1):  # white

    Board.append(Cell("W", False, False, False))



for i in range(48, 53, 1):  # home lane of blue

    Board.append(Cell("B", False, True, False))



Board.append(Cell("W", False, False, False))

Board.append(Cell("W", True, False, True))  # start state of blue



for i in range(55, 62, 1):  # white between blue start and red safe

    Board.append(Cell("W", False, False, False))



Board.append(Cell("W", True, False, False))  # safe state of red



for i in range(63, 66, 1):  # white

    Board.append(Cell("W", False, False, False))



for i in range(66, 71, 1):  # home lane of red

    Board.append(Cell("R", False, True, False))



Board.append(Cell("W", False, False, False))



#print(Board)

#for item in Board:

    #print(item.color, item.home_lane_flag)



#update board and return "Invalid" if not possible

def updateboard(token_no,dice_value):

    token_pos = my_player.ptokenlist[token_no].location + dice_value

    my_player.ptokenlist[token_no].counter += dice_value

    if(my_player.ptokenlist[token_no].color != Board[token_pos].color) and (Board[token_pos].color != "W"):

        token_pos +=5



    if(my_player.ptokenlist[token_no].counter >56 ): #change 33 to correct value of toatal moves possible

        return "Invalid"

    if(Board[token_pos].safe_state_flag == True):

        my_player.ptokenlist[token_no].location = token_pos



    for i in range(4):

        if my_player.ptokenlist[i].location == token_pos:

            return "Invalid"

    for i in range(4):

        if opp_player.ptokenlist[i].location == token_pos:

            opp_player.ptokenlist[i].location = -1



    my_player.ptokenlist[token_no].location = token_pos



    return str(token_no)


alive= True
size=(1000,1000)
WHITE=(255,255,255)
RED= (255, 0, 0)
BLACK=(0,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
COLOR1=(78,21,21)
COLOR2=(8,74,13)
coins=[{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0}]
coins_o=[{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0}]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Assignment-2 :Ludo Bot")
 
# Used to manage how fast the screen updates
clocktime = pygame.time.Clock()
 
while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
            pygame.quit()
    REPEAT = False
    init_flag == False

    sys.stderr.write('<BEFORE WHILE>\n')
    while (not my_player.haswon()) and (not opp_player.haswon()):

	    if REPEAT == False:

		sys.stderr.write('<IN WHILE>\n')

		my_color = my_player.color  #returns the color of this player
		if pid == 2 and init_flag == False:
		    init_flag = True
		    dice = sys.stdin.readline().strip()
		    sys.stderr.write('pid 2 PRINT DICE: ' + dice + '\n')
		    move = sys.stdin.readline().strip()
		    sys.stderr.write('pid 2 PRINT MOVE: ' + move + '\n')

		sys.stdout.write('<THROW>\n')

		sys.stdout.flush()

	       

		dice = sys.stdin.readline().strip()

		sys.stderr.write('read from dice string ' + dice + '\n')

		dice_value = int(dice.split(' ')[2])     #returns the number on dice

		

		if(my_player.out_pieces == 0):      #all the 4 tokens are inside home state

		    if(dice_value == 6 or dice_value == 1):

		        my_player.ptokenlist[0].setlocation(startStates[my_color]+dice_value)       #set the token to start position+dicevalue

		        my_player.out_pieces = my_player.out_pieces + 1

		        my_player.ptokenlist[0].counter += dice_value

		        sys.stderr.write('move sent: ' + str(dice_value) + '\n')

		        sys.stdout.write(my_color+str(0)+'_'+str(dice_value)+'\n')

		        #update board

		     #else what to send to server??

		    else:

		        sys.stdout.write('NA\n')

		else:

		    if (dice_value == 6 or dice_value == 1) and (my_player.out_pieces != 4):

		       for i in range(4):

		           if (my_player.ptokenlist[i].location == -1):

		               my_player.ptokenlist[i].setlocation(startStates[my_color] + dice_value)

		               my_player.out_pieces = my_player.out_pieces + 1

		               my_player.ptokenlist[i].counter += dice_value

		               sys.stdout.write(my_color + str(0) +'_'+ str(dice_value) + '\n')

		    else:

		        f=0

		        x = ''

		        index=-1

		        for i in range(4):

		            x = updateboard(i,dice_value)

		            if x == 'Invalid':

		                continue

		            else:

		                f=1

		                index = i

		                break;

		        if f == 1:

		            sys.stdout.write(my_color + str(index) +'_'+ str(dice_value) + '\n')

		        else:

		            sys.stdout.write('NA')



		'''else:      #if atleast 1 token is out of home state

		    t=getBestPossibleMove(my_player,opp_player,dice_value,Board)     #returns the token  which should be moved

		    ind=validIndex(t,dice_value,Board)          #returns the valid index at which t is to be placed

		    my_player.ptokenlist[t.id].setlocation(ind)  # set the token to start position+dicevalue

		    sys.stdout.write(my_color + str(t.id) + str(dice_value) + '\n')

		    # update board'''



	    #sys.stdout.write(color[pid - 1] + str(tokenID) + '_1\n')

		sys.stdout.flush()

	    else:

		REPEAT = False

	    sys.stderr.write('<AFTER WHILW>\n')

	    dice = sys.stdin.readline().strip()

	    if dice != 'REPEAT':

	    	sys.stderr.write('bot_msg_dice: ' + dice + '\n')

	    	move = sys.stdin.readline().strip()

	    	sys.stderr.write('bot_msg_move: ' + move + '\n')

	    	if move.strip().split('<next>')[-1] == 'REPEAT':

			REPEAT = True    
        graphics(my_player, opp_player, gm)
