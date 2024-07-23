import os
import time

def Yellow():
    print("\033[1;33m",end="")

def Sky_blue():
    print("\033[1;36m",end="")

def red():
    print("\033[1;35m",end="")

def defcol():
    print("\033[0m",end="")

def printf(str):
    print(str,end="")

def s_display():
    printf("\033[1;34m Loading \033[0m")
    for x in range(10):
        time.sleep(0.03)
        printf("\033[1;34m_\033[0m")
        time.sleep(0.03)
        printf("\033[1;35m_\033[0m")
        time.sleep(0.03)
        printf("\033[1;31m_\033[0m")
        time.sleep(0.03)
        printf("\033[1;32m_\033[0m")
    print()

def e_display():
    for x in range(5):
        os.system("cls")
        for m in range(x):
            print()
        print("\t\t\t\t\t\t\t\033[1;36m<<<<QUITING GAME>>>\033[0m")
        time.sleep(0.4)
        os.system("cls")

def p1_win():
    time.sleep(2)
    for x in range(8):
        os.system("cls")
        for m in range(x):
            print()
        print("\t\t\t\t\t\t\t\033[1;32m<<<<PLAYER 1 WIN!!!>>>>\033[0m")
        time.sleep(0.4)
        os.system("cls")

def p2_win():
    time.sleep(2)
    for x in range(8):
        os.system("cls")
        for m in range(x):
            print()
        print("\t\t\t\t\t\t\t\033[1;32m<<<<PLAYER 2 WIN!!!>>>>\033[0m")
        time.sleep(0.4)
        os.system("cls")

def Match_draw():
    time.sleep(2)
    for x in range(8):
        os.system("cls")
        for m in range(x):
            print()
        print("\t\t\t\t\t\t\t\033[1;32m<<<< Match Draw !!!>>>>\033[0m")
        time.sleep(0.4)
        os.system("cls")

def gameover():
    os.system("cls");
    s_display();
    os.system("cls");
    printf("\t\t\t\t\t\t\033[1;33mO\033[0m-\033[1;35mGAME\033[0m\033[1;31m OVER\033[0m-\033[1;33mX\033[0m\n");

    printf("\n\n")
    printf("\t\t\t\t\t\t\033[1;33m 1.Play Again\033[0m\n")
    print("\t\t\t\t\t\t\033[1;33m 2.Quit Game\033[0m\n")

def condition_checks(game):
    if game[0]=='O'and game[1]=='O' and game[2]=='O':
        return 1
    elif game[3]=='O'and game[4]=='O' and game[5]=='O':
        return 1
    elif game[6]=='O'and game[7]=='O' and game[8]=='O':
        return 1
    elif game[3]=='O'and game[0]=='O' and game[6]=='O':
        return 1
    elif game[1]=='O'and game[4]=='O' and game[7]=='O':
        return 1
    elif game[2]=='O'and game[8]=='O' and game[5]=='O':
        return 1
    elif game[0]=='O'and game[4]=='O' and game[8]=='O':
        return 1
    elif game[2]=='O'and game[6]=='O' and game[4]=='O':
        return 1  
    elif game[0]=='X'and game[1]=='X' and game[2]=='X':
        return 2
    elif game[3]=='X'and game[4]=='X' and game[5]=='X':
        return 2
    elif game[6]=='X'and game[7]=='X' and game[8]=='X':
        return 2
    elif game[3]=='X'and game[0]=='X' and game[6]=='X':
        return 2
    elif game[1]=='X'and game[4]=='X' and game[7]=='X':
        return 2
    elif game[2]=='X'and game[8]=='X' and game[5]=='X':
        return 2
    elif game[0]=='X'and game[4]=='X' and game[8]=='X':
        return 2
    elif game[2]=='X'and game[6]=='X' and game[4]=='X':
        return 2
    elif game[0]!=1 and game[1]!=2 and game[2]!=3 and game[3]!=4 and game[4]!=5 and game[5]!=6 and game[6]!=7 and game[7]!=8 and game[8]!=9:
        return 3
    else:
        return 0
    
    

def playgame():
    game=[1,2,3,4,5,6,7,8,9]
    while(1):
        os.system("cls")
        i=0
        for x in range(3):
            for y in range(3):
                if game[i]=='O':
                    Yellow()
                    print(game[i]," ",end="")
                    defcol()
                elif game[i]=='X':
                    Sky_blue()
                    print(game[i]," ",end="")
                    defcol()
                else:
                    print(game[i]," ",end="")
                i+=1
            print()
        # p1_in = int(input("Player 1 :Select the box where you want to give input(1 to 9) :"))
        p1_in = int(input("\033[1;32m Player 1 :Select the box[O] where you want to give input(1 to 9) : \033[0m"))

        for i in range(9):
            if p1_in==(game[i]):
                game[i]='O'
        check = condition_checks(game)
        if check==1:
            os.system("cls")
            i=0
            for x in range(3):
                for y in range(3):
                    if game[i]=='O':
                        Yellow()
                        print(game[i]," ",end="")
                        defcol()
                    elif game[i]=='X':
                        Sky_blue()
                        print(game[i]," ",end="")
                        defcol()
                    else:
                        print(game[i]," ",end="")
                    i+=1
                print()
            p1_win()
            break
        elif check==2:
            os.system("cls")
            i=0
            for x in range(3):
                for y in range(3):
                    if game[i]=='O':
                        Yellow()
                        print(game[i]," ",end="")
                        defcol()
                    elif game[i]=='X':
                        Sky_blue()
                        print(game[i]," ",end="")
                        defcol()
                    else:
                        print(game[i]," ",end="")
                    i+=1
                print()
            p2_win()
            break
        elif check==3:
            os.system("cls")
            i=0
            for x in range(3):
                for y in range(3):
                    if game[i]=='O':
                        Yellow()
                        print(game[i]," ",end="")
                        defcol()
                    elif game[i]=='X':
                        Sky_blue()
                        print(game[i]," ",end="")
                        defcol()
                    else:
                        print(game[i]," ",end="")
                    i+=1
                print()
            Match_draw()
            break
        os.system("cls")
        # game=[1,2,3,4,5,6,7,8,9]
        i=0
        for x in range(3):
            for y in range(3):
                if game[i]=='O':
                    Yellow()
                    print(game[i]," ",end="")
                    defcol()
                elif game[i]=='X':
                    Sky_blue()
                    print(game[i]," ",end="")
                    defcol()
                else:
                    print(game[i]," ",end="")
                i+=1
            print()
        # p2_in = int(input("Player 2 :Select the box where you want to give input(1 to 9) :"))
        p2_in = int(input("\033[1;36m Player 2 :Select the box[X] where you want to give input(1 to 9) : \033[0m"))
        
        for i in range(9):
            if p2_in==(game[i]):
                game[i]='X'
        check = condition_checks(game)
        if check==1:
            os.system("cls")
            i=0
            for x in range(3):
                for y in range(3):
                    if game[i]=='O':
                        Yellow()
                        print(game[i]," ",end="")
                        defcol()
                    elif game[i]=='X':
                        Sky_blue()
                        print(game[i]," ",end="")
                        defcol()
                    else:
                        print(game[i]," ",end="")
                    i+=1
                print()
            p1_win()
            break
        elif check==2:
            os.system("cls")
            i=0
            for x in range(3):
                for y in range(3):
                    if game[i]=='O':
                        Yellow()
                        print(game[i]," ",end="")
                        defcol()
                    elif game[i]=='X':
                        Sky_blue()
                        print(game[i]," ",end="")
                        defcol()
                    else:
                        print(game[i]," ",end="")
                    i+=1
                print()
            p2_win()
            break
        elif check==3:
            os.system("cls")
            i=0
            for x in range(3):
                for y in range(3):
                    if game[i]=='O':
                        Yellow()
                        print(game[i]," ",end="")
                        defcol()
                    elif game[i]=='X':
                        Sky_blue()
                        print(game[i]," ",end="")
                        defcol()
                    else:
                        print(game[i]," ",end="")
                    i+=1
                print()
            Match_draw()
            break
        # time.sleep(1)
    # pass

# game=['1','2','3','4','5','6','7','8','9']
game=[1,2,3,4,5,6,7,8,9]
os.system("cls")
s_display()
os.system("cls")
printf("\t\t\t\t\t\t\033[1;33mO\033[0m-\033[1;35mTIC\033[0m-\033[1;31mTAC\033[0m-\033[1;34mTOE\033[0m-\033[1;33mX\033[0m\n")
printf("\n\n")
printf("\t\t\t\t\t\t\033[1;33m  1.Play Game\033[0m\n")
printf("\t\t\t\t\t\t\033[1;33m  2.Quit Game\033[0m\n")
while(1):
    ch = int(input())
    if ch==1:
        playgame()
        os.system("cls")
        gameover()
    elif ch==2:
        e_display()
        exit()
        