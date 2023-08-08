from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#Command for coordinates and rgb: pyautogui.displayMousePosition()

#Coordinates:
#'Play' button : X: 1504 Y:  929 RGB: (115, 207,  28)
#'Dont Save' coordinates 1: X:  601 Y:  802 RGB: (236,  69,  31)
#'Dont Save' coordinates 2: X:  646 Y:  804 RGB: (234,  67,  29)
#'Watch' coordinates : X: 1557 Y:  803 RGB: (254, 171,  39)
#'Collect' button after match coordinates: X:  866 Y:  936 RGB: (105, 200,  16)
#'Yes' button for confirming closing an ad : X:  742 Y:  768 RGB: (235,  68,  30)
# Battle chest button on menu : X:  763 Y:  770 RGB: (255, 255, 255)



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(random.uniform(0.1,0.2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def pressEsc():
    keyboard.press('esc')
    time.sleep(random.uniform(0.1,0.4))
    keyboard.release('esc')
    print('Esc key pressed')
    time.sleep(0.5)

def sleep(seconds):
    elapsed_time = 0.0
    while elapsed_time < seconds:
        print(".", end="", flush=True)
        time.sleep(0.5)
        elapsed_time += 0.5
    print()
    
    




#2nd function (called from the 1st one)
#verifies if the battle chest is ready to open
def battleChest():
    if pyautogui.pixel(69,976) [0] == 216:
        if pyautogui.pixel(69,976) [1] == 150:
            if pyautogui.pixel(69,976) [2] == 53:
                print('"Battle Chest" button is available')
                click(69,976)
                print('Battle Chest opened')
                sleep(2)
                pressEsc()
                playVerification()
    else:
        print('Battle Chest is not ready to open')
                
    
    



#1st function
#verifies if the play button can be pressed, if so returns true
def playVerification():
    playButtonPressed = False
    while playButtonPressed == False:
        if pyautogui.pixel(1504,929) [0] == 115:
            if pyautogui.pixel(1504,929) [1] == 207:
                if pyautogui.pixel(1504,929) [2] == 28:
                    time.sleep(1)
                    if pyautogui.pixel(1504,929) [0] == 115:
                        if pyautogui.pixel(1504,929) [1] == 207:
                            if pyautogui.pixel(1504,929) [2] == 28:
                                print('"Play" button is available')
                                battleChest()
                                click(1504,929)
                                if pyautogui.pixel(1504,929) [0] != 115:
                                    if pyautogui.pixel(1504,929) [1] != 207:
                                        if pyautogui.pixel(1504,929) [2] != 28:
                                            print('"Play" button clicked')
                                            playButtonPressed = True
                                            return True
                                else:
                                    print('"Play button" not actually clicked')
                                    
        else:
            print('"Play" button is NOT available')
            pressEsc()
            if pyautogui.pixel(763,770) [0] == 255:
                if pyautogui.pixel(763,770) [1] == 255:
                    if pyautogui.pixel(763,770) [2] == 255:
                        print('"Yes" button is available')
                        click(763,770)
                        print('"Yes" button for confirming the ad closing was clicked')
            else:
                print('"Yes" button for confirming the ad closing was NOT found')
            






#3rd function
#verifies if the game is over
def verifyIfGameIsOver():
    sleep(10)
    gameIsOver = False
    while gameIsOver == False:
        
        sleep(random.uniform(3,5))
        #To walk and not get kicked out
        keyboard.press('W')
        time.sleep(random.uniform(0.2,0.6))
        keyboard.release('W')



        
        
        #Verifiyng if the 'Dont Save 1' message has appeared
        if pyautogui.pixel(601,802) [0] == 236:
            if pyautogui.pixel(601,802) [1] == 69:
                if pyautogui.pixel(601,802) [2] == 31:
                    print()
                    print('"Dont Save 1" button has appeared')
                    pressEsc()
                    time.sleep(1)
                    gameIsOver = True
                    break
        else:
            print('"Dont Save 1" button NOT found')



        #Verifiyng if the 'Dont Save 2' message has appeared
        if pyautogui.pixel(646,804) [0] == 234:
            if pyautogui.pixel(646,804) [1] == 67:
                if pyautogui.pixel(646,804) [2] == 29:
                    print()
                    print('"Dont Save 2" button has appeared')
                    pressEsc()
                    time.sleep(1)
                    gameIsOver = True
                    break
        else:
            print('"Dont Save 2" button NOT found')




        #Verifiyng if the 'Collect' message has appeared
        if pyautogui.pixel(866,936) [0] == 105:
            if pyautogui.pixel(866,936) [1] == 200:
                if pyautogui.pixel(866,936) [2] == 16:
                    print()
                    print('"Collect" button has appeared')
                    pressEsc()
                    gameIsOver = True
        else:
            print('"Collect" button NOT found')
                    
                    
                    
    

    






#Main
###############################################################
sleep(2)
while keyboard.is_pressed('k') == False:
    #Time to alt-tab
    gameOn = playVerification()
    #At this point the game is now searching a lobby
    print()
    gameOver = verifyIfGameIsOver()
    #At this point the game has ended
    print()
    print()
    
    









#################################################################
                    
        

    
