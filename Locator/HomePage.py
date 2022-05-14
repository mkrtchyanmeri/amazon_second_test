from selenium.webdriver.common.by import By
#homepage
allMenu = (By.ID, "nav-hamburger-menu")
signOut = (By.LINK_TEXT, "Sign Out")
cartPressLocator = (By.ID, "nav-cart-count")
search = (By.NAME, "field-keywords")

#searchresultpage
secondProductLocator = (By.XPATH, "(//img[@class ='s-image'])[2]")
addToCartBtn = (By.ID, "add-to-cart-button")