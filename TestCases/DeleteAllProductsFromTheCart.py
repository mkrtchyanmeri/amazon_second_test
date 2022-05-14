import unittest
from selenium import  webdriver
from Pages.LoginPage import LoginTC
from Pages.SignInPage import PasswordTC
from Pages.CartPage import cart_page
from Pages.HomePage import AmazonHomePageclass
from Common.Variables.signInVariables import *
from Common.GeneralSetUp.GeneralSetUp import GeneralSetUpClass

class AmazonLoginPageTC(unittest.TestCase):
    def setUp(self):
        self.generalSetUp = GeneralSetUpClass()
        self.driver = webdriver.Chrome("..\\Common\\Drivers\\chromedriver.exe")
        self.loginpage = LoginTC(self.driver)
        self.password = PasswordTC(self.driver)
        self.homepage = AmazonHomePageclass(self.driver)
        self.cart = cart_page(self.driver)

    def test_LoginTest(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginpage.fill_username_fill(username)
        self.loginpage.press_continue_button()
        self.password.fill_password_fill(password)
        self.password.check_checkbox()
        self.password.press_signin_button()
        self.homepage.press_cart()
        self.cart.delete_all_items_in_cart()
        self.homepage.sign_out()

    def tearDown(self):
        self.driver.close()