import Game
import time
import Cuphead
import Mugman

#This is the actual game Where everything gets printed this is where the interactivity with the user is being put into test

print(Game.Game.gameWelcome, Game.Game.gameTitle)
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
print(Game.Game.gameIntro1)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro2)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro3)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro4)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro5)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro6)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro7)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro8)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro9)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro10)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro11)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro12)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro13)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro14)
Game.Game.textSpeed(textSetting)
print(Game.Game.gameIntro15)
Game.Game.textSpeed(textSetting)


#Loading Screen
print(Game.Game.starSymbol)
print(Game.Game.loadingScreen.center(70))
print(Game.Game.starSymbol)
time.sleep(2)

#Office Speech
print(Game.Game.Atmosphere1)
Game.Game.textSpeed(textSetting)
print(Game.Game.Atmosphere2)
Game.Game.textSpeed(textSetting)
print(Game.Game.kingDice,Game.Game.officeSpeech1)
Game.Game.textSpeed(textSetting)
print(Game.Game.kingDice,Game.Game.officeSpeech2)
Game.Game.textSpeed(textSetting)
print(Game.Game.kingDice,Game.Game.officeSpeech3)
Game.Game.textSpeed(textSetting)
print(Game.Game.cuphead,Game.Game.officeSpeech4)
Game.Game.textSpeed(textSetting)
print(Game.Game.kingDice,Game.Game.officeSpeech5)
Game.Game.textSpeed(textSetting)
print(Game.Game.kingDice,Game.Game.officeSpeech6)
Game.Game.textSpeed(textSetting)
print(Game.Game.kingDice,Game.Game.officeSpeech7)
Game.Game.textSpeed(textSetting)
print(Game.Game.mugman,Game.Game.officeSpeech8)
Game.Game.textSpeed(textSetting)
print(Game.Game.cuphead,Game.Game.officeSpeech9)

#Player Selection Loading Screen
print(Game.Game.minusSymbol)
print(Game.Game.playerSelectLoading.center(70))
print(Game.Game.minusSymbol)
time.sleep(2)

while True:
    try:
        #Player Selection Menu
        playerSelection = str(input(Game.Game.playerSelect))
        #Defining the different ways cuphead can be selected            
        if (playerSelection == "cuphead" or playerSelection == "Cuphead"):
            print("You Have Selected", playerSelection)

            #Cuphead With Statistics Option
            #Entry to Display Cuphead's Statistics
            cupheadStats = str(input("Would you like to display Cuphead's statistics? "))
            if (cupheadStats == "yes") or (cupheadStats == "Yes") or (cupheadStats =="Y") or (cupheadStats == "y"):
                print(Game.Game.cuphead,"Strength: ",Game.Game.cupheadStrengthLevel,"Speed: ",Game.Game.cupheadSpeedLevel,"Wisdom: ",Game.Game.cupheadWisdomLevel,"Health: ",Game.Game.cupheadHealthLevel)
                print(input("Press Enter to Continue..."))
                print(Game.Game.cuphead,"Thank you for picking me, I know of a way out...")
                Game.Game.textSpeed(textSetting)

                #Andrew & Tristan Speech
                print("Meanwhile... In Romania at the Tate Mansion... *Indila - Tourner Dans Le Vide* playing at the Emergency Meeting")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Welcome to the Emergency Meeting where I the Top G along with brother Tristan are going to teach all of you brokies about true male masculinity!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate,"Oh come on Andrew! How are you going to teach them about masculinity when they can't even afford my 10,000$ suit and my $400 expensive cuban cigars!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"To everyone! I don't care, if you really want to be a Top G like I am and spend money on expensive drinks. Then join The real world and make money now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate,"While we were in Romanian Prison over the past 6 months our cousin Luke came up with the Real World 10.0! This program is now at its truest form to help you escape the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Yes, indeed and that is how you escape from poverty ladies and gentlemen!")
                Game.Game.textSpeed(textSetting)
                print("*A moment of Silence on stream happens as the phone rings*")
                Game.Game.textSpeed(textSetting)
                print("Andrew picks up the phone while smoking his expensive gold-plated Cuban Cigar!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"Top G! Top G!, I need your help!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Who are you and how did you get my number, Tristan get security! We are under attack by an agent from the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead," Well.. Porkrind has given me your number and he told me that you possess the world's strongest weapon that can defeat all sorts of bad enemies in the world!")
                Game.Game.textSpeed(textSetting)
                print("*Panic Ensues as Andrew and Tristan decide to end the Emergency meeting livestream on Rumble*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"I don't know what you're talking about if you think that my bald head can shoot down lasers then you are absolutely correct! ...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"However, my Masseuse has gone down for vacation and my head needs a lot of polishing so that leaves you with only one option....")
                Game.Game.textSpeed(textSetting)
                print("*The Nelk Boys Interrupt the meeting*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.kyleNelkBoys,"Yo Tate full send it yea! Here is some Happy Dad Seltzer for you!")
                Game.Game.textSpeed(textSetting)
                print("*** Kyle Hands Happy Dad to Andrew*** and Andrew Tate grows some wisdom within himself! ***")
                Game.Game.textSpeed(textSetting)
                print("*** Andrew Tate grows some wisdom within himself! ***")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Now that was way better than sparkling water!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate,"Stop! Andrew! Are you seriously going to give this Cuphead brokie the weapon of a True G")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate, "Yes, I feel bad and he reminds me a lot of my days eating KFC and Adin too, but a brokie version of himself!")
                Game.Game.textSpeed(textSetting)
                print("Andrew & Tristan (Privately): I mean you do realize that King Dice hasn't been fair enough with my casino establishments lately, he's been aiming for a 30 percent cut on our earnings and that is bad, we can't even afford to buying a new Buggati!")
                Game.Game.textSpeed(textSetting)
                print("Tristan (Privately): Also, my expensive cigars were all taken by him not to mention me lending him a my new Aston martin, so now I am driving my Lada and I feel like a brokie too! No other women will see as me as the 'Rich Romanian Playboy' that dates models!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"So What am I going to do? I have to save mugman.")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Have no Worries brother! I will provide you with the weapon of mass destruction!")
                Game.Game.textSpeed(textSetting)
                print("*Cuphead, Andrew, and Tristan Enter the Garage*")
                Game.Game.textSpeed(textSetting)
                print("A wild Buggati Appears!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Tristan! Do your thing and transform into a wizard!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate, "I haven't done this in a while though")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Do it and stop being a coward like our cousin Luke sitting on the computer all day!")
                Game.Game.textSpeed(textSetting)
                print("Tristan Transforms into a wizard and enchants a spell....")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate,"Buggati Buggati on the floor show me the greatest weapon of them all!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate,"Turn yourself into a two-sided Dice and give it all to Cuphead without thinking twice!")
                Game.Game.textSpeed(textSetting)
                print("The Buggati Transforms into a two-sided dice capable of causing havok among any enemy...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead, "Thank you Top G, I am glad to have done this with you, I will need to rescue Mugman Now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Andrew: I want to be a force of good and defeating King Dice and the Devil is all that I want, you can keep the Dice and never return it back!")
                Game.Game.textSpeed(textSetting)

                #Phase One Loading Screen 
                print(Game.Game.starSymbol)
                print(Game.Game.loadingScreen.center(70))
                print(Game.Game.starSymbol)
                time.sleep(5)

                print("Phase One: Defeat Pip and Dot! (The Quest for Strength)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"*Magical Dice show me where Mugman is and teleport me to his location*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PipandDot,"Who is this?")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"Its me Cuphead!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PipandDot,"So you have come to join your brother at the torture chamber...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead, "Buggati Dice! Activate!")
                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)

                #Phase One Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.cupheadName,"has lost", number, "points making his strength attribute at ", (Cuphead.Cuphead.strengthCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his strength attribute the same at ", (Cuphead.Cuphead.strengthCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his strength attribute the same at", (Cuphead.Cuphead.strengthCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.cupheadName,"has won", number, "Making his strength attribute at ", (Cuphead.Cuphead.strengthCuphead) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.cupheadName, "Saves Mugman")

                #Phase Two Loading Screen 
                print(Game.Game.starSymbol)
                print(Game.Game.loadingScreen.center(70))
                print(Game.Game.starSymbol)
                time.sleep(5)    
                
                print("Phase Two: Defeat King Dice (The Quest for Speed)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"*Cuphead Teleports to King Dice*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.kingDice,"uhhh what is going on")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.cupheadName, "&", Mugman.Mugman.mugmanName, ": We are here to defeat you!")
                Game.Game.textSpeed(textSetting)

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)

                #Phase Two Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.cupheadName,"has lost", number, "points making his speed attribute at ", (Cuphead.Cuphead.speedCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his speed attribute the same at ", (Cuphead.Cuphead.speedCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his speed attribute the same at ", (Cuphead.Cuphead.speedCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.cupheadName,"has won", number, "Making his speed attribute at", (Cuphead.Cuphead.speedCuphead) + number)
                else: 
                    Game.Game.inGameExit()
                Game.Game.textSpeed(textSetting)

                #Phase Three Loading Screen
                print(Game.Game.starSymbol)
                print(Game.Game.loadingScreen.center(70))
                print(Game.Game.starSymbol)
                time.sleep(5)    

                print("Phase Three: Defeat the Devil(The Quest for Wisdom)")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.cupheadName, "&",Mugman.Mugman.mugmanName, "Teleport to the Devil!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.theDevil,"What????!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"We are here to officially defeat you!")

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)

                #Phase Three Dice Algorithm 
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.cupheadName,"has lost", number, "points making his wisdom attribute at ", (Cuphead.Cuphead.wisdomCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his wisdom attribute the same at ", (Cuphead.Cuphead.wisdomCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his wisdom attribute the same at", (Cuphead.Cuphead.wisdomCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.cupheadName,"has won", number, "Making his wisdom attribute", (Cuphead.Cuphead.wisdomCuphead) + number)
                else: 
                    Game.Game.inGameExit()
                Game.Game.textSpeed(textSetting)

                #Game Ending Cuphead with Statistics Menu Option
                print("*** Cuphead and Mugman gifts the dice to Ms. Chalice but Ms. Chalice has already changed her facebook status to 'in a relationship with Tristan Tate' ***")
                Game.Game.textSpeed(textSetting)
                print("*** Cuphead and Mugman are in shock and can't comprehend what is happening? ***")
                Game.Game.textSpeed(textSetting)
                print("Tristan & Andrew: You were both being played in the end and now we would like my have our 10,000,000$ Buggati branded Dice back!")
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
                print(Game.Game.cuphead,"Thank you for picking me, I know of a way out...")
                Game.Game.textSpeed(textSetting)

                #Andrew & Tristan Speech
                print("Meanwhile... In Romania at the Tate Mansion... *Indila - Tourner Dans Le Vide* playing at the Emergency Meeting")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Welcome to the Emergency Meeting where I the Top G along with brother Tristan are going to teach all of you brokies about true male masculinity!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate,"Oh come on Andrew! How are you going to teach them about masculinity when they can't even afford my 10,000$ suit and my $400 expensive cuban cigars!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"To everyone! I don't care, if you really want to be a Top G like I am and spend money on expensive drinks. Then join The real world and make money now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate,"While we were in Romanian Prison over the past 6 months our cousin Luke came up with the Real World 10.0! This program is now at its truest form to help you escape the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Yes, indeed and that is how you escape from poverty ladies and gentlemen!")
                Game.Game.textSpeed(textSetting)
                print("*A moment of Silence on stream happens as the phone rings*")
                Game.Game.textSpeed(textSetting)
                print("Andrew picks up the phone while smoking his expensive gold-plated Cuban Cigar!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"Top G! Top G!, I need your help!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Who are you and how did you get my number, Tristan get security! We are under attack by an agent from the Matrix!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead," Well.. Porkrind has given me your number and he told me that you possess the world's strongest weapon that can defeat all sorts of bad enemies in the world!")
                Game.Game.textSpeed(textSetting)
                print("*Panic Ensues as Andrew and Tristan decide to end the Emergency meeting livestream on Rumble*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"I don't know what you're talking about if you think that my bald head can shoot down lasers then you are absolutely correct! ...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"However, my Masseuse has gone down for vacation and my head needs a lot of polishing so that leaves you with only one option....")
                Game.Game.textSpeed(textSetting)
                print("*The Nelk Boys Interrupt the meeting*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.kyleNelkBoys,"Yo Tate full send it yea! Here is some Happy Dad Seltzer for you!")
                Game.Game.textSpeed(textSetting)
                print("*** Kyle Hands Happy Dad to Andrew*** and Andrew Tate grows some wisdom within himself! ***")
                Game.Game.textSpeed(textSetting)
                print("*** Andrew Tate grows some wisdom within himself! ***")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Now that was way better than sparkling water!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate,"Stop! Andrew! Are you seriously going to give this Cuphead brokie the weapon of a True G")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate, "Yes, I feel bad and he reminds me a lot of my days eating KFC and Adin too, but a brokie version of himself!")
                Game.Game.textSpeed(textSetting)
                print("Andrew & Tristan (Privately): I mean you do realize that King Dice hasn't been fair enough with my casino establishments lately, he's been aiming for a 30 percent cut on our earnings and that is bad, we can't even afford to buying a new Buggati!")
                Game.Game.textSpeed(textSetting)
                print("Tristan (Privately): Also, my expensive cigars were all taken by him not to mention me lending him a my new Aston martin, so now I am driving my Lada and I feel like a brokie too! No other women will see as me as the 'Rich Romanian Playboy' that dates models!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"So What am I going to do? I have to save mugman.")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Have no Worries brother! I will provide you with the weapon of mass destruction!")
                Game.Game.textSpeed(textSetting)
                print("*Cuphead, Andrew, and Tristan Enter the Garage*")
                Game.Game.textSpeed(textSetting)
                print("A wild Buggati Appears!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Tristan! Do your thing and transform into a wizard!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate, "I haven't done this in a while though")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Do it and stop being a coward like our cousin Luke sitting on the computer all day!")
                Game.Game.textSpeed(textSetting)
                print("Tristan Transforms into a wizard and enchants a spell....")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate,"Buggati Buggati on the floor show me the greatest weapon of them all!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.tristanTate,"Turn yourself into a two-sided Dice and give it all to Cuphead without thinking twice!")
                Game.Game.textSpeed(textSetting)
                print("The Buggati Transforms into a two-sided dice capable of causing havok among any enemy...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead, "Thank you Top G, I am glad to have done this with you, I will need to rescue Mugman Now!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.andrewTate,"Andrew: I want to be a force of good and defeating King Dice and the Devil is all that I want, you can keep the Dice and never return it back!")
                Game.Game.textSpeed(textSetting)

                #Phase One Loading Screen 
                print(Game.Game.starSymbol)
                print(Game.Game.loadingScreen.center(70))
                print(Game.Game.starSymbol)
                time.sleep(5)

                print("Phase One: Defeat Pip and Dot! (The Quest for Strength)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"*Magical Dice show me where Mugman is and teleport me to his location*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PipandDot,"Who is this?")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"Its me Cuphead!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.PipandDot,"So you have come to join your brother at the torture chamber...")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead, "Buggati Dice! Activate!")
                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)

                #Phase One Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.cupheadName,"has lost", number, "points making his strength attribute at ", (Cuphead.Cuphead.strengthCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his strength attribute the same at ", (Cuphead.Cuphead.strengthCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his strength attribute the same at", (Cuphead.Cuphead.strengthCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.cupheadName,"has won", number, "Making his strength attribute at ", (Cuphead.Cuphead.strengthCuphead) + number)
                else: 
                    Game.Game.inGameExit()

                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.cupheadName, "Saves Mugman")

                #Phase Two Loading Screen 
                print(Game.Game.starSymbol)
                print(Game.Game.loadingScreen.center(70))
                print(Game.Game.starSymbol)
                time.sleep(5)    
                
                print("Phase Two: Defeat King Dice (The Quest for Speed)")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"*Cuphead Teleports to King Dice*")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.kingDice,"uhhh what is going on")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.cupheadName, "&", Mugman.Mugman.mugmanName, ": We are here to defeat you!")
                Game.Game.textSpeed(textSetting)

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)

                #Phase Two Dice Algorithm
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.cupheadName,"has lost", number, "points making his speed attribute at ", (Cuphead.Cuphead.speedCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his speed attribute the same at ", (Cuphead.Cuphead.speedCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his speed attribute the same at ", (Cuphead.Cuphead.speedCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.cupheadName,"has won", number, "Making his speed attribute at", (Cuphead.Cuphead.speedCuphead) + number)
                else: 
                    Game.Game.inGameExit()
                Game.Game.textSpeed(textSetting)

                #Phase Three Loading Screen
                print(Game.Game.starSymbol)
                print(Game.Game.loadingScreen.center(70))
                print(Game.Game.starSymbol)
                time.sleep(5)    

                print("Phase Three: Defeat the Devil(The Quest for Wisdom)")
                Game.Game.textSpeed(textSetting)
                print(Cuphead.Cuphead.cupheadName, "&",Mugman.Mugman.mugmanName, "Teleport to the Devil!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.theDevil,"What????!")
                Game.Game.textSpeed(textSetting)
                print(Game.Game.cuphead,"We are here to officially defeat you!")

                Game.Game.textSpeed(textSetting)
                test = str(input("Type 'Roll' or 'roll' to roll the dice: "))
                Game.Game.textSpeed(textSetting)
                number = Game.Game.diceRollCuphead()
                Game.Game.textSpeed(textSetting)

                #Phase Three Dice Algorithm 
                if(number >= 2 and number <= 3):
                    print("The Two-sided Dice has Rolled",number)
                    print("Challenge is lost and",Cuphead.Cuphead.cupheadName,"has lost", number, "points making his wisdom attribute at ", (Cuphead.Cuphead.wisdomCuphead) - number)
                elif (number >= 4 and number <= 7):
                    print(number)
                    print("Challenge is lost but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his wisdom attribute the same at ", (Cuphead.Cuphead.wisdomCuphead))
                elif (number >=8 and number <=10):
                    print(number)
                    print("Challenge is won, but",Cuphead.Cuphead.cupheadName,"has not lost any character attribute points, making his wisdom attribute the same at", (Cuphead.Cuphead.wisdomCuphead))
                elif (number >=11 and number <=12):
                    print(number)
                    print("Challenge is won and",Cuphead.Cuphead.cupheadName,"has won", number, "Making his wisdom attribute", (Cuphead.Cuphead.wisdomCuphead) + number)
                else: 
                    Game.Game.inGameExit()
                Game.Game.textSpeed(textSetting)

                #Game Ending Cuphead without statistics Menu Option
                print("*** Cuphead and Mugman gifts the dice to Ms. Chalice but Ms. Chalice has already changed her facebook status to 'in a relationship with Tristan Tate' ***")
                Game.Game.textSpeed(textSetting)
                print("*** Cuphead and Mugman are in shock and can't comprehend what is happening? ***")
                Game.Game.textSpeed(textSetting)
                print("Tristan & Andrew: You were both being played in the end and now we would like my have our 10,000,000$ Buggati branded Dice back!")
                Game.Game.textSpeed(textSetting)
                print("To be continued....")
                Game.Game.textSpeed(textSetting)
                print("Game Over! You lose for now!")
                print("Created By Nawaf Raheem")
                Game.Game.inGameExit
                break              
    except ValueError:
            print("Role 1 Working")