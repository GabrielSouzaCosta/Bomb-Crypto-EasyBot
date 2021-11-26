import pyautogui
from time import sleep


class Bot():
    def __init__(self):
        # self.login()
        self.x, self.y = pyautogui.size()
        self.put_heroes_to_work()
    

    def check(self, image):
        return pyautogui.locateOnScreen(image, confidence=0.9) 

    def login(self):
        print("Trying to log in...")
        sleep(3)
        pyautogui.press('f5')
        sleep(8)
        # walletCoord = pyautogui.locateCenterOnScreen("images/wallet.png")
        # if walletCoord:
        #     print(walletCoord)
        #     pyautogui.click(walletCoord)

    def put_heroes_to_work(self):
        sleep(3)
        x_button_check = self.check('images/closeHeroes.png')
        heroes_check = self.check('images/heroes.png')
        pyautogui.click(heroes_check) if heroes_check else print('Heroes Image not found')
        sleep(5)
        pyautogui.moveTo(self.x/2, self.y/2)
        pyautogui.scroll(-2000)
        pyautogui.click(self.check('images/work.png'))         
        sleep(2)
        pyautogui.click(x_button_check) if x_button_check else print('Close button image not found')




def main():
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 1.2
    bot = Bot()
    # bot.start()


if __name__ == "__main__":
    main()
