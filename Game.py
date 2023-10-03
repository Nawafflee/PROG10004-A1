import time

#This Module below is used to implement the Game Data and Logic

class Game:
    
    #Game Introduction Text
    gameWelcome = "Welcome to"
    gameTitle   = "Cuphead & Mugman: The Return of King Dice"
    gameIntro1  = "After the defeat and surrender of King Dice along with The Devil the story of both brothers ends in happiness..."
    gameIntro2  = "Inkwell Isle celebrates victory and both brothers were seen as heroes..."
    gameIntro3  = "OR.. is this really the true happy ending to the story?"
    gameIntro4  = "We all know that after this triumph both Cuphead and Mugman stopped gambling all together!"
    gameIntro5  = "But.... At the end of things.. It always go back to the beginning, some call it passion!" 
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

    #in-game loading symbols and Loading Screen
    starSymbol = "**********************************************************************************" #just a divider between texts
    minusSymbol ="----------------------------------------------------------------------------------"
    hashtagSymbol = "###############################################################################"
    loadingScreen = "Loading Game......."
    playerSelectLoading = "Player Selection is Loading......."

    #Time Function in between script texts
    def textSpeed(x):
        time.sleep(x)
        return x
    
    #Simple In-game exit functon
    def inGameExit():
        quit()
