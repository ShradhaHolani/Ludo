# TODO -To check time limit 120s
#If you need 1 to finish the token and also 1 token is inside home state-then what should be done

import pygame,sys,time
import random
import traceback
pygame.init()

# set token variables like color,id,location

def graphics(player_1, player_2, gm, win ):
	COLOR1=(0,0,0)
	COLOR2=(0,0,0)
	screen.fill(WHITE)
	string=''

	myfont = pygame.font.SysFont('Comic Sans MS', 35)
	myfont_d = pygame.font.SysFont('Comic Sans MS', 50)
	for i in dice_value_list:
		string =string+ str(i)+'  '
	textsurface = myfont.render('Dice Move', False, (0, 0, 0))
	textsurface1=myfont_d.render(string, False, (0, 0, 0))
	textsurface2 = myfont_d.render("Player No. " + str(pid) , False, (0, 0, 0))
	textsurface3 = myfont_d.render("YOU WIN", False, (0, 0, 0))
	textsurface4=myfont_d.render("YOU LOST", False, (0, 0, 0))
	if(win==1):
		if (my_player.ptokenlist[0].getlocation()==-2 and my_player.ptokenlist[1].getlocation()==-2 and my_player.ptokenlist[2].getlocation()==-2 and my_player.ptokenlist[3].getlocation()==-2 ):
			screen.blit(textsurface3,(750,500))
		else:
			screen.blit(textsurface4, (750, 500))
	screen.blit(textsurface2,(750, 60))
	#screen.blit(textsurface, (720,320))
	#screen.blit(textsurface1, (750, 360))

	pygame.draw.rect(screen, BLACK , [50,50,604,604],1)
	pygame.draw.rect(screen, BLACK , [52,52,600,600],1)
	#pygame.draw.rect(screen, BLACK, [700,300,150,150],3)

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

	R_I=[{'x':115,'y': 120},{'x':185,'y': 120},{'x':115,'y': 180},{'x':185,'y': 180}]
	B_I=[{'x':115,'y': 475},{'x':185,'y': 475},{'x':115,'y': 540},{'x':185,'y': 540}]
	G_I=[{'x':475,'y': 120},{'x':475,'y': 180},{'x':540,'y': 120},{'x':540,'y': 180}]
	Y_I=[{'x':475,'y': 475},{'x':540,'y': 475},{'x':475,'y': 540},{'x':540,'y': 540}]
	M_F= [{'x': 720, 'y': 115}, {'x': 770, 'y': 115}, {'x': 820, 'y': 115}, {'x': 860, 'y': 115}]
	O_F= [{'x': 720, 'y': 175}, {'x': 770, 'y': 175}, {'x': 820, 'y': 175}, {'x': 860, 'y': 175}]

	position=[{'x':96,'y':294, 'c':0,'d':0},{'x':136,'y':294,'c':0, 'd':0},{'x':176,'y':294, 'c':0, 'd':0},{'x':216,'y':294,'c':0,'d':0},{'x':256,'y':294, 'c':0,'d':0},{'x':297,'y':254, 'c':0,'d':0},
              {'x':297,'y':216,'c':0, 'd':0},{'x':297,'y':176,'c':0,'d':0},{'x':297,'y':136,'c':0,'d':0},{'x':297,'y':96,'c':0,'d':0},{'x':297,'y':56,'c':0, 'd':0},{'x':337,'y':56, 'c':0,'d':0},
              {'x':337,'y':96,'c':0, 'd':0},{'x':337,'y':136, 'c':0,'d':0},{'x':337,'y':176, 'c':0,'d':0},{'x':337,'y':216, 'c':0, 'd':0},{'x':337,'y':254, 'c':0,'d':0},{'x': 377,'y':56, 'c':0,'d':0},
              {'x':377,'y':96, 'c':0,'d':0},{'x':377,'y':136, 'c':0,'d':0},{'x':377,'y':176,'c':0,'d':0},{'x':377,'y':216, 'c':0,'d':0},{'x':377,'y':254, 'c':0, 'd':0},{'x':416,'y': 294, 'c':0,'d':0},
              {'x':456,'y':294, 'c':0,'d':0},{'x':496,'y':294,'c':0,'d':0},{'x':536,'y':294, 'c':0, 'd':0},{'x':576,'y':294, 'c':0,'d':0},{'x': 616, 'y':294, 'c':0,'d':0}, {'x':616,'y':334, 'c':0,'d':0},
              {'x':576,'y':334, 'c':0,'d':0},{'x':536,'y':334, 'c':0, 'd':0},{'x':496,'y':334, 'c':0,'d':0},{'x':456,'y':334, 'c':0,'d':0},{'x':416,'y':334, 'c':0, 'd':0},{'x':616, 'y':374, 'c':0,'d':0},
              {'x':576,'y':374, 'c':0,'d':0},{'x':536,'y':374, 'c':0, 'd':0},{'x':496,'y': 374, 'c':0,'d':0},{'x':456,'y':374, 'c':0,'d':0},{'x':416,'y':374, 'c':0, 'd':0}, {'x':377,'y':416, 'c':0,'d':0},
              {'x':377,'y': 456, 'c':0,'d':0},{'x':377,'y':496, 'c':0,'d':0},{'x':377,'y':536, 'c':0,'d':0},{'x':377,'y':576, 'c':0,'d':0},{'x':377,'y':614, 'c':0,'d':0},{'x': 337, 'y': 614, 'c':0,'d':0},
              {'x': 337,'y':576, 'c':0,'d':0}, {'x': 337, 'y': 536, 'c':0,'d':0}, {'x':337, 'y':496, 'c':0,'d':0}, {'x':337, 'y':456, 'c':0,'d':0},{'x': 337, 'y':416, 'c':0,'d':0}, {'x': 297, 'y': 614, 'c':0,'d':0},
              {'x': 297, 'y': 576, 'c':0,'d':0}, {'x': 297, 'y':536, 'c':0,'d':0}, {'x': 297, 'y':496, 'c':0,'d':0}, {'x': 297, 'y':456, 'c':0,'d':0},{'x': 297, 'y':416, 'c':0,'d':0}, {'x': 256, 'y':374, 'c':0,'d':0},
              {'x': 216, 'y':374, 'c':0,'d':0}, {'x': 176, 'y':374, 'c':0,'d':0}, {'x': 136, 'y':374, 'c':0,'d':0}, {'x': 96, 'y':374, 'c':0,'d':0},{'x': 56, 'y': 374, 'c':0,'d':0}, {'x':56,'y':334, 'c':0,'d':0},
              {'x': 96, 'y': 334, 'c':0,'d':0}, {'x': 136, 'y':334, 'c':0, 'd':0}, {'x': 176, 'y':334, 'c':0,'d':0}, {'x': 216, 'y':334, 'c':0,'d':0},{'x':256, 'y':334, 'c':0,'d':0}, {'x': 56, 'y':294, 'c':0, 'd':0}
              ]

	for p in range(4):
		screen.blit(textsurface, (720, 320))
		screen.blit(textsurface1, (850, 355))
		if(gm==0):
			if (my_player.color=='R'):
				COLOR1=COLOR_R
				COLOR2=COLOR_Y
				if(my_player.ptokenlist[p].getlocation()==-1):
					coins[p]['x']=R_I[p]['x']
					coins[p]['y']=R_I[p]['y']
				elif (my_player.ptokenlist[p].getlocation()==-2):
					coins[p]['x'] = M_F[p]['x']
					coins[p]['y'] = M_F[p]['y']
				else:
					coins[p]['x']=position[my_player.ptokenlist[p].getlocation()]['x']
					coins[p]['y']=position[my_player.ptokenlist[p].getlocation()]['y']
					position[my_player.ptokenlist[p].getlocation()]['c']+=1


				if(opp_player.ptokenlist[p].getlocation()==-1):
					coins_o[p]['x']=Y_I[p]['x']
					coins_o[p]['y']=Y_I[p]['y']
				elif(opp_player.ptokenlist[p].getlocation()==-2):
					coins_o[p]['x']=O_F[p]['x']
					coins_o[p]['y']=O_F[p]['y']
				else:
					coins_o[p]['x']=position[opp_player.ptokenlist[p].getlocation()]['x']
					coins_o[p]['y']=position[opp_player.ptokenlist[p].getlocation()]['y']
					position[opp_player.ptokenlist[p].getlocation()]['c']+=1
			else:
				COLOR1 = COLOR_Y
				COLOR2 = COLOR_R
				if (my_player.ptokenlist[p].getlocation() == -1):
					coins[p]['x'] = Y_I[p]['x']
					coins[p]['y'] = Y_I[p]['y']
				elif (my_player.ptokenlist[p].getlocation() == -2):
					coins[p]['x'] = O_F[p]['x']
					coins[p]['y'] = O_F[p]['y']
				else:
					coins[p]['x'] = position[my_player.ptokenlist[p].getlocation()]['x']
					coins[p]['y'] = position[my_player.ptokenlist[p].getlocation()]['y']
					position[my_player.ptokenlist[p].getlocation()]['c']+=1

				if (opp_player.ptokenlist[p].getlocation() == -1):
					coins_o[p]['x'] = R_I[p]['x']
					coins_o[p]['y'] = R_I[p]['y']
				elif (opp_player.ptokenlist[p].getlocation() == -2):
					coins_o[p]['x'] = M_F[p]['x']
					coins_o[p]['y'] = M_F[p]['y']
				else:
					coins_o[p]['x'] = position[opp_player.ptokenlist[p].getlocation()]['x']
					coins_o[p]['y'] = position[opp_player.ptokenlist[p].getlocation()]['y']
					position[opp_player.ptokenlist[p].getlocation()]['c']+=1
		else:
			if (my_player.color=='B'):
				COLOR1 = COLOR_B
				COLOR2 = COLOR_G
				if (my_player.ptokenlist[p].getlocation() == -1):
					coins[p]['x'] = B_I[p]['x']
					coins[p]['y'] = B_I[p]['y']
				elif (my_player.ptokenlist[p].getlocation() == -2):
					coins[p]['x'] = M_F[p]['x']
					coins[p]['y'] = M_F[p]['y']
				else:
					coins[p]['x'] = position[my_player.ptokenlist[p].getlocation()]['x']
					coins[p]['y'] = position[my_player.ptokenlist[p].getlocation()]['y']
					position[my_player.ptokenlist[p].getlocation()]['c']+=1


				if (opp_player.ptokenlist[p].getlocation() == -1):
					coins_o[p]['x'] = G_I[p]['x']
					coins_o[p]['y'] = G_I[p]['y']
				elif (opp_player.ptokenlist[p].getlocation() == -2):
					coins_o[p]['x'] = O_F[p]['x']
					coins_o[p]['y'] = O_F[p]['y']
				else:
					coins_o[p]['x'] = position[opp_player.ptokenlist[p].getlocation()]['x']
					coins_o[p]['y'] = position[opp_player.ptokenlist[p].getlocation()]['y']
					position[opp_player.ptokenlist[p].getlocation()]['c']+=1

			else:
				COLOR1 = COLOR_G
				COLOR2 = COLOR_B
				if (my_player.ptokenlist[p].getlocation() == -1):
					coins[p]['x'] = G_I[p]['x']
					coins[p]['y'] = G_I[p]['y']
				elif (my_player.ptokenlist[p].getlocation() == -2):
					coins[p]['x'] = O_F[p]['x']
					coins[p]['y'] = O_F[p]['y']
				else:
					coins[p]['x'] = position[my_player.ptokenlist[p].getlocation()]['x']
					coins[p]['y'] = position[my_player.ptokenlist[p].getlocation()]['y']
					position[my_player.ptokenlist[p].getlocation()]['c']+=1

				if (opp_player.ptokenlist[p].getlocation() == -1):
					coins_o[p]['x'] = B_I[p]['x']
					coins_o[p]['y'] = B_I[p]['y']
				elif (opp_player.ptokenlist[p].getlocation() == -2):
					coins_o[p]['x'] = M_F[p]['x']
					coins_o[p]['y'] = M_F[p]['y']
				else:
					coins_o[p]['x'] = position[opp_player.ptokenlist[p].getlocation()]['x']
					coins_o[p]['y'] = position[opp_player.ptokenlist[p].getlocation()]['y']
					position[opp_player.ptokenlist[p].getlocation()]['c']+=1

		textsurface5 = myfont.render("My Player ", False, (0, 0, 0))
		pygame.draw.ellipse(screen, COLOR1, [675,360, 35, 35], 0)
		screen.blit(textsurface5, (720, 360))
		textsurface6 = myfont.render("Opponent Player " , False, (0, 0, 0))
		pygame.draw.ellipse(screen, COLOR2, [675,400, 35, 35], 0)
		screen.blit(textsurface6, (720, 400))
		pygame.draw.ellipse(screen, COLOR1, [coins[p]['x'], coins[p]['y'], 35, 35], 0)
		pygame.draw.ellipse(screen, BLACK, [coins[p]['x'], coins[p]['y'], 35, 35], 2)
		pygame.draw.ellipse(screen, COLOR2, [coins_o[p]['x'], coins_o[p]['y'], 35, 35], 0)
		pygame.draw.ellipse(screen, BLACK, [coins_o[p]['x'], coins_o[p]['y'], 35, 35], 2)
		for i in range(position[my_player.ptokenlist[p].getlocation()]['c']):
			pygame.draw.ellipse(screen, COLOR1, [coins[p]['x']+(i*10),coins[p]['y'],35,35],0)
			pygame.draw.ellipse(screen, BLACK, [coins[p]['x'] + (i * 10), coins[p]['y'], 35, 35], 2)
		for i in range(position[opp_player.ptokenlist[p].getlocation()]['c']):
			pygame.draw.ellipse(screen, COLOR2, [coins_o[p]['x']+(i*10),coins_o[p]['y'],35,35],0)
			pygame.draw.ellipse(screen, BLACK, [coins_o[p]['x'] + (i * 10), coins_o[p]['y'], 35, 35], 2)

	pygame.display.update()
	time.sleep(1)
	pygame.display.flip()
	clocktime.tick(10)





# set token variables like color,id,location
class Token:
	counter = 0
	color = ''
	id = 0
	location = 0

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
	win_pieces = 0  # number of token reached passed the home lane i;e out of the board

	out_pieces = 0  # number of pieces out of the home state

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



tokenID = 0



if gm == 0:

	color = ['R', 'Y']

else:

	color = ['B', 'G']

tokenlist = []

for i in range(4):
	tokenlist.append(Token(color[pid - 1], i, -1)) # -1 indicates that token is in home. create object for each token
tokenlist1 = []

for i in range(4):
	tokenlist1.append(Token(color[2-pid], i, -1))

my_player = Player(pid, color[pid - 1], tokenlist)  # object of player 1

opp_player = Player(3 - pid, color[2 - pid], tokenlist1)  # object of player 1

# print(my_player.haswon())



startStates = {'R': 0, 'G': 18, 'Y': 36, 'B': 54}
startHomeLane = {'R': 66, 'G': 12, 'Y': 30, 'B': 48}
stopStates = {'R': 70, 'G': 16, 'Y': 34, 'B': 52}
inside = [0, 1, 2, 3]

outside = []

Board = []

Board.append(Cell("W", True, False, True))  # 0 starts with red start cell

for i in range(1, 8, 1):  # white color

	Board.append(Cell("W", False, False, False))

Board.append(Cell("W", True, False, False))  # green safe state

for i in range(9, 12, 1):
	Board.append(Cell("W", False, False, False))

for i in range(12, 17, 1):  # home lane of green

	Board.append(Cell("G", True, True, False))

Board.append(Cell("W", False, False, False))

Board.append(Cell("W", True, False, True))  # start state of green

for i in range(19, 26, 1):  # white between green start and yellow safe

	Board.append(Cell("W", False, False, False))

Board.append(Cell("W", True, False, False))  # safe state of yellow

for i in range(27, 30, 1):  # white of yellow

	Board.append(Cell("W", False, False, False))

for i in range(30, 35, 1):  # home lane of yellow

	Board.append(Cell("Y", True, True, False))

Board.append(Cell("W", False, False, False))

Board.append(Cell("W", True, False, True))  # start state of yellow

for i in range(37, 44, 1):  # white between yellow start and blue safe

	Board.append(Cell("W", False, False, False))

Board.append(Cell("W", True, False, False))  # safe state of blue

for i in range(45, 48, 1):  # white

	Board.append(Cell("W", False, False, False))

for i in range(48, 53, 1):  # home lane of blue

	Board.append(Cell("B", True, True, False))

Board.append(Cell("W", False, False, False))

Board.append(Cell("W", True, False, True))  # start state of blue

for i in range(55, 62, 1):  # white between blue start and red safe

	Board.append(Cell("W", False, False, False))

Board.append(Cell("W", True, False, False))  # safe state of red

for i in range(63, 66, 1):  # white

	Board.append(Cell("W", False, False, False))

for i in range(66, 71, 1):  # home lane of red

	Board.append(Cell("R", True, True, False))

Board.append(Cell("W", False, False, False))


# print(Board)

# for item in Board:

# print(item.color, item.home_lane_flag)







# update board and return "Invalid" if not possible

def updateboard(token_no, dice_value):
	token_pos = (my_player.ptokenlist[token_no].location + dice_value)%72

	my_player.ptokenlist[token_no].counter += dice_value

	if (my_player.ptokenlist[token_no].color != Board[token_pos].color) and (
		Board[token_pos].color != "W"):  # checks if it enters into diff color homelane

		token_pos = (token_pos + 5) % 72

	'''if(my_player.ptokenlist[token_no].counter==57)
	
		   set location of token to -2 implies it has reached finish state '''

	if (my_player.ptokenlist[token_no].counter > 56):  # change 33 to correct value of toatal moves possible
		my_player.ptokenlist[token_no].counter -= dice_value  # token will not make move, counter remain unchanged
		return "Invalid"

	if (Board[token_pos].safe_state_flag == True):
		my_player.ptokenlist[token_no].location = token_pos

	for i in range(4):

		if my_player.ptokenlist[i].location == token_pos:
			return "Invalid"

	for i in range(4):

		if opp_player.ptokenlist[i].location == token_pos:
			opp_player.ptokenlist[i].location = -1

	my_player.ptokenlist[token_no].setlocation(token_pos)

	return str(token_no)


# method to check -given a token,token_loc+dice enters into home lane of diff color,and then return the correct  index at which the token should be set
def invalidHomeLane(t, dice_value):
	# gets the location and color of this token
	t_color = t.color
	t_loc = t.getlocation()
	#if token located at startstate of any home lene -1 and dice_value = 6 , do not enter home lane
	if((t_loc== 11 or t_loc== 29 or t_loc== 47 or t_loc== 65 ) and(dice_value == 6) ):
		return (t_loc + dice_value + 5) % 72
	# get the color of the cell after loc+dice_value
	if (Board[(t_loc + dice_value)%72].home_lane_flag == True):  # check whether after addition its a homeLane cell
		if (Board[(t_loc + dice_value)%72].color != t_color):  # if the lane is of different color
			return (t_loc + dice_value + 5)%72
		else:  # if its of the same color
			return (t_loc + dice_value)%72
	else:
		return (t_loc + dice_value)%72


# returns true if the token t has reached finish state
def check_finish_state(t):
	if (t.counter == 57):
		t.setlocation(-2)

		return True
	else:
		return False


# algo starts here..................................


def valid_move (t,dice_value):

	temp_loc = invalidHomeLane(t,dice_value)
	if(Board[temp_loc].safe_state_flag == False):
		for i in range(4):
			if (i != t.id):
				if(temp_loc == my_player.ptokenlist[i].getlocation() ):
					return False
	return True

#returns list of token of my_player which are inside home lane
def inHomeLane(my_player):

	l =[]
	for i in range(4):
		if(my_player.ptokenlist[i].getlocation()!=-2 and my_player.ptokenlist[i].getlocation()!=-1 and my_player.ptokenlist[i].color == Board[my_player.ptokenlist[i].getlocation()].color):
			l.append(i)
	return l

#returns token which is located in range(1,6) ahead of opposite color token
def defensive_move(my_player,dice_value):
	sys.stderr.write('@@@-GOING IN DEFENSIVE@@@--'+'\n')
	tk =None
	for i in range(4):
		my_loc = my_player.ptokenlist[i].getlocation()
		if (my_loc == -2 or my_loc == -1):
			continue
		if Board[my_loc].safe_state_flag == True:
			continue
		for j in range(6):
			new_loc = my_loc - j
			if (new_loc < 0):
				new_loc = new_loc + 72
			if(Board[new_loc].home_lane_flag == True):
				new_loc = new_loc -5
			for k in range(4):
				opp_loc =opp_player.ptokenlist[k].getlocation()
				if (opp_loc == new_loc):
					if valid_move(my_player.ptokenlist[i], dice_value):
						return my_player.ptokenlist[i]
	return tk
#returns token which can knock off other's token if mylocation+dice=other's token location
def aggresive_move(my_player,dice_value):
	sys.stderr.write('?????   GOING IN Aggressive   ????' + '\n')
	for i in range(4):
		my_loc=my_player.ptokenlist[i].getlocation()
		if (my_loc == -2 or my_loc == -1 or Board[my_loc].home_lane_flag==True):
			continue
		for j in range(4):
			correct_ind=invalidHomeLane(my_player.ptokenlist[i],dice_value) #returns the correct index of mytoken if required
			#checks if the other's token is not in safe state
			if((Board[correct_ind].safe_state_flag==False) and (correct_ind==opp_player.ptokenlist[j].getlocation())):
				return my_player.ptokenlist[i]
	return None





# TODO
# returns token which is closer to homelane
def getFastMovePiece(my_player,dice_value):
	sys.stderr.write('$$$   GOING IN Fast move $$$$$' + '\n')
	min_diff = 100
	pc =None
	for i in range(4):
		l = my_player.ptokenlist[i].getlocation()
		if(my_player.ptokenlist[i].counter+dice_value > 57):
			continue
		if (l != -1 and l != -2 and (my_player.ptokenlist[i].color != Board[my_player.ptokenlist[i].getlocation()].color)):  # do this only if the piece is out or not and not in home lane
			if valid_move(my_player.ptokenlist[i],dice_value):
				diff = (startHomeLane[my_player.color] - l) % 72
				if (diff < min_diff):
					min_diff = diff
					pc = my_player.ptokenlist[i]
	return pc


def getBestPossibleMove(my_player, opp_player, dice_value):
#Priority Order -First try if any in home lane-Defensive-Aggressive-Fast Move

	#Checks if any token is inside home lane
	pc = None
	# temp_index=invalidHomeLane(t, dice_value)       #stores the
	hl_pc_list = inHomeLane(my_player)  #returns list of token which are inside home lane
	max=0
	tk =-1
	if (len(hl_pc_list)>0):
		for i in (hl_pc_list):
			if (my_player.ptokenlist[i].counter+dice_value == 57):
				return my_player.ptokenlist[i]  #returns token which finishes
			else:
				temp_loc = my_player.ptokenlist[i].getlocation()+dice_value
				if (temp_loc<startHomeLane[my_player.color]+5):
					if(max <temp_loc):
						tk = i #stores token id which is closest to finish state
						max =temp_loc     #loc closest to finish state
		if(tk != -1):
			if (my_player.ptokenlist[tk].counter+dice_value < 57):
				return my_player.ptokenlist[tk] #returns token which is to be moved

	#2nd-check if I need to defend from opponent
	pc=defensive_move(my_player,dice_value)
	#3rd-check if i can knock off opponent's token
	if (pc ==None):
		pc=aggresive_move(my_player,dice_value)

	#Otherwise move the one closest to finish
	if(pc == None):
		pc = getFastMovePiece(my_player,dice_value)

	sys.stderr.write('PC @@@----------------' + str(pc)+'\n')
	return pc


# def validIndex(t, dice_value, Board):


alive = True
size = (1000, 1000)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLOR_R = (141, 23, 23)
COLOR_B = (0, 203, 210)
COLOR_G = (9, 129, 0)
COLOR_Y = (247, 148, 0)
coins = [{'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}]
coins_o = [{'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Assignment-2 :Ludo Bot" + "--Player No.--" + str(pid))

# Used to manage how fast the screen updates
clocktime = pygame.time.Clock()

while alive:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			pygame.quit()
	REPEAT = False
	init_flag = False
	flag_NA = 0


	while (not my_player.haswon()) and (not opp_player.haswon()):

		if REPEAT == False:

			#sys.stderr.write('<IN WHILE>\n')

			my_color = my_player.color  # returns the color of this player
			if pid == 2 and init_flag == False:
				init_flag = True
				dice = sys.stdin.readline().strip()
				sys.stderr.write('pid 2 PRINT DICE: ' + dice + '\n')
				move = sys.stdin.readline().strip()

				move_opp_list1 = move.split('<next>')
				for move2 in move_opp_list1:

					if ((move2[1] == '0') or (move2[1] == '1') or (move2[1] == '2') or (move2[1] == '3')):
						loc = (opp_player.ptokenlist[ord(move2[1]) - 48].getlocation() + ord(move2[3]) - 48) % 72
						if (loc == stopStates[opp_player.color] + 1):
							opp_player.ptokenlist[ord(move2[1]) - 48].setlocation(-2)
						else:
							if (opp_player.ptokenlist[ord(move2[1]) - 48].getlocation() == -1):
								opp_player.ptokenlist[ord(move2[1]) - 48].setlocation(startStates[opp_player.color])
							else:
								if (opp_player.ptokenlist[ord(move2[1]) - 48].color != Board[loc].color) and (
									Board[loc].color != "W"):
									opp_player.ptokenlist[ord(move2[1]) - 48].setlocation((loc + 5) % 72)
								else:
									opp_player.ptokenlist[ord(move2[1]) - 48].setlocation((loc) % 72)
				sys.stderr.write('pid 2 PRINT MOVE: ' + move + '\n')



			# THis player's turn to

			sys.stdout.write('<THROW>\n')
			try:
				sys.stdout.flush()
			except:
				sys.stderr.write('i think game has finished')
				sys.exit(0)
			move_list = []
			dice = sys.stdin.readline().strip()
			sys.stderr.write('my player received dice value as>>>'+dice)
			dice_value_list = []
			#sys.stderr.write('read from dice string ' + dice + '\n')
			i = 2
			#sys.stderr.write('read from dice string ')
			if 'SIXES' in dice:
				sys.stdout.write('NA\n')
				sys.stdout.flush()

			else:
				while i < len(dice.split(' ')):
					dice_value_list.append(int(dice.split(' ')[i]))  # returns the numbers on dice
					#sys.stderr.write('::' + str(dice.split(' ')[i]) + '\n')
					i += 1
				for dice_value in dice_value_list:


					if (my_player.out_pieces == 0):  # all the 4 tokens are inside home state

						if (dice_value == 6 or dice_value == 1):

							my_player.ptokenlist[0].setlocation(
								startStates[my_color])  # set the token to start position+dicevalue

							my_player.out_pieces = my_player.out_pieces + 1

							my_player.ptokenlist[0].counter += 1

							#sys.stderr.write('move sent: ' + str(dice_value) + '\n')
							move_list.append(my_color + str(0) + '_' + str(dice_value))

							# sys.stdout.write(my_color+str(0)+'_'+str(dice_value)+'\n')

							# update board



						else:
							move_list.append('NA')

							# sys.stdout.write('NA\n')

					else:

						if (dice_value == 6 or dice_value == 1) and (my_player.out_pieces != 4):

							for i in range(4):

								if (my_player.ptokenlist[i].location == -1):
									my_player.ptokenlist[i].setlocation(startStates[my_color] )

									my_player.out_pieces = my_player.out_pieces + 1

									my_player.ptokenlist[i].counter += 1
									move_list.append(my_color + str(i) + '_' + str(dice_value))
									break

									# sys.stdout.write(my_color + str(i) +'_'+ str(dice_value) + '\n')



						else:  # if atleast 1 token is out of home state

							t = getBestPossibleMove(my_player, opp_player,
													dice_value)  # returns the token  which should be moved

							if (t == None):
								move_list.append('NA')

							else:
								ind = invalidHomeLane(t, dice_value)  # returns the valid index at which t is to be placed


								my_player.ptokenlist[t.id].setlocation(ind)  # set the token to start position+dicevalue
								my_player.ptokenlist[t.id].counter += dice_value
								# check if "t" cuts other player token
								for oppid in range(4):
									opp_loc =opp_player.ptokenlist[oppid].getlocation()
									if(ind == opp_loc and opp_loc != -2 and Board[ind].safe_state_flag == False and opp_loc !=-1):
										opp_player.ptokenlist[oppid].setlocation(-1)


								if(t.counter == 57):
									my_player.win_pieces += 1
									my_player.ptokenlist[t.id].setlocation(-2)

								move_list.append(my_color + str(t.id) + '_' + str(dice_value))

				first = 1
				str1 = ''
				for i in move_list:
					if(i!='NA'):
						if (first == 1):
							str1 = str1 + str(i)
							first = 0
						else:
							str1 = str1 + str('<next>')
							str1 = str1 + str(i)
				try:
					if(str1 == ''):
						sys.stdout.write('NA\n')
					else :
						sys.stdout.write(str1+'\n')


					sys.stdout.flush()
				except:
					sys.stderr.write('i think game has finished')
					sys.exit(0)
					break
				sys.stderr.write("my token pos are>>>" + str(my_player.ptokenlist[0].getlocation()) + '>>>' + str(
					my_player.ptokenlist[1].getlocation()) + '>>>' + str(
					my_player.ptokenlist[2].getlocation()) + '>>>' + str(my_player.ptokenlist[3].getlocation()) + '\n')
				sys.stderr.write("my token counter are:::" + str(my_player.ptokenlist[0].counter) + ">>>" + str(
					my_player.ptokenlist[1].counter) + ">>>" + str(my_player.ptokenlist[2].counter) + ">>>" + str(
					my_player.ptokenlist[3].counter) + "\n")
			graphics(my_player,opp_player,gm,0)



		else:
			REPEAT=False

		dice = sys.stdin.readline().strip()
		sys.stderr.write('bot_msg_dice:------------------------- ' + dice + '\n')


		if dice != 'REPEAT':

			#sys.stderr.write('bot_msg_dice: ' + dice + '\n')
			try:
				move = sys.stdin.readline().strip()


				move_opp_list = move.split('<next>')
				for move1 in move_opp_list:

					if ((move1[1] =='0') or (move1[1] =='1') or (move1[1] =='2') or (move1[1] =='3')):
						loc = (opp_player.ptokenlist[ord(move1[1])-48].getlocation() + ord(move1[3])-48)%72
						if (loc == stopStates[opp_player.color]+1):
							opp_player.ptokenlist[ord(move1[1])-48].setlocation(-2)
						#if opp token was at starthome lane -1 and dice value =6 add 5
						elif((loc== 17 or loc== 35 or loc== 53 or loc== 71 ) and( ord(move1[3])-48== 6) ):
							opp_player.ptokenlist[ord(move1[1]) - 48].setlocation((loc + 5) % 72)

						else:

							if (opp_player.ptokenlist[ord(move1[1])-48].getlocation() == -1):
									opp_player.ptokenlist[ord(move1[1])-48].setlocation(startStates[opp_player.color])
							else:
								if (opp_player.ptokenlist[ord(move1[1])-48].color != Board[loc].color) and (Board[loc].color != "W"):
									opp_player.ptokenlist[ord(move1[1])-48].setlocation((loc + 5) % 72)
								else:
									opp_player.ptokenlist[ord(move1[1]) - 48].setlocation((loc) % 72)
						loc = opp_player.ptokenlist[ord(move1[1])-48].getlocation()
						for myid in range(4):
							if(my_player.ptokenlist[myid].getlocation() == loc and loc != -2 and Board[loc].safe_state_flag == False):
								my_player.ptokenlist[myid].setlocation(-1)
								my_player.ptokenlist[myid].counter = 0
								my_player.out_pieces = my_player.out_pieces -1
				sys.stderr.write("opp token pos are>>>" + str(opp_player.ptokenlist[0].getlocation()) +'>>>'+ str(
						opp_player.ptokenlist[1].getlocation()) +'>>>'+ str(opp_player.ptokenlist[2].getlocation())+'>>>' + str(
						opp_player.ptokenlist[3].getlocation()) + '\n')
				if move.strip().split('<next>')[-1] == 'REPEAT':
					REPEAT = True

				graphics(my_player, opp_player, gm,0)
			except:
				graphics(my_player, opp_player, gm,1)


