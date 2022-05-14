import unittest
from Pages.LoginPage import LoginTC
from Pages.SignInPage import PasswordTC
from Pages.HomePage import AmazonHomePageclass
from Common.Variables.signInVariables import *
from Common.GeneralSetUp.GeneralSetUp import GeneralSetUpClass


class AmazonLoginPageTC(unittest.TestCase,GeneralSetUpClass):
    def setUp(self):
        self.general_set_up()
        self.loginpage = LoginTC(self.driver)
        self.password = PasswordTC(self.driver)
        self.signOut = AmazonHomePageclass(self.driver)

    def test_LoginTest(self):
        self.driver.get("https://www.amazon.com/gp/sign-in.html")
        self.loginpage.fill_username_fill(username)
        self.loginpage.press_continue_button()
        self.password.fill_password_fill(password)
        self.password.check_checkbox()
        self.password.press_signin_button()
        self.signOut.sign_out()


    def tearDown(self):
        self.driver.close()