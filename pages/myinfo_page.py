from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MyInfoPage(BasePage):
    '''个人中心页面类'''
    url = 'http://120.78.128.25:8765/Member/index'
    availabe_money_element_locator = (By.CSS_SELECTOR, '.color_sub')
    trading_frozen_money_element_locator = (By.XPATH, "//li[@class='color_sub']/following-sibling::li[2]")
    invest_detail_tab_element_locator = (By.XPATH, "//div[@class='px_card']/div[2]")
    invest_project_table_element_locator = (By.XPATH, "//div[@class='deal_manage']/div[3]/table[1]")

    def availabe_money_element(self):
        '''可用余额定位'''
        return self.wait_presence_element(self.availabe_money_element_locator)

    def trading_frozen_money_element(self):
        '''交易冻结金额定位'''
        return self.wait_presence_element(self.trading_frozen_money_element_locator)

    def invest_detail_ta_element(self):
        '''投资项目页签'''
        return self.wait_click_element(self.invest_detail_tab_element_locator)

    def invest_project_table_element(self):
        '''投资项目列表'''
        return self.wait_visible_element(self.invest_project_table_element_locator)

    def invest_project_table_trs(self):
        '''投资项目列表行数'''
        return len(self.invest_project_table_element.find_elements('tr'))

