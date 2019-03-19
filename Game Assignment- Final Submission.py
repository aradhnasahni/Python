# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:34:44 2018

@author: aradhna sahni

"""
# Alladin and his lady love Princess Jasmine 

"""
  DocString:
       A) Introduction:
       This is a fictional game called 'Alladin and his lady love Princess Jasmine',
       a handsome youth named Alladin who desire to marry Princess Jasmine.But 
       Jasmine's father Sultan had put some challenges for Alladin to prove his
       love for his daughter . Sultan sets him 3 stages : start,win and lose 
       to be accomplished to win the heart of beautiful princess Jasmine.
       
       B)Game Map:
       In this exercise, we will assume that we have three rooms on our game
       map.The assignment requirements also specify that we have a fail
       function. Princess Jasmine would be found in room 3 and thus Alladin needs 
       to successfully complete all three stages.Therefore, we will be creating a 
       simple skeleton containing the following elements:
       *start
       * room_1
       * room_2
       * room_3 (Princess Jasmine is waiting here)
       * fail     
        game_start --> room_1 --> room_2 --> room_3 --> (win Jasmine's heart and take her with you)
            |          |         |            |
             `----------`---------`------------`----->  (fail)

Good luck, and thanks for playing. 

Remember - "There is always some madness in Love"
       
 """


from random import randint
from sys import exit


#This is the start of the game where the user Aladdin is all set to go to room 1

def start():
    print("""
          As you're about to start, you have to answer atleast two questions correctly to 
          pass room 1 stage and go to room 2. The questions would be related 
          based on the life of Jasmine in order to check how much you love her.
          
          In this, you must truthfully answer these questions else you will fail.
          """)
    input("<Press enter to continue>") # helps user to enter some value 
    room_1() # This moves us into room_1
    
    
############################################################################################
# Constructing room_1 and linking to room 2
############################################################################################


'''Entering to room 1 has Challenge 1 , where you (Aladdin) has to answer certain questions
to meet your girl Jasmine in room 3. The game will over if your score is less than 2''' # comment
# f-strings allow us to integrate text and variables together.

def room_1():
    
    print(""" \t You're in room 1.To go ahead to room 2 you need to answer 
         atleast two questions correctly!\n""")
    
    question_list = ['What is the town that Jasmine lived in her childhood days called?',
                     'What is the favorite color of Jasmine?',
                     'What is the name of Princess Jasmine\'s tiger?']
    questions = 2
    score = 0
    while questions >= 0:
        
        question = question_list[questions]
        print(question)
        print(" ")
        
        if question == question_list[0]:# The section has conditional answers for question 1.
            
            print("Select any number to choose Jasmine's childhood town.")
            print("1) Agrabah")
            print("2) Kurg")
            print("3) Shimla")
            quest = input("Your selected town: \n")
            if quest == '1':
                print("Wow.. You are correct . Just some more steps to meet your princess.\n")
                score +=1
                questions -=1
            else:
                print("No,this is incorrect.Try again\n")
                questions -=1
                         
        elif question == question_list[1]:# The section has conditional answers for question 2
            print("Select any number or color to choose Jasmine's favourite color.\n")
            print("1) red")
            print("2) yellow")
            print("3) green")
            print("4) blue")
            color = input(">Your selected color \n")
            color = color.lower()
            
            if 'red' in color or 'yellow' in color or '1' in color or '2' in color:
                print("She loves these colors. Good that you know all this !\n")
                score +=1
                questions -=1
            else:
                print("What? That's not her favourite color!\n")
                print("You failed.Please try again to go to the next level\n")
                
                questions -=1
            
        elif question == question_list[2]: # The section has conditional answers for question 3
            print("Select any number to choose for Jasmine's Tiger's name.")
            print("1) Raja")
            print("2) Shamsheer")
            print("3) Jafar")
            quest = input("Choose Jasmine's Tiger name: \n")
            if quest == '1':
                print(""" Wow !!!!!! You are correct . You know this.
                     Awww you really love her 
                     """)
                score +=1
                questions -=1
              
            else:
                print("No,this is incorrect.Try again\n")
                questions -=1
            
    if score>= 2:
        print(f"As your score is {score} .You have passed first stage to meet the princess. Congratulations")
        room_2() # This moves us into room_2
    else:
        print(f"""          As your score is {score}.You have failed go back home in the first stage only 
                  or if you want to try again start the game again""")
        



#############################################################################################
# Adding room_2 and linking to room 3
#############################################################################################

# This stage is more interesting where in you(Aladdin) has to fight for princess
# If-else condition will check if the Aladdin chooses to fight or not.
        
def room_2():
        print("You're in room 2!\n")
        print("""You will now have to defeat with the Jafar-the Sultan's most trusted advisor and is also an evil sorcerer""")
        print("What do you do?")
        print("1) Attack with your sword")
        print("2) Run away!")
    
        challenge=input('>Press your option to continue\n')
        
        if '1' in challenge or 'attack' in challenge or 'sword' in challenge:
                print("You attack with your sword and cut the Jafar's neck off.")
                print("Jafar shouts, yells and cries . 'Tis but a scratch' and runs away.\n")
                input("<Press enter to continue>\n")
                #room_3()
                print("You have passed second stage to meet the princess. Congratulations")
                room_3() # This moves us into room_3       
        
        else:
            
                print('You end up stay alone in the room.')
                fail() 
        
##################################################################################################
# Adding room_3 and linking to room 1
##################################################################################################

'''
This stage is very interesting where in Jasmine asks Aladdin to search a ring for her in the jewel box.
Created a empty list named jewel box having 4X4 matrix and append it with some ***** values.
'''
#help(random.randint)

def room_3():
         print("You're in room 3! Your love of the life is right infront of you!\n")
         print("*****You can now meet Jasmine and tell her about your feelings*****!")
         input("<Press enter to continue>\n")
         print("""
           .-.-. .-.-. .-.-. .-.-. .-.-. .-.-. .-.-.              .-.-.              .-.-. .-.-. .-.-. .-.-.          .-.-. .-.-. .-.-.       
    '. J )'. a )'. s )'. m )'. i )'. n )'. e ).-.-.-.-.-.-.'. I ).-.-.-.-.-.-.'. L )'. o )'. v )'. e ).-.-.-.-.'. Y )'. o )'. u ).-.-. 
      ).'   ).'   ).'   ).'   ).'   ).'   ).' '._.'._.'._.'  ).' '._.'._.'._.'  ).'   ).'   ).'   ).' '._.'._.'  ).'   ).'   ).' '._.'
     """)
         input(">Take a deep breath and press enter")
    
         print("But now Jasmine put forward one challenge for you!\n")
         print("\nShe wants you to find the hidden ring is in a jewel box ")
         print("Your challenge is to spot the jewel box by guessing the row and the column number")
         print("It is a 4X4 jewel box having a max of 4 rows and 4 columns")
         print("Only four chances would be provided for you to guess, else you lose!")
     
         jewelBox=[]
         for ring in range(5):                  # set the maximum range of rows and columns to five
                jewelBox.append(["*"] * 5) 
            
         def jewel_board(jewelBox):
                for col in jewelBox:
                    print("".join(col))        # defining a fuction and filling the jewel box by initialising the columns   
         jewel_board(jewelBox)
         
         def set_random_row(jewelBox):                 
                return randint(0, len(jewelBox) - 1) #return random integer in range [a, b], including both end points.Also reducing the length of jewel box by 1
        
         def set_random_col(jewelBox): 
                return randint(0, len(jewelBox[0]) - 1)  
        
         ring_row=set_random_row(jewelBox)
         ring_col=set_random_col(jewelBox)
         
#prints ring row
#prints ring col

         for turn in range(4):
            print(f"\n Turn", turn+1)
            row_guess=int(input("Guess the row number:"))
            col_guess=int(input("Guess the column number:"))
        
            if(row_guess==ring_row and col_guess==ring_col):#checks if your guess is correct
                print(f"\n Wohoooooo!!!!! You found the jewel box , You can take your Jasmine with you. You Win!!")
                print(""" 
              
                               mMm  _[_]_
                              /(_)\  (_)
                             //)^(\\//:\\
                            /(/&@&\)\|~|/
                           / /-~`~-\ |||
                           `/       \|||
                           `--------'-'--
    """)
                break
            
            else:                                           # checks if your guess is incorrect
                if(row_guess<0 or row_guess>4)or (col_guess<0 or col_guess>4):
                    print(f"\n Oops!!!!!!!!!,the ring is not found there at all")
                elif(jewelBox[row_guess][col_guess]=="X"):
                    print(f"\n Don't fool us .You have already guessed it before")
                else:
                    print(f"\n Oh no! You coudn't spot the jewel box. You lost it")
                    
                    jewelBox[row_guess][col_guess]="X"
                
                if turn == 3:
                    print(f"\n You lost the game. Game over! You ran out of chances.")
                    fail()


    
def fail():
    print('\nYou have failed in meeting Jasmine.Game Over.You have lost all the chances')
    print("""
          
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                          

          """)
    exit(0)

start() # Calling the first function in our map will start our game