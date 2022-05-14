import time
from Locator.CartPage import *
from Common.CustomFind.FindElementBy import FindElement

class cart_page():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def delete_shopping_cart_first_item(self):
        firstItem = self.findElement.find(*item1)
        firstItem.click()


    def delete_all_items_in_cart(self):
        cartCount = self.findElement.find(*cartPageCartCount)
        numberOfProductsInCart = int(cartCount.text)
        while numberOfProductsInCart > 0:
            deleteButton = self.findElement.find(*cartPageDeleteButton)
            deleteButton.click()
            numberOfProductsInCart -=1
            time.sleep(2)