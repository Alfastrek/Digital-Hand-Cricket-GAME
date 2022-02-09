# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 12:52:59 2022

@author: ALFASTREK
"""
#HAND CRICKET
import random
import pandas as pd
print('Hello, Welcome to the Hand Cricket Game!')
gamepl=['BAT','BALL']
poss=(0,1,2,3,4,5,6) #Runs Allowed 
userrecord=[] #TO maintain indiv run record
comprecord=[]
Players=int(input("Enter Total Players on each side:"))
User_team=[]
Comp_team=[("ROBO-",i+1) for i in range(Players)]
for h in range (Players): #formation of User Team
    names=input("Enter Name of the Players:")
    User_team.append(names)
data={"USER TEAM":User_team,
      "COMP TEAM":Comp_team}
sr_no=[i+1 for i in range(Players)]
df=pd.DataFrame(data, index=[sr_no])
print("Overview of the TEAMS:",'\n',df)


def oddevengame():
    global oeresult,oddeve
    oddeve=input("\nChoose ODD or EVEN:")
    while oddeve=="ODD" or oddeve=="EVEN":
        oeno=int(input("Choose your no (within 0 to 6):")) #input for odd even game
        rand=random.choice(poss)
        oeresult= oeno + rand #total result of oddevengame
        print("Computer Chooses:", rand,
              "\nAnd the Total makes:", oeresult)
        break
    else:
        return 'Repeat again'
        oddevengame()

def batting():
    global userteamtotalruns
    ballno=1 #In order to keep the count for balls
    user_teamno=0 #In order to display current player
    userteamtotalruns=0
    userscore=0
    while Players>0:
        print("\nBall no:",ballno,"For Player:",User_team[user_teamno])
        runs=int(input('Play Runs:'))
        rand1=random.choice(poss)
        print("Computer Choses:",rand1)
        if runs not in poss: #extra precaution to maintain fair play
            print("Sorry You are Out!, Only 0 to 6 is the range for runs")
            break
        elif (rand1==runs):
            print(User_team[user_teamno],"is OUT!\n")
            print("Your Total Runs after batting are:" ,userscore)
            ballno=1 #reset the ball serial no.
            user_teamno+=1 #To switch to the next player
            if (user_teamno==Players):
                break
            else:
                pass
            userteamtotalruns+=userscore #To maintain Team run record
            x=userscore
            userrecord.append(x)
            userscore=0 #To reset variable for counting runs for the next player
        else:
            userscore+=runs
            ballno+=1
            userteamtotalruns+=userscore
            print("Your Runs after this round are:",userscore)
    return "Your Team Total Runs after batting are:" , userteamtotalruns

def balling():
    global compteamtotalruns
    compscore=0
    ballno=1
    comp_teamno=0
    compteamtotalruns=0
    while Players>0:
        print("\nBall no:",ballno,"For Player:",Comp_team[comp_teamno])
        rand2=random.choice(poss)
        balls=int(input("Enter your Balling input:"))
        print(Comp_team[comp_teamno],"Choses:",rand2)
        if balls not in poss: #extra precaution to maintain fair play
            ("Sorry You are Out!, Only 0 to 6 is the range for runs")
            break
        elif (rand2!=balls):
            compscore=rand2+compscore
            print("Computer Runs after this ball is:",compscore)
            ballno+=1
            break
        else:
            print("You Win!"
                  "\nThe",Comp_team[comp_teamno],"is OUT!")
            ballno=1 #reset the ball serial no.
            comp_teamno+=1 #To switch to the next player.
            if (comp_teamno==Players):
                break
            else:
                pass
            compteamtotalruns+=compscore #To maintain Comp team total record
            print("Computer after this round are:",compscore)
            y=compscore
            comprecord.append(y)
            compscore=0
            
            
            
    return "Computer Team Total Runs are:" , compteamtotalruns

def final_overview():
    totalteamnames=User_team+Comp_team
    totalrecord=userrecord+comprecord
    print("FINAL SCOREBOARD IS:")
    print(totalteamnames,totalrecord)
    '''df2=pd.DataFrame(totalrecord,columns=['Runs Scored'],index=[totalteamnames])
    print(df2)'''
    
    print("\nTOTAL RUNS OF USER TEAM:",userteamtotalruns,
          "\nTOTAL RUNS OF COMPUTER TEAM:",compteamtotalruns)
    if userteamtotalruns>compteamtotalruns:
        print("\n\i\bYOU WON!!!!")
    elif userteamtotalruns<compteamtotalruns:
        print("\n\i\bYOU LOSE!!!")
    else:
        print("\n\i\bIt's A DRAW."
              "\n THANK YOU FOR PLAYING!")
        
    playagain=input("Do you want to play again? YES?NO:")
    if playagain=='YES':
        maingame()
    else:
        print('OK')
    
    
            
def maingame():
    print("\nLets Play The Classic ODD/EVEN Game First!")
    oddevengame()
    if (oddeve=='EVEN' and oeresult%2==0) or (oddeve=="ODD" and oeresult%2!=0):
        #user won the odd even game
        print("User won the ODD/EVEN Toss!")
        Choice=input("Choose BAT OR BALL:")
        if Choice=='BAT':
                batting()
                print("Now its your turn to Ball!")
                balling()
                final_overview()
        elif Choice=="BALL":
                balling()
                ("Now its your turn to Bat!")
                batting()
                final_overview()
        else:
            print("invalid input")
            pass 
    elif (oddeve=="ODD" and oeresult%2==0) or (oddeve=="EVEN" and oeresult%2!=0):
        #computer won the odd even game
        print("Computer won the ODD/EVEN Toss!")
        Choice1=random.choice(gamepl)
        print("\nComputer choses to:", Choice1)
        if Choice1=='BAT':
                balling()
                print("Now its your turn to Bat!")
                batting()
                final_overview()
        elif Choice1=="BALL":
                batting()
                print("Now its your turn to Ball!")
                balling()
                final_overview()
        else:
            pass
    
maingame()
                
        
        
    
        
        


        
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    