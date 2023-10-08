import time
import Cuphead
import Mugman
import random

"""This Module is used to implement the Game Data and Logic"""

class Game:
    
    #Game Introduction Text
    gameWelcome = "Welcome to"
    gameTitle   = "Cuphead & Mugman: The Return of King Dice"
    gameIntro1  = "After the defeat and surrender of King Dice along with The Devil the story of both brothers ends in happiness..."
    gameIntro2  = "Inkwell Isle celebrates victory and both brothers were seen as heroes..."
    gameIntro3  = "OR.. is this really the true happy ending to the story?"
    gameIntro4  = "We all know that after this triumph both Cuphead and Mugman stopped gambling all together!"
    gameIntro5  = "But... in the end of things.. It always go back to the beginning, some call it passion!" 
    gameIntro6  = "But to the all of us this is yet another typical Disney love story...."
    gameIntro7  = "Mercy - Where do you go *song playing in the background*"
    gameIntro8  = "A wild Ms. Chalice appears out of nowhere..."
    gameIntro9  = "Both Cuphead and Mugman fall in love with Ms. Chalice trying their best to win her heart..."
    gameIntro10 ="They both spent money taking her out on expensive Caviar and Oyester restaurants not knowing that their savings will soon run out..."
    gameIntro11 ="Their wallets running dry and with desperate calls comes desperate measures..."
    gameIntro12 ="That means that they have to go back to the casino..."
    gameIntro13 ="Unfortunately... They borrowed so much money again from the casino and lost it all betting on black on Roulette..."
    gameIntro14 ="They were again at the mercy of King Dice and his henchmen..."
    gameIntro15 ="Their debts are now due...."

    #In-game loading symbols and Loading Screen
    starSymbol = "**********************************************************************************" #just a divider between texts
    minusSymbol ="----------------------------------------------------------------------------------"
    hashtagSymbol = "###############################################################################"
    loadingScreen = "Loading Game......."
    playerSelectLoading = "Player Selection is Loading......."

    #Character Script Names  
    cuphead = "Cuphead: "
    mugman = "Mugman: "
    kingDice = "King Dice: "
    theDevil = "The Devil: "
    andrewTate = "Andrew Tate: "
    tristanTate = "Tristan Tate: "
    kyleNelkBoys = "Kyle (Nelk Boys): "
    PipandDot = "Pip & Dot: "

    #Character Statistics Setup 
    cupheadStrengthLevel = Cuphead.Cuphead.strengthCuphead
    cupheadSpeedLevel = Cuphead.Cuphead.speedCuphead
    cupheadWisdomLevel= Cuphead.Cuphead.wisdomCuphead
    cupheadHealthLevel = Cuphead.Cuphead.healthCuphead

    mugmanStrengthLevel = Mugman.Mugman.strengthMugman
    mugmanSpeedLevel = Mugman.Mugman.speedMugman
    mugmanWisdomLevel = Mugman.Mugman.speedMugman
    mugmanHealthLevel = Mugman.Mugman.healthMugman

    #Atmosphere
    Atmosphere1 = "*Cuphead and Mugman are kidnapped by King Dice's Henchmen*"
    Atmosphere2 = "*The Henchmen forcefully take the brothers to King Dice's office*"

    #King Dice's Office Speech
    officeSpeech1= "So here we go again, you were both greedy and fate has once again brought us together! How delightful!"
    officeSpeech2= "Now one of you is going to be locked up in my dungeon while being tortured by Pip & Dot!"
    officeSpeech3 = "I can't wait for them to try my new torture tools that came all the way from Italy!"
    
    #Cuphead Office Speech 
    officeSpeech4 = "ITALY! Mammamìa!"
   
    #King Dice Speech
    officeSpeech5= "Yes, it was a special order from the Italian Mafia, I can't wait to try it on the both of you! HAHAHAHA!"
    officeSpeech6= "I have decided that one of you will be tortured while the other will live to do my bidding!"
    officeSpeech7 = "Until I get bored of it obviously, which is never!!"
    
    #Mugman Office Speech
    officeSpeech8 = "*Cries in the corner* This keeps getting worse and worse! I don't want to be held by King Dice!"
    
    #Cuphead Office Speech
    officeSpeech9= "Me neither but one of us has to go for the time being...."
    
    #Player Selection Screen
    playerSelect = "Dear Player, It is up to you to control the outcome of this game type 'Cuphead' or 'Mugman' to have as your main character: "

    """Simple and Basic random dice roll Algorithm function for Cuphead"""
    def diceRollCuphead():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        totalDice = dice1 + dice2
        print("Your first Dice Roll is:", dice1)
        print("The Second Dice Roll is :", dice2)
        print("Total Dice Roll is : ", totalDice)
        return totalDice
    
    """Simple and Basic random dice roll Algorithm function for Mugman"""
    def diceRollMugman():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        totalDice = dice1 + dice2
        print("Your first Dice Roll is:", dice1)
        print("The Second Dice Roll is :", dice2)
        print("Total Dice Roll is : ", totalDice)
        return totalDice


    """Time Function in between script texts"""
    def textSpeed(x):
        time.sleep(x)
        return x
    
    """Simple In-game exit function"""
    def inGameExit():
        quit()
