from PIL.ImageOps import grayscale
import pyautogui
from time import sleep


class Bot():
    def __init__(self):
        self.x, self.y = pyautogui.size()
        print('Bot waking up...')
        self.main_chain()
    
    def main_chain(self):
        while True:
            self.login()
            heroes_work = self.put_heroes_to_work()
            if heroes_work != False:
                self.treasure_hunt()

    def check(self, image, confidence=0.8):
        return pyautogui.locateOnScreen(image, confidence=confidence) 

    def login(self):
        print("Trying to log in...")
        sleep(3)
        self.refresh_page()
        sleep(10)
        wallet_check = self.check('images/wallet.png')
        pyautogui.click(wallet_check) if wallet_check else print('Wallet button not found')
        # sleep(2)
        # fox_check = self.check('images/metamask.png')
        # pyautogui.click(fox_check) if fox_check else print('Metamask fox not found')
        sleep(8)
        sign_check = self.check('images/sign.png', confidence=0.6)
        pyautogui.click(sign_check, clicks=3, interval=0.5) if sign_check else print('Sign button not found')
        sleep(30)

    def put_heroes_to_work(self):
        print("Putting your slaves to work")
        sleep(3)
        heroes_check = self.check('images/heroes.png')
        if heroes_check: 
            pyautogui.click(heroes_check) 
        else:
            print("Maybe your not in the main screen, trying to enter again")
            return False

        sleep(10)
        scroll_x, scroll_y = pyautogui.locateCenterOnScreen('images\scroll.PNG')
        for t in range(4):
            pyautogui.click(scroll_x, scroll_y)
            pyautogui.dragTo(scroll_x, 200, duration=1.5)   
        self.click_work_button()
        sleep(1.2)
        x_button_check = self.check('images/closeHeroes.png')
        pyautogui.click(x_button_check, clicks=2, interval=1) if x_button_check else print('Close button image not found')
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
        pyautogui.click(treasure_check, clicks=2, interval=1) if treasure_check else print('Treasure hunt not found')
        while True:
            sleep(120)
            pyautogui.click()
            self.refresh_treasure()
            refresh_count += 1
            if refresh_count >= 10 or self.not_found_count >= 2:
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
        sleep(1.5)
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
    pyautogui.PAUSE = 1.2
    bot = Bot()


if __name__ == "__main__":
    main()
