from PIL.ImageOps import grayscale
import pyautogui
from time import sleep
import random

rg = random.uniform
smaller_time = [0.9, 1.2]
small_time = [2.1, 3.9]
medium_time = [7.1, 7.5]
large_time = [8.1, 11.2]
larger_time = [24.3, 30.4]
big_time = [380.6, 423.7]



class Bot():
    def __init__(self):
        pyautogui.PAUSE = random.uniform(1.1, 1.4)
        self.x, self.y = pyautogui.size()
        print('Bot waking up...')
        print('ctrl + c to kill Bot')
        self.main_chain()
    
    def main_chain(self):
        sleep(rg(*medium_time))
        while True:
            self.login()
            heroes_work = self.put_heroes_to_work()
            if heroes_work != False:
                self.treasure_hunt()

    def check(self, image, confidence=0.8):
        return pyautogui.locateOnScreen(image, confidence=confidence) 

    def login(self):
        print("Trying to log in...")
        sleep(rg(*small_time))
        self.refresh_page()
        sleep(rg(*large_time))
        wallet_check = self.check('images/wallet.png')
        pyautogui.click(wallet_check) if wallet_check else print('Wallet button not found')
        sleep(rg(*medium_time))
        sign_check = self.check('images/sign.png', confidence=0.8)
        pyautogui.click(sign_check, clicks=3, interval=0.5) if sign_check else print('Sign button not found')
        sleep(rg(*larger_time))

    def put_heroes_to_work(self):
        print("Putting your slaves to work")
        sleep(rg(*small_time))
        heroes_check = self.check('images/heroes.png')
        if heroes_check: 
            pyautogui.click(heroes_check) 
        else:
            print("Maybe your not in the main screen, trying to enter again")
            return False

        sleep(rg(*large_time))
        work_all = pyautogui.locateCenterOnScreen("images/all.png", confidence=0.8)
        pyautogui.click(work_all)
        # scroll_x, scroll_y = pyautogui.locateCenterOnScreen('/home/gcosta/Documents/Projects/Bomb-Crypto-EasyBot/images/scroll.png')
        # for t in range(3):
        #     pyautogui.click(scroll_x, scroll_y)
        #     pyautogui.dragTo(scroll_x, 200, duration=rg(*smaller_time))   
        # self.click_work_button()
        sleep(rg(*small_time))
        x_button_check = self.check('images/closeHeroes.png')
        pyautogui.click(x_button_check, clicks=2, interval=rg(*smaller_time)) if x_button_check else print('Close button image not found')
        return True

    def click_work_button(self):
        work_button = pyautogui.locateOnScreen('images/work.png', confidence=0.9, grayscale=True)
        while work_button:
            pyautogui.click(work_button)
            pyautogui.click()
            work_button = pyautogui.locateOnScreen('images/work.png', confidence=0.9, grayscale=True)

    def treasure_hunt(self):
        print('Going to Treasure Hunt')
        refresh_count = 0
        self.not_found_count = 0
        treasure_check = self.check('images/treasureScreen.png')
        pyautogui.click(treasure_check, clicks=2, interval=rg(*smaller_time)) if treasure_check else print('Treasure hunt not found')
        while True:
            refresher = random.randint(4, 7)
            sleep(rg(*big_time))
            pyautogui.click()
            self.refresh_treasure()
            refresh_count += 1
            if refresh_count >= refresher or self.not_found_count >= 2:
                self.refresh_page()
                break


    def refresh_treasure(self):
        print('Refreshing treasure hunt screen')
        back_check = self.check('images/back.png')
        if back_check:
            pyautogui.click(back_check) 
        else:
            print('Back icon not found')
            self.not_found_count += 1
        sleep(rg(*small_time))
        treasure_check = self.check('images/treasureScreen.png')
        pyautogui.click(treasure_check, clicks=2, interval=1) if treasure_check else print('Treasure hunt not found')

    def refresh_page(self):
        print("Doing a hard refresh to avoid possible errors")
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.press('r')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('ctrl')

def main():
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = random.uniform(1.1, 1.4)
    bot = Bot()


if __name__ == "__main__":
    main()
