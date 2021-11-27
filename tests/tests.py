import json
import pyautogui
from time import sleep

# with open('configs.json', 'r') as file:



def searchImage():
    sleep(3)
    # if wallet:
    #     print(wallet)
    # else:
    #     print('Image not found')

searchImage()
# pyautogui.scroll(-2000)
# x = pyautogui.locateCenterOnScreen('images/closeHeroes.png', confidence=0.85)
# pyautogui.click(x) if x else print("NOt found")
x, y = pyautogui.size()
print(pyautogui.size())
pyautogui.moveTo(x/2, y/2)