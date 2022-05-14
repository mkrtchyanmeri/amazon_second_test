from Locator.HomePage import *
from Common.CustomFind.FindElementBy import FindElement
from selenium.webdriver.common.keys import Keys

class AmazonHomePageclass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def press_cart(self):
        AmazonCart = self.findElement.find(*cartPressLocator)
        AmazonCart.click()

    def sign_out(self):
        allMenuIcon = self.findElement.find(*allMenu)
        allMenuIcon.click()
        scrollDown = self.driver.execute_script("window,scrollBy(0,-50)""")
        signOutFrom = self.findElement.find(*signOut)
        signOutFrom.click()

    def add_to_cart_one_product(self):
        serchFill = self.findElement.find(*search)
        serchFill.clear()
        serchFill.click()
        serchFill.send_keys("t shirt dress")
        serchFill.send_keys(Keys.ENTER)
        scrollDown = self.driver.execute_script("window,scrollBy(0,-20)""")
        img = self.findElement.find(*secondProductLocator)
        img.click()
        btn2 = self.findElement.find(*addToCartBtn)
        btn2.click()