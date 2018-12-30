from src.page import BasePage
from appium.webdriver.common import mobileby


class HomePage(BasePage.BasePage):
    by = mobileby.MobileBy()
