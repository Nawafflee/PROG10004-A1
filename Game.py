import time
import Cuphead
import Mugman
import random

"""This Module is used to implement the Game Data and Logic"""

class Game:
    
    #Game Introduction Text Constants
    GAME_WELCOME = "Welcome to"
    GAME_TITLE   = "Cuphead & Mugman: The Return of King Dice"
    GAME_INTRO_1  = "After the defeat and surrender of King Dice along with The Devil the story of both brothers ends in happiness..."
    GAME_INTRO_2  = "Inkwell Isle celebrates victory and both brothers were seen as heroes..."
    GAME_INTRO_3  = "OR.. is this really the true happy ending to the story?"
    GAME_INTRO_4  = "We all know that after this triumph both Cuphead and Mugman stopped gambling all together!"
    GAME_INTRO_5  = "But... in the end of things.. It always go back to the beginning, some call it passion!" 
    GAME_INTRO_6  = "But to the all of us this is yet another typical Disney love story...."
    GAME_INTRO_7  = "Mercy - Where do you go *song playing in the background*"
    GAME_INTRO_8  = "A wild Ms. Chalice appears out of nowhere..."
    GAME_INTRO_9  = "Both Cuphead and Mugman fall in love with Ms. Chalice trying their best to win her heart..."
    GAME_INTRO_10 ="They both spent money taking her out on expensive Caviar and Oyster restaurants not knowing that their savings will soon run out..."
    GAME_INTRO_11 ="Their wallets running dry and with desperate calls comes desperate measures..."
    GAME_INTRO_12 ="That means that they have to go back to the casino..."
    GAME_INTRO_13 ="Unfortunately... They borrowed so much money again from the casino and lost it all betting black on Roulette..."
    GAME_INTRO_14 ="They were again at the mercy of King Dice and his henchmen..."
    GAME_INTRO_15 ="Their debts are now due...."

    #In-game loading symbols and Loading Screen Constants
    STAR_SYMBOL = "**********************************************************************************" #just a divider between texts
    MINUS_SYMBOL ="----------------------------------------------------------------------------------"
    HASHTAG_SYMBOL = "###############################################################################"
    LOADING_SCREEN = "Loading Game......."
    PLAYER_SELECT_LOADING = "Player Selection is Loading......."

    #Character Script Names Constants
    CUPHEAD = "Cuphead: "
    MUGMAN = "Mugman: "
    KING_DICE = "King Dice: "
    THE_DEVIL = "The Devil: "
    ANDREW_TATE = "Andrew Tate: "
    TRISTAN_TATE = "Tristan Tate: "
    KYLE_NELK_BOYS = "Kyle (Nelk Boys): "
    PIP_AND_DOT = "Pip & Dot: "

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
    ATOMOSPHERE_1 = "*Cuphead and Mugman are kidnapped by King Dice's Henchmen*"
    ATOMOSPHERE_2 = "*The Henchmen forcefully take the brothers to King Dice's office*"

    #King Dice's Office Speech
    OFFICE_SPEECH_1= "So here we go again, you were both greedy and fate has once again brought us together! How delightful!"
    OFFICE_SPEECH_2= "Now one of you is going to be locked up in my dungeon while being tortured by Pip & Dot!"
    OFFICE_SPEECH_3 = "I can't wait for them to try my new torture tools that came all the way from Italy!"
    
    #Cuphead Office Speech 
    OFFICE_SPEECH_4 = "ITALY! Mammamìa!"
   
    #King Dice Speech
    OFFICE_SPEECH_5 = "Yes, it was a special order from the Italian Mafia, I can't wait to try it on the both of you! HAHAHAHA!"
    OFFICE_SPEECH_6 = "I have decided that one of you will be tortured while the other will live to do my bidding!"
    OFFICE_SPEECH_7  = "Until I get bored of it obviously, which is never!!"
    
    #Mugman Office Speech
    OFFICE_SPEECH_8 = "*Cries in the corner* This keeps getting worse and worse! I don't want to be held by King Dice!"
    
    #Cuphead Office Speech
    OFFICE_SPEECH_9= "Me neither but one of us has to go for the time being...."
    
    #Player Selection Screen
    PLAYER_SELECT = "Dear Player, It is up to you to control the outcome of this game type 'Cuphead' or 'Mugman' to have as your main character: "

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
