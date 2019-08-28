from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from pages.base_page import BasePage


class InvestPage(BasePage):
    url = 'http://120.78.128.25:8765'
    invest_input_locator = (By.CSS_SELECTOR, '.form-control')
    invest_confirm_locator = (By.CSS_SELECTOR, ".btn-special']")

    @property
    def invest_input(self):
        '''投标输入框定位'''
        return self.wait_visible_element(self.invest_input_locator)

    @property
    def invest_confirm_button(self):
        '''投标确认按钮'''
        return self.wait_visible_element(self.invest_confirm_button)

