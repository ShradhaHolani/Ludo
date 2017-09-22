# TODO -to mark home lane in safe state or not

import sys
# set token variables like color,id,location
import self as self


class Token:

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

    def __init__(self, color, safe_state_flag, home_lane_flag, start_state_flag):
        # self.index = index      this not required because it can be accessed using list index only
        self.color = color  # assigned to special cell otherwise "W"
        self.safe_flag_flag = safe_state_flag
        self.home_lane_flag = home_lane_flag
        self.start_start_flag = start_state_flag

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
    tokenlist.append(Token("B", i, -1))    # -1 indicates that token is in home. create object for each token
my_player = Player(pid, color[pid-1], tokenlist)  # object of player 1
opp_player = Player(3-pid, color[2-pid], tokenlist)  # object of player 1
print(my_player.haswon())

startStates = {'R':0,'G':18,'Y':36,'B': 54}


Board = []
Board.append(Cell("R", True, False, True))  # 0 starts with red start cell

for i in range(1, 8, 1):  # white color
    Board.append(Cell("W", False, False, False))

Board.append(Cell("G", True, False, False))  # green safe state

for i in range(9, 12, 1):
    Board.append(Cell("W", False, False, False))

for i in range(12, 17, 1):  # home lane of green
    Board.append(Cell("G", False, True, False))

Board.append(Cell("W", False, False, False))
Board.append(Cell("G", True, False, True))  # start state of green

for i in range(19, 26, 1):  # white between green start and yellow safe
    Board.append(Cell("W", False, False, False))

Board.append(Cell("Y", True, False, False))  # safe state of yellow

for i in range(27, 30, 1):  # white of yellow
    Board.append(Cell("W", False, False, False))

for i in range(30, 35, 1):  # home lane of yellow
    Board.append(Cell("Y", False, True, False))

Board.append(Cell("W", False, False, False))
Board.append(Cell("Y", True, False, True))  # start state of yellow

for i in range(37, 44, 1):  # white between yellow start and blue safe
    Board.append(Cell("W", False, False, False))

Board.append(Cell("B", True, False, False))  # safe state of blue

for i in range(45, 48, 1):  # white
    Board.append(Cell("W", False, False, False))

for i in range(48, 53, 1):  # home lane of blue
    Board.append(Cell("B", False, True, False))

Board.append(Cell("W", False, False, False))
Board.append(Cell("B", True, False, True))  # start state of blue

for i in range(55, 62, 1):  # white between blue start and red safe
    Board.append(Cell("W", False, False, False))

Board.append(Cell("R", True, False, False))  # safe state of red

for i in range(63, 66, 1):  # white
    Board.append(Cell("W", False, False, False))

for i in range(66, 71, 1):  # home lane of red
    Board.append(Cell("R", False, True, False))

Board.append(Cell("W", False, False, False))

#print(Board)
for item in Board:
    print(item.color, item.home_lane_flag)

#algo starts here..................................

#TODO
#def getBestPossibleMove(my_player , opp_player, dice_value, b):
#def validIndex(t, dice_value, Board):


REPEAT = False
while (not my_player.haswon()) and (not opp_player.haswon()):
    if REPEAT == False:
        my_color = my_player.color  #returns the color of this player
        sys.stdout.write('<THROW>\n')
        sys.stdout.flush()

        dice = sys.stdin.readline().strip()
        dice_value = int(tl.split(' ')[2])     #returns the number on dice
        if(my_player.out_pieces == 0):      #all the 4 tokens are inside home state
            if(dice_value == 6 or dice_value == 1):
                my_player.ptokenlist[0].setlocation(startStates[my_color]+dice_value)       #set the token to start position+dicevalue

                sys.stdout.write(my_color+str(0)+str(dice_value)+'\n')
                #update board
             #else what to send to server??

        else:      #if atleast 1 token is out of home state
            t=getBestPossibleMove(my_player,opp_player,dice_value,Board)     #returns the token  which should be moved
            ind=validIndex(t,dice_value,Board)          #returns the valid index at which t is to be placed
            my_player.ptokenlist[t.id].setlocation(ind)  # set the token to start position+dicevalue
            sys.stdout.write(my_color + str(t.id) + str(dice_value) + '\n')
            # update board

    sys.stdout.write(color[pid - 1] + str(tokenID) + '_1\n')
    sys.stdout.flush()

counter += 1




