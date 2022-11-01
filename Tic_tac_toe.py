#refered Code_with_harry tic_tac_toe project


def sum(a,b,c):
    return a+b+c


def printBoard(xs,zs):                                                           #function to print the board
    _0='X' if xs[0] else ('O' if zs[0] else 0)
    _1='X' if xs[1] else ('O' if zs[1] else 1)
    _2='X' if xs[2] else ('O' if zs[2] else 2)
    _3='X' if xs[3] else ('O' if zs[3] else 3)
    _4='X' if xs[4] else ('O' if zs[4] else 4)
    _5='X' if xs[5] else ('O' if zs[5] else 5)
    _6='X' if xs[6] else ('O' if zs[6] else 6)
    _7='X' if xs[7] else ('O' if zs[7] else 7)
    _8='X' if xs[8] else ('O' if zs[8] else 8)
    print(f" {_0}| {_1} | {_2} ")
    print(f"--|---|---")
    print(f"{_3} | {_4} | {_5} ")
    print(f"--|---|---")
    print(f"{_6} | {_7} | {_8} ")


def checkWin(xs,zs):                                                             #function to check who is the winner
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xs[win[0]],xs[win[1]],xs[win[2]])==3):
            print("X Won the Match")
            return 1
        if(sum(zs[win[0]],zs[win[1]],zs[win[2]])==3):
            print("O Won the Match")
            return 0
    return -1


if __name__=="__main__":
    xs=[0,0,0,0,0,0,0,0,0]
    zs=[0,0,0,0,0,0,0,0,0]
    turn=1                                                                       #1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    chance=0
    while(chance<=9):                                                            #Will termenate when chance=10
        printBoard(xs,zs)                                                        #To print the board

        cwin=checkWin(xs,zs)
        if(cwin!=-1 or chance==9):                                               #When X or O wins OR when the the total chance=9 the loop terminates
            print("Match Over")
            break

        if(turn==1):
            print("X's Chance")
            val=int(input("Please enter a value:"))
            xs[val]=1

        else:
             print("O's Chance")
             val=int(input("Please enter a value:"))
             zs[val]=1

        chance+=1                                                                #Incrementing total no. of chances
        turn=1- turn                                                             #giving alternative chance to X and O
