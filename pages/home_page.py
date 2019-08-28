from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from pages.base_page import BasePage


class HomePage(BasePage):
    url = 'http://120.78.128.25:8765'
    invest_locator = (By.CSS_SELECTOR, '.btn-special')
    user_locator = (By.XPATH, "//a[@href='/Member/index.html']")

    @property
    def user_element(self):
        """用户昵称"""
        return self.wait_presence_element(self.user_locator)

    @property
    def invest_button(self):
        '''首页投标按钮'''
        return self.wait_click_element(self.invest_locator)

    def click_invest_button(self):
        '''点击首页投标按钮'''
        return self.invest_button.click()

