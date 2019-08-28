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
    invest_success_msg_locator = (By.XPATH, "//div[@class='layui-layer-content']//div[@class='capital_font1 note']")
    invest_active_button_locator = (By.XPATH, "//div[@class='layui-layer-content']//button")

    @property
    def invest_input(self):
        '''投标输入框定位'''
        return self.wait_visible_element(self.invest_input_locator)

    @property
    def invest_confirm_button(self):
        '''投标确认按钮'''
        return self.wait_visible_element(self.invest_confirm_button)

    @property
    def invest_success_msg(self):
        '''投资成功提示信息定位'''
        return self.wait_visible_element(self.invest_success_msg_locator)

    def invest_active_button(self):
        '''投资成功弹窗查看并激活按钮'''
        return self.wait_click_element(self.invest_active_button_locator).click()

    

