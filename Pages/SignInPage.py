import time
from Locator.SignIn import *
from Common.CustomFind.FindElementBy import FindElement

class PasswordTC():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def fill_password_fill(self, passwordText):
        password = self.findElement.find(*thePassword)
        password.clear()
        password.send_keys(passwordText)

    def check_checkbox(self):
        check = self.findElement.find(*checkbox)
        check.click()
        time.sleep(3)

    def press_signin_button(self):
        signIn = self.findElement.find(*signInAmazon)
        signIn.click()

        try:
            self.findElement.find(*amazonLogo)
            print("OK")
        except:
            print("There was  problem")
            exit(2)
