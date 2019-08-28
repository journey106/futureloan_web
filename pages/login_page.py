import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from pages.locators.login_locators import LoginLocaters
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_url = 'http://120.78.128.25:8765/Index/login.html'
    # 页面元素定位表达式，当需求发生变化，改的地方尽量的少，好找：可维护性强
    # error_msg_locator = (By.CSS_SELECTOR, 'div.form-error-info')
    # confirm_login_locator = (By.CSS_SELECTOR, 'button.btn-special')
    # mobile_locator = (By.NAME, 'phone')
    # pwd_locator = (By.NAME, 'password')
    # invalidate_msg_locator = (By.CSS_SELECTOR, '.layui-layer-content')

    def get_actual_result(self):
        '''获取实际结果'''
        return self.driver.find_element(*LoginLocaters.error_msg_locator)

    def get_invalidate_result(self):
        '''获取没有经过授权的等待'''
        return self.wait_visible_element(LoginLocaters.invalidate_msg_locator)

    @property
    # def user_elem(self):
    def user_elem(self) -> WebElement:
        '''定位用户'''
        return self.wait_presence_element(LoginLocaters.mobile_locator)

    @property
    # def pwd_elem(self):
    def pwd_elem(self) -> WebElement:
        '''定位密码'''
        return self.wait_presence_element(LoginLocaters.pwd_locator)

    # def login(self, username:str, password):
    def login(self, username, password):
        print('---------------')
        self.driver.get(self.login_url)
        # 隐式等待
        # user_element = self.wait_presence_element((By.NAME, 'phone'))
        # pwd_element = self.wait_presence_element((By.NAME, 'password'))
        self.user_elem.send_keys(username)
        self.pwd_elem.send_keys(password)

        # self.driver.find_element_by_css_selector('button.btn-special')
        e = self.wait_click_element(LoginLocaters.confirm_login_locator)
        e.click()



