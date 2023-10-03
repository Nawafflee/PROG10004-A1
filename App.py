import Game
import time

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