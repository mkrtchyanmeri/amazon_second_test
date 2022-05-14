import time
from Locator.Login import *
from Common.CustomFind.FindElementBy import FindElement

class LoginTC():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def fill_username_fill(self, text):
        username = self.findElement.find(*theUserName)
        username.clear()
        username.send_keys(text)
        time.sleep(3)

    def press_continue_button(self):
        continuebtn = self.findElement.find(*continueButton)
        continuebtn.click()

        try:
            self.findElement.find(*loginValid)
            print("OK")
        except:
            print("There was a problem")
            exit(1)