import Game
import time
import Cuphead
import Mugman

"""This module contains the actual game where everything gets printed and this is also where the interactivity with the user is being put into test"""
"""Github Repository https://github.com/Nawafflee/PROG10004-A1 """


print(Game.Game.GAME_WELCOME, Game.Game.GAME_TITLE)
time.sleep(2)
#This is the settings menu where the user picks an integer speed from 1 to 10
print("Dear Player, let's take you on a trip to the settings menu:")
time.sleep(2)
print("Settings: ")

#Terminal settings menu to pick the in-game text speed
while True:
    try:
        textSetting = int(input("Pick the in-game text speed from 1-10 (Seconds) (Recommended 5): "))
        print("You have now selected,", textSetting, "as your primary text speed")
        print(input("Press Enter to continue..."))
        break #Will exit the loop once success has been achieved
    except ValueError:
        print("Invalid input.Please enter an integer")

#Game Introduction and Welcome Screen!
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_1)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_2)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_3)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_4)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_5)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_6)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_7)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_8)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_9)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_10)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_11)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_12)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_13)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_14)
Game.Game.textSpeed(textSetting)
print(Game.Game.GAME_INTRO_15)
Game.Game.textSpeed(textSetting)


#Loading Screen
print(Game.Game.STAR_SYMBOL)
print(Game.Game.LOADING_SCREEN.center(70))
print(Game.Game.STAR_SYMBOL)
time.sleep(2)

#Office Speech
print(Game.Game.ATOMOSPHERE_1)
Game.Game.textSpeed(textSetting)
print(Game.Game.ATOMOSPHERE_2)
Game.Game.textSpeed(textSetting)
print(Game.Game.KING_DICE,Game.Game.OFFICE_SPEECH_1)
Game.Game.textSpeed(textSetting)
print(Game.Game.KING_DICE,Game.Game.OFFICE_SPEECH_2)
Game.Game.textSpeed(textSetting)
print(Game.Game.KING_DICE,Game.Game.OFFICE_SPEECH_3)
Game.Game.textSpeed(textSetting)
print(Game.Game.CUPHEAD,Game.Game.OFFICE_SPEECH_4)
Game.Game.textSpeed(textSetting)
print(Game.Game.KING_DICE,Game.Game.OFFICE_SPEECH_5)
Game.Game.textSpeed(textSetting)
print(Game.Game.KING_DICE,Game.Game.OFFICE_SPEECH_6)
Game.Game.textSpeed(textSetting)
print(Game.Game.KING_DICE,Game.Game.OFFICE_SPEECH_7)
Game.Game.textSpeed(textSetting)
print(Game.Game.MUGMAN,Game.Game.OFFICE_SPEECH_8)
Game.Game.textSpeed(textSetting)
print(Game.Game.CUPHEAD,Game.Game.OFFICE_SPEECH_9)

#Player Selection Loading Screen
print(Game.Game.MINUS_SYMBOL)
print(Game.Game.PLAYER_SELECT_LOADING.center(70))
print(Game.Game.MINUS_SYMBOL)
time.sleep(2)

while True:
    try:
        #Player Selection Menu
        playerSelection = str(input(Game.Game.PLAYER_SELECT))
        #Defining the different ways cuphead can be selected            
        if (playerSelection == "cuphead" or playerSelection == "Cuphead"):
            print("You Have Selected", playerSelection)

            #Cuphead With Statistics Option
            #Entry to Display Cuphead's Statistics
            cupheadStats = str(input("Would you like to display Cuphead's statistics? "))
            if (cupheadStats == "yes") or (cupheadStats == "Yes") or (cupheadStats =="Y") or (cupheadStats == "y"):
                print(Game.Game.CUPHEAD,"Strength: ",Game.Game.cupheadStrengthLevel,"Speed: ",Game.Game.cupheadSpeedLevel,"Wisdom: ",Game.Game.cupheadWisdomLevel,"Health: ",Game.Game.cupheadHealthLevel)
                print(input("Press Enter to Continue..."))
                print(Game.Game.CUPHEAD,"Thank you for picking me, I know of a way out...")
                Game.Game.textSpeed(textSetting)

                #Andrew & Tristan Speech
                print("Meanwhile... In Romania at the Tate Mansion... *Indila - Tourner Dans Le Vide* playing at the Emergency Meeting")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Welcome to the Emergency Meeting where I the Top G along with brother Tristan are going to teach all of you brokies about true male masculinity!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Oh come on Andrew! How are you going to teach them about masculinity when they can't even afford my 10,000$ suit and my $400 expensive Cuban Cigars!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"To everyone! I don't care, if you really want to be a Top G like I am and spend money on expensive drinks. Then join The real world and make money now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"While we were in Romanian Prison over the past 6 months our cousin Luc came up with the Real World 10.0! This program is now at its truest form to help you escape the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Yes, indeed and that is how you escape from poverty ladies and gentlemen!")
                Game.Game.textSpeed(textSetting)
                print("*A moment of Silence on stream happens as the phone rings*")
                Game.Game.textSpeed(textSetting)
                print("Andrew picks up the phone while smoking his expensive gold-plated Cuban Cigar!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"Top G! Top G!, I need your help!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Who are you and how did you get my number, Tristan get security! We are under attack by an agent from the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD," Well.. Porkrind has given me your number and he told me that you possess the world's strongest weapon that can defeat all sorts of bad enemies in the world!")
                Game.Game.textSpeed(textSetting)
                print("*Panic Ensues as Andrew and Tristan decide to end the Emergency meeting livestream on Rumble*")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, " *** Gets invited over to the Tate mansion ***")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"I don't know what you're talking about if you think that my bald head can shoot down lasers then you are absolutely correct! ...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"However, my Masseuse has gone down for vacation and my head needs a lot of polishing so that leaves you with only one option....")
                Game.Game.textSpeed(textSetting)
                print("*The Nelk Boys Interrupt the meeting*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.KYLE_NELK_BOYS,"Yo Tate full send it yea! Here is some Happy Dad Seltzer for you!")
                Game.Game.textSpeed(textSetting)
                print("*** Kyle Hands Happy Dad to Andrew ***")
                Game.Game.textSpeed(textSetting)
                print("*** Andrew Tate grows some wisdom within himself! ***")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Now that was way better than sparkling water!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Stop! Andrew! Are you seriously going to give this Cuphead brokie the weapon of a True G!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE, "Yes, I feel bad and he reminds me a lot of my days eating KFC and my time with Adin too, but a brokie version of himself!")
                Game.Game.textSpeed(textSetting)
                print("Andrew & Tristan (Privately): I mean you do realize that King Dice hasn't been fair enough with my casino establishments lately, he's been aiming for a 30 percent cut on our earnings and that is bad, we can't even afford to buying a new Bugatti!")
                Game.Game.textSpeed(textSetting)
                print("Tristan (Privately): Also, my expensive cigars were all taken by him not to mention lending him a my new Aston Martin...")
                Game.Game.textSpeed(textSetting)
                print("Tristan (Privately): Now I am driving my Lada and I feel like a brokie too! No other women will see as me as the 'Rich Romanian Playboy' that dates models!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"So what am I going to do? I have to save Mugman.")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Have no worries brother! I will provide you with the weapon of mass destruction!")
                Game.Game.textSpeed(textSetting)
                print("*Cuphead, Andrew, and Tristan Enter the Garage*")
                Game.Game.textSpeed(textSetting)
                print("A wild Bugatti Appears!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Tristan! Do your thing and transform into a wizard!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE, "I haven't done this in a while though...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Do it and stop being a coward like our cousin Luc sitting on the computer all day!")
                Game.Game.textSpeed(textSetting)
                print("Tristan Transforms into a wizard and enchants a spell....")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Bugatti Bugatti on the floor show me the greatest weapon of them all!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Turn yourself into a two-sided Dice and give it all to Cuphead without thinking twice!")
                Game.Game.textSpeed(textSetting)
                print("The Bugatti Transforms into a two-sided dice capable of causing havok among any enemy...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD, "Thank you Top G! I am glad to have done this with you, I will need to rescue Mugman Now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"I want to be a force of good and defeating King Dice and the Devil is all that I want, you can keep the Dice and never return it back!")
                Game.Game.textSpeed(textSetting)

                #Phase One Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)

                print("Phase One: Defeat Pip and Dot! (The Quest for Strength)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"*Magical Dice show me where Mugman is and teleport me to his location*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PIP_AND_DOT,"Who is this?")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"Its me Cuphead!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PIP_AND_DOT,"So you have come to join your brother at the torture chamber...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD, "Bugatti Dice! Activate!")
                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)


                #Phase One Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.CUPHEAD_NAME,"has lost", number, "points making his strength attribute at ", (Cuphead.Cuphead.strengthCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his strength attribute the same at ", (Cuphead.Cuphead.strengthCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his strength attribute the same at", (Cuphead.Cuphead.strengthCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.CUPHEAD_NAME,"has won", number, "Making his strength attribute at ", (Cuphead.Cuphead.strengthCuphead) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "Defeats Pip and Dot")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "Saves Mugman")

                #Phase Two Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    
                
                print("Phase Two: Defeat King Dice (The Quest for Speed)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"*Cuphead Teleports to King Dice*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.KING_DICE,"uhhh what is going on")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "&", Mugman.Mugman.MUGMAN_NAME, ": We are here to defeat you!")
                Game.Game.textSpeed(textSetting)

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)

                #Phase Two Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.CUPHEAD_NAME,"has lost", number, "points making his speed attribute at ", (Cuphead.Cuphead.speedCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his speed attribute the same at ", (Cuphead.Cuphead.speedCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his speed attribute the same at ", (Cuphead.Cuphead.speedCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.CUPHEAD_NAME,"has won", number, "Making his speed attribute at", (Cuphead.Cuphead.speedCuphead) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "Defeats King Dice")
                Game.Game.textSpeed(textSetting)

                #Phase Three Loading Screen
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    

                print("Phase Three: Defeat the Devil (The Quest for Wisdom)")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "&",Mugman.Mugman.MUGMAN_NAME, "Teleport to the Devil!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.THE_DEVIL,"What????!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"We are here to officially defeat you!")

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)

                #Phase Three Dice Algorithm 
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.CUPHEAD_NAME,"has lost", number, "points making his wisdom attribute at ", (Cuphead.Cuphead.wisdomCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his wisdom attribute the same at ", (Cuphead.Cuphead.wisdomCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his wisdom attribute the same at", (Cuphead.Cuphead.wisdomCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.CUPHEAD_NAME,"has won", number, "Making his wisdom attribute", (Cuphead.Cuphead.wisdomCuphead) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "Defeats The Devil")
                Game.Game.textSpeed(textSetting)

                #Final Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    

                #Game Ending Cuphead with Statistics Menu Option
                print("*** Cuphead and Mugman gifts the dice to Ms. Chalice but Ms. Chalice has already changed her facebook status to 'in a relationship with Tristan Tate' ***")
                Game.Game.textSpeed(textSetting)
                print("*** Cuphead and Mugman are in shock and can't comprehend what is happening? ***")
                Game.Game.textSpeed(textSetting)
                print("Tristan & Andrew: You were both being played in the end and now we would like my have our 10,000,000$ Bugatti branded Dice back!")
                Game.Game.textSpeed(textSetting)
                print("To be continued....")
                Game.Game.textSpeed(textSetting)
                print("Game Over! You lose for now!")
                print("Created By Nawaf Raheem")
                Game.Game.inGameExit
                break
            else:
                #Cuphead without statistics option
                print(input("Press Enter to Continue..."))
                print(Game.Game.CUPHEAD,"Thank you for picking me, I know of a way out...")
                Game.Game.textSpeed(textSetting)

                #Andrew & Tristan Speech
                print("Meanwhile... In Romania at the Tate Mansion... *Indila - Tourner Dans Le Vide* playing at the Emergency Meeting")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Welcome to the Emergency Meeting where I the Top G along with brother Tristan are going to teach all of you brokies about true male masculinity!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Oh come on Andrew! How are you going to teach them about masculinity when they can't even afford my 10,000$ suit and my $400 expensive Cuban Cigars!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"To everyone! I don't care, if you really want to be a Top G like I am and spend money on expensive drinks. Then join The real world and make money now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"While we were in Romanian Prison over the past 6 months our cousin Luc came up with the Real World 10.0! This program is now at its truest form to help you escape the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Yes, indeed and that is how you escape from poverty ladies and gentlemen!")
                Game.Game.textSpeed(textSetting)
                print("*A moment of Silence on stream happens as the phone rings*")
                Game.Game.textSpeed(textSetting)
                print("Andrew picks up the phone while smoking his expensive gold-plated Cuban Cigar!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"Top G! Top G!, I need your help!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Who are you and how did you get my number, Tristan get security! We are under attack by an agent from the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD," Well.. Porkrind has given me your number and he told me that you possess the world's strongest weapon that can defeat all sorts of bad enemies in the world!")
                Game.Game.textSpeed(textSetting)
                print("*Panic Ensues as Andrew and Tristan decide to end the Emergency meeting livestream on Rumble*")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, " *** Gets invited over to the Tate mansion ***")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"I don't know what you're talking about if you think that my bald head can shoot down lasers then you are absolutely correct! ...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"However, my Masseuse has gone down for vacation and my head needs a lot of polishing so that leaves you with only one option....")
                Game.Game.textSpeed(textSetting)
                print("*The Nelk Boys Interrupt the meeting*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.KYLE_NELK_BOYS,"Yo Tate full send it yea! Here is some Happy Dad Seltzer for you!")
                Game.Game.textSpeed(textSetting)
                print("*** Kyle Hands Happy Dad to Andrew ***")
                Game.Game.textSpeed(textSetting)
                print("*** Andrew Tate grows some wisdom within himself! ***")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Now that was way better than sparkling water!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.THE_DEVIL,"Stop! Andrew! Are you seriously going to give this Cuphead brokie the weapon of a True G!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE, "Yes, I feel bad and he reminds me a lot of my days eating KFC and my time with Adin too, but a brokie version of himself!")
                Game.Game.textSpeed(textSetting)
                print("Andrew & Tristan (Privately): I mean you do realize that King Dice hasn't been fair enough with my casino establishments lately, he's been aiming for a 30 percent cut on our earnings and that is bad, we can't even afford to buying a new Bugatti!")
                Game.Game.textSpeed(textSetting)
                print("Tristan (Privately): Also, my expensive cigars were all taken by him not to mention lending him a my new Aston Martin...")
                Game.Game.textSpeed(textSetting)
                print("Tristan (Privately): Now I am driving my Lada and I feel like a brokie too! No other women will see as me as the 'Rich Romanian Playboy' that dates models!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"So what am I going to do? I have to save mugman.")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Have no worries brother! I will provide you with the weapon of mass destruction!")
                Game.Game.textSpeed(textSetting)
                print("*Cuphead, Andrew, and Tristan Enter the Garage*")
                Game.Game.textSpeed(textSetting)
                print("A wild Bugatti Appears!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Tristan! Do your thing and transform into a wizard!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE, "I haven't done this in a while though...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Do it and stop being a coward like our cousin Luc sitting on the computer all day!")
                Game.Game.textSpeed(textSetting)
                print("Tristan Transforms into a wizard and enchants a spell....")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Bugatti Bugatti on the floor show me the greatest weapon of them all!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Turn yourself into a two-sided Dice and give it all to Cuphead without thinking twice!")
                Game.Game.textSpeed(textSetting)
                print("The Bugatti Transforms into a two-sided dice capable of causing havok among any enemy...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD, "Thank you Top G! I am glad to have done this with you, I will need to rescue Mugman Now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"I want to be a force of good and defeating King Dice and the Devil is all that I want, you can keep the Dice and never return it back!")
                Game.Game.textSpeed(textSetting)

                #Phase One Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)

                print("Phase One: Defeat Pip and Dot! (The Quest for Strength)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"*Magical Dice show me where Mugman is and teleport me to his location*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PIP_AND_DOT,"Who is this?")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"Its me Cuphead!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PIP_AND_DOT,"So you have come to join your brother at the torture chamber...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD, "Bugatti Dice! Activate!")
                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)

                #Phase One Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.CUPHEAD_NAME,"has lost", number, "points making his strength attribute at: ", (Cuphead.Cuphead.strengthCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his strength attribute the same at: ", (Cuphead.Cuphead.strengthCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his strength attribute the same at: ", (Cuphead.Cuphead.strengthCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.CUPHEAD_NAME,"has won", number, "Making his strength attribute at: ", (Cuphead.Cuphead.strengthCuphead) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "Defeats Pip and Dot")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "Saves Mugman")

                #Phase Two Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    
                
                print("Phase Two: Defeat King Dice (The Quest for Speed)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"*Cuphead Teleports to King Dice*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.KING_DICE,"uhhh what is going on")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "&", Mugman.Mugman.MUGMAN_NAME, ": We are here to defeat you!")
                Game.Game.textSpeed(textSetting)

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)

                #Phase Two Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.CUPHEAD_NAME,"has lost", number, "points making his speed attribute at: ", (Cuphead.Cuphead.speedCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his speed attribute the same at: ", (Cuphead.Cuphead.speedCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his speed attribute the same at: ", (Cuphead.Cuphead.speedCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.CUPHEAD_NAME,"has won", number, "Making his speed attribute at: ", (Cuphead.Cuphead.speedCuphead) + number)
                else: 
                    Game.Game.inGameExit()
                Game.Game.textSpeed(textSetting)

                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "Defeats King Dice")
                Game.Game.textSpeed(textSetting)

                #Phase Three Loading Screen
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    

                print("Phase Three: Defeat the Devil (The Quest for Wisdom)")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "&",Mugman.Mugman.MUGMAN_NAME, "Teleport to the Devil!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.THE_DEVIL,"What????!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"We are here to officially defeat you!")

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)

                #Phase Three Dice Algorithm 
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.CUPHEAD_NAME,"has lost", number, "points making his wisdom attribute at: ", (Cuphead.Cuphead.wisdomCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his wisdom attribute the same at: ", (Cuphead.Cuphead.wisdomCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.CUPHEAD_NAME,"has not lost any character attribute points, making his wisdom attribute the same at: ", (Cuphead.Cuphead.wisdomCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.CUPHEAD_NAME,"has won", number, "Making his wisdom attribute at: ", (Cuphead.Cuphead.wisdomCuphead) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "Defeats The Devil")
                Game.Game.textSpeed(textSetting)

                #Final Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    

                #Game Ending Cuphead without statistics Menu Option
                print("*** Cuphead and Mugman gifts the dice to Ms. Chalice but Ms. Chalice has already changed her facebook status to 'in a relationship with Tristan Tate' ***")
                Game.Game.textSpeed(textSetting)
                print("*** Cuphead and Mugman are in shock and can't comprehend what is happening? ***")
                Game.Game.textSpeed(textSetting)
                print("Tristan & Andrew: You were both being played in the end and now we would like my have our 10,000,000$ Bugatti branded Dice back!")
                Game.Game.textSpeed(textSetting)
                print("To be continued....")
                Game.Game.textSpeed(textSetting)
                print("Game Over! You lose for now!")
                print("Created By Nawaf Raheem")
                Game.Game.inGameExit
                break
            
        #Mugman with Statistics Option 
        elif (playerSelection == "mugman" or playerSelection == "Mugman"):
            print("You Have Selected", playerSelection)

            #Entry to Display Mugman's Statistics
            mugmanStats = str(input("Would you like to display Mugman's statistics? "))
            if (mugmanStats == "yes") or (mugmanStats == "Yes") or (mugmanStats =="Y") or (mugmanStats == "y"):
                print(Game.Game.MUGMAN,"Strength: ",Game.Game.mugmanStrengthLevel,"Speed: ",Game.Game.mugmanSpeedLevel,"Wisdom: ",Game.Game.mugmanWisdomLevel,"Health: ",Game.Game.mugmanHealthLevel)
                print(input("Press Enter to Continue..."))
                print(Game.Game.MUGMAN,"Thank you for picking me, I know of a way out...")
                Game.Game.textSpeed(textSetting)

                #Andrew & Tristan Speech
                print("Meanwhile... In Romania at the Tate Mansion... *Indila - Tourner Dans Le Vide* playing at the Emergency Meeting")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Welcome to the Emergency Meeting where I the Top G along with brother Tristan are going to teach all of you brokies about true male masculinity!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Oh come on Andrew! How are you going to teach them about masculinity when they can't even afford my 10,000$ suit and my $400 expensive Cuban Cigars!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"To everyone! I don't care, if you really want to be a Top G like I am and spend money on expensive drinks. Then join The real world and make money now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"While we were in Romanian Prison over the past 6 months our cousin Luc came up with the Real World 10.0! This program is now at its truest form to help you escape the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Yes, indeed and that is how you escape from poverty ladies and gentlemen!")
                Game.Game.textSpeed(textSetting)
                print("*A moment of Silence on stream happens as the phone rings*")
                Game.Game.textSpeed(textSetting)
                print("Andrew picks up the phone while smoking his expensive gold-plated Cuban Cigar!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN,"Top G! Top G!, I need your help!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Who are you and how did you get my number, Tristan get security! We are under attack by an agent from the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN," Well Porkrind has given me your number and he told me that you possess the world's strongest weapon that can defeat all sorts of bad enemies in the world!")
                Game.Game.textSpeed(textSetting)
                print("*Panic Ensues as Andrew and Tristan decide to end the Emergency meeting livestream on Rumble*")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, " *** Gets invited over to the Tate mansion ***")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"I don't know what you're talking about if you think that my bald head can shoot down lasers then you are absolutely correct! ...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"However, my Masseuse has gone down for vacation and my head needs a lot of polishing so that leaves you with only one option....")
                Game.Game.textSpeed(textSetting)
                print("*The Nelk Boys Interrupt the meeting*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.KYLE_NELK_BOYS,"Yo Tate full send it yea! Here is some Happy Dad Seltzer for you!")
                Game.Game.textSpeed(textSetting)
                print("*** Kyle Hands Happy Dad to Andrew ***")
                Game.Game.textSpeed(textSetting)
                print("*** Andrew Tate grows some wisdom within himself! ***")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Now that was way better than sparkling water!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Stop! Andrew! Are you seriously going to give this Mugman brokie the weapon of a True G!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE, "Yes, I feel bad and he reminds me a lot of my days eating KFC and my time with Adin too, but a brokie version of himself!")
                Game.Game.textSpeed(textSetting)
                print("Andrew & Tristan (Privately): I mean you do realize that King Dice hasn't been fair enough with my casino establishments lately, he's been aiming for a 30 percent cut on our earnings and that is bad, we can't even afford to buying a new Bugatti.")
                Game.Game.textSpeed(textSetting)
                print("Tristan (Privately): Also, my expensive cigars were all taken by him not to mention lending him a my new Aston Martin...")
                Game.Game.textSpeed(textSetting)
                print("Tristan (Privately): Now I am driving my Lada and I feel like a brokie too! No other women will see as me as the 'Rich Romanian Playboy' that dates models!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN,"So what am I going to do? I have to save Cuphead.")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Have no worries brother! I will provide you with the weapon of mass destruction!")
                Game.Game.textSpeed(textSetting)
                print("*Mugman, Andrew, and Tristan Enter the Garage*")
                Game.Game.textSpeed(textSetting)
                print("A wild Bugatti Appears!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Tristan! Do your thing and transform into a wizard!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE, "I haven't done this in a while though...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Do it and stop being a coward like our cousin Luc sitting on the computer all day!")
                Game.Game.textSpeed(textSetting)
                print("Tristan Transforms into a wizard and enchants a spell....")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Bugatti Bugatti on the floor show me the greatest weapon of them all!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Turn yourself into a two-sided Dice and give it all to Mugman without thinking twice!")
                Game.Game.textSpeed(textSetting)
                print("The Bugatti Transforms into a two-sided dice capable of causing havok among any enemy.")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN, "Thank you Top G! I am glad to have done this with you, I will need to rescue Cuphead Now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"I want to be a force of good and defeating King Dice and the Devil is all that I want, you can keep the Dice and never return it back!")
                Game.Game.textSpeed(textSetting)

                #Phase One Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)

                print("Phase One: Defeat Pip and Dot! (The Quest for Strength)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN,"*Magical Dice show me where Mugman is and teleport me to his location*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PIP_AND_DOT,"Who is this?")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN,"Its me Mugman!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PIP_AND_DOT,"So you have come to join your brother at the torture chamber...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN, "Bugatti Dice! Activate!")
                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollMugman()
                Game.Game.textSpeed(textSetting)

                #Phase One Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Mugman.Mugman.MUGMAN_NAME,"has lost", number, "points making his strength attribute at: ", (Mugman.Mugman.strengthMugman) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his strength attribute the same at: ", (Mugman.Mugman.strengthMugman))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his strength attribute the same at: ", (Mugman.Mugman.strengthMugman))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Mugman.Mugman.MUGMAN_NAME,"has won", number, "Making his strength attribute at: ", (Mugman.Mugman.strengthMugman) + number)
                else: 
                    Game.Game.inGameExit()
                    
                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, "Defeats Pip and Dot")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, "Saves Cuphead")

                #Phase Two Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    
                
                print("Phase Two: Defeat King Dice (The Quest for Speed)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"*Cuphead Teleports to King Dice*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.KING_DICE,"uhhh what is going on")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "&", Mugman.Mugman.MUGMAN_NAME, ": We are here to defeat you!")
                Game.Game.textSpeed(textSetting)

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollMugman()
                Game.Game.textSpeed(textSetting)

                #Phase Two Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Mugman.Mugman.MUGMAN_NAME,"has lost", number, "points making his speed attribute at: ", (Mugman.Mugman.speedMugman) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his speed attribute the same at: ", (Mugman.Mugman.speedMugman))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his speed attribute the same at: ", (Mugman.Mugman.speedMugman))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Mugman.Mugman.MUGMAN_NAME,"has won", number, "Making his speed attribute at: ", (Mugman.Mugman.speedMugman) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, "Defeats King Dice")
                Game.Game.textSpeed(textSetting)

                #Phase Three Loading Screen
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    

                print("Phase Three: Defeat the Devil (The Quest for Wisdom)")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, "&",Cuphead.Cuphead.CUPHEAD_NAME, "Teleport to the Devil!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.THE_DEVIL,"What????!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN,"We are here to officially defeat you!")

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollMugman()
                Game.Game.textSpeed(textSetting)

                #Phase Three Dice Algorithm 
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Mugman.Mugman.MUGMAN_NAME,"has lost", number, "points making his wisdom attribute at: ", (Mugman.Mugman.wisdomMugman) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his wisdom attribute the same at: ", (Mugman.Mugman.wisdomMugman))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his wisdom attribute the same at: ", (Mugman.Mugman.wisdomMugman))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Mugman.Mugman.MUGMAN_NAME,"has won", number, "Making his wisdom attribute at: ", (Mugman.Mugman.wisdomMugman) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, "Defeats The Devil")
                Game.Game.textSpeed(textSetting)

                #Final Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    

                #Game Ending Mugman with Statistics Menu Option
                print("*** Cuphead and Mugman gifts the dice to Ms. Chalice but Ms. Chalice has already changed her facebook status to 'in a relationship with Tristan Tate' ***")
                Game.Game.textSpeed(textSetting)
                print("*** Cuphead and Mugman are in shock and can't comprehend what is happening? ***")
                Game.Game.textSpeed(textSetting)
                print("Tristan & Andrew: You were both being played in the end and now we would like my have our 10,000,000$ Bugatti branded Dice back!")
                Game.Game.textSpeed(textSetting)
                print("To be continued....")
                Game.Game.textSpeed(textSetting)
                print("Game Over! You lose for now!")
                print("Created By Nawaf Raheem")
                Game.Game.inGameExit
                break
            else:
                #Mugman without Statistics Option
                print(input("Press Enter to Continue..."))
                print(Game.Game.MUGMAN,"Thank you for picking me, I know of a way out...")
                Game.Game.textSpeed(textSetting)

                #Andrew & Tristan Speech
                print("Meanwhile... In Romania at the Tate Mansion... *Indila - Tourner Dans Le Vide* playing at the Emergency Meeting")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Welcome to the Emergency Meeting where I the Top G along with brother Tristan are going to teach all of you brokies about true male masculinity!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Oh come on Andrew! How are you going to teach them about masculinity when they can't even afford my 10,000$ suit and my $400 expensive Cuban Cigars!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"To everyone! I don't care, if you really want to be a Top G like I am and spend money on expensive drinks. Then join The real world and make money now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"While we were in Romanian Prison over the past 6 months our cousin Luc came up with the Real World 10.0! This program is now at its truest form to help you escape the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Yes, indeed and that is how you escape from poverty ladies and gentlemen!")
                Game.Game.textSpeed(textSetting)
                print("*A moment of Silence on stream happens as the phone rings*")
                Game.Game.textSpeed(textSetting)
                print("Andrew picks up the phone while smoking his expensive gold-plated Cuban Cigar!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN,"Top G! Top G!, I need your help!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Who are you and how did you get my number, Tristan get security! We are under attack by an agent from the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN," Well Porkrind has given me your number and he told me that you possess the world's strongest weapon that can defeat all sorts of bad enemies in the world!")
                Game.Game.textSpeed(textSetting)
                print("*Panic Ensues as Andrew and Tristan decide to end the Emergency meeting livestream on Rumble*")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, " *** Gets invited over to the Tate mansion ***")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"I don't know what you're talking about if you think that my bald head can shoot down lasers then you are absolutely correct! ...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"However, my Masseuse has gone down for vacation and my head needs a lot of polishing so that leaves you with only one option....")
                Game.Game.textSpeed(textSetting)
                print("*The Nelk Boys Interrupt the meeting*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.KYLE_NELK_BOYS,"Yo Tate full send it yea! Here is some Happy Dad Seltzer for you!")
                Game.Game.textSpeed(textSetting)
                print("*** Kyle Hands Happy Dad to Andrew ***")
                Game.Game.textSpeed(textSetting)
                print("*** Andrew Tate grows some wisdom within himself! ***")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Now that was way better than sparkling water!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Stop! Andrew! Are you seriously going to give this Mugman brokie the weapon of a True G!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE, "Yes, I feel bad and he reminds me a lot of my days eating KFC and my time with Adin too, but a brokie version of himself!")
                Game.Game.textSpeed(textSetting)
                print("Andrew & Tristan (Privately): I mean you do realize that King Dice hasn't been fair enough with my casino establishments lately, he's been aiming for a 30 percent cut on our earnings and that is bad, we can't even afford to buying a new Bugatti.")
                Game.Game.textSpeed(textSetting)
                print("Tristan (Privately): Also, my expensive cigars were all taken by him not to mention lending him a my new Aston Martin...")
                Game.Game.textSpeed(textSetting)
                print("Tristan (Privately): Now I am driving my Lada and I feel like a brokie too! No other women will see as me as the 'Rich Romanian Playboy' that dates models!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN,"So what am I going to do? I have to save Cuphead.")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Have no worries brother! I will provide you with the weapon of mass destruction!")
                Game.Game.textSpeed(textSetting)
                print("*Mugman, Andrew, and Tristan Enter the Garage*")
                Game.Game.textSpeed(textSetting)
                print("A wild Bugatti Appears!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Tristan! Do your thing and transform into a wizard!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE, "I haven't done this in a while though...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"Do it and stop being a coward like our cousin Luc sitting on the computer all day!")
                Game.Game.textSpeed(textSetting)
                print("Tristan Transforms into a wizard and enchants a spell....")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Bugatti Bugatti on the floor show me the greatest weapon of them all!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.TRISTAN_TATE,"Turn yourself into a two-sided Dice and give it all to Mugman without thinking twice!")
                Game.Game.textSpeed(textSetting)
                print("The Bugatti Transforms into a two-sided dice capable of causing havok among any enemy.")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN, "Thank you Top G! I am glad to have done this with you, I will need to rescue Cuphead Now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.ANDREW_TATE,"I want to be a force of good and defeating King Dice and the Devil is all that I want, you can keep the Dice and never return it back!")
                Game.Game.textSpeed(textSetting)

                #Phase One Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)

                print("Phase One: Defeat Pip and Dot! (The Quest for Strength)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN,"*Magical Dice show me where Mugman is and teleport me to his location*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PIP_AND_DOT,"Who is this?")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN,"Its me Mugman!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PIP_AND_DOT,"So you have come to join your brother at the torture chamber...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN, "Bugatti Dice! Activate!")
                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollMugman()
                Game.Game.textSpeed(textSetting)

                #Phase One Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Mugman.Mugman.MUGMAN_NAME,"has lost", number, "points making his strength attribute at: ", (Mugman.Mugman.strengthMugman) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his strength attribute the same at: ", (Mugman.Mugman.strengthMugman))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his strength attribute the same at: ", (Mugman.Mugman.strengthMugman))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Mugman.Mugman.MUGMAN_NAME,"has won", number, "Making his strength attribute at: ", (Mugman.Mugman.strengthMugman) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, "Defeats Pip and Dot")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, "Saves Cuphead")

                #Phase Two Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    
                
                print("Phase Two: Defeat King Dice (The Quest for Speed)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.CUPHEAD,"*Cuphead Teleports to King Dice*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.KING_DICE,"uhhh what is going on")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.CUPHEAD_NAME, "&", Mugman.Mugman.MUGMAN_NAME, ": We are here to defeat you!")
                Game.Game.textSpeed(textSetting)

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollMugman()
                Game.Game.textSpeed(textSetting)

                #Phase Two Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Mugman.Mugman.MUGMAN_NAME,"has lost", number, "points making his speed attribute at: ", (Mugman.Mugman.speedMugman) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his speed attribute the same at: ", (Mugman.Mugman.speedMugman))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his speed attribute the same at: ", (Mugman.Mugman.speedMugman))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Mugman.Mugman.MUGMAN_NAME,"has won", number, "Making his speed attribute at: ", (Mugman.Mugman.speedMugman) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, "Defeats King Dice")
                Game.Game.textSpeed(textSetting)


                #Phase Three Loading Screen
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    

                print("Phase Three: Defeat the Devil (The Quest for Wisdom)")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, "&",Cuphead.Cuphead.CUPHEAD_NAME, "Teleport to the Devil!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.THE_DEVIL,"What????!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.MUGMAN,"We are here to officially defeat you!")

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollMugman()
                Game.Game.textSpeed(textSetting)

                #Phase Three Dice Algorithm 
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Mugman.Mugman.MUGMAN_NAME,"has lost", number, "points making his wisdom attribute at: ", (Mugman.Mugman.wisdomMugman) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his wisdom attribute the same at: ", (Mugman.Mugman.wisdomMugman))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Mugman.Mugman.MUGMAN_NAME,"has not lost any character attribute points, making his wisdom attribute the same at: ", (Mugman.Mugman.wisdomMugman))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Mugman.Mugman.MUGMAN_NAME,"has won", number, "Making his wisdom attribute at: ", (Mugman.Mugman.wisdomMugman) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print("*** The mysterious power of the Bugatti dice eradicates the enemy ***")
                Game.Game.textSpeed(textSetting)
                print(Mugman.Mugman.MUGMAN_NAME, "Defeats The Devil")
                Game.Game.textSpeed(textSetting)

                #Final Loading Screen 
                print(Game.Game.STAR_SYMBOL)
                print(Game.Game.LOADING_SCREEN.center(70))
                print(Game.Game.STAR_SYMBOL)
                time.sleep(5)    
                
                #Game Ending Mugman without statistics Menu Option
                print("*** Cuphead and Mugman gifts the dice to Ms. Chalice but Ms. Chalice has already changed her facebook status to 'in a relationship with Tristan Tate' ***")
                Game.Game.textSpeed(textSetting)
                print("*** Cuphead and Mugman are in shock and can't comprehend what is happening? ***")
                Game.Game.textSpeed(textSetting)
                print("Tristan & Andrew: You were both being played in the end and now we would like my have our 10,000,000$ Bugatti branded Dice back!")
                Game.Game.textSpeed(textSetting)
                print("To be continued....")
                Game.Game.textSpeed(textSetting)
                print("Game Over! You lose for now!")
                Game.Game.textSpeed(textSetting)
                print("Created By Nawaf Raheem")
                Game.Game.inGameExit
                break              
    except ValueError:
            print("Role 1 & Role 2 Working")