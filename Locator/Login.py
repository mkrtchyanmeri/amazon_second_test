from selenium.webdriver.common.by import By

trr = (By.XPATH, "ap_change_login_claim")
theUserName = (By.NAME, "email")
continueButton = (By.CLASS_NAME, "a-button-input")
failUserName = (By.CLASS_NAME, "a-list-item")
loginValid = (By.LINK_TEXT, "Change")
