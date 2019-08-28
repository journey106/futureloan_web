import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from pages.login_page import LoginPage
from pages.home_page import HomePage
from datas.invest_data import user_info_success, invest_data_error, invest_error_100_data
from pages.invest_page import InvestPage
from ddt import ddt, data

# 某一变量，某一个方法，某个类
# 依据python  一切皆为对象
# users_info_error = [
#     ('', '', '请输入手机号'),
#     ('12', '', '请输入正确的手机号'),
#     ('12355', '12', '请输入正确的手机号')
# ]

@ddt
class TestInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.login_page = LoginPage(self.driver)
        self.login_page.login(user_info_success['mobile'], user_info_success['pwd'])
        pass

    def tearDown(self):
        self.driver.refresh()
        # self.login_page.user_elem.clear()
        # self.login_page.pwd_elem.clear()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*invest_data_error)
    def test_invest_01_error(self, invest_data):
        """
        测试投标功能异常
        :return:
        """
        HomePage(self.driver).click_invest_button()
        invest_page = InvestPage(self.driver)
        invest_page.invest_input.send_keys(invest_data['amount'])
        self.assertEqual(invest_page.invest_confirm_button.text, invest_data['msg'])

    @data(*invest_error_100_data)
    def test_login_02_invalidate(self, user_info):
        """
        测试登录输入不合法
        :return:
        """
        self.login_page.login(user_info[0], user_info[1])
        invalidate_msg_element = self.login_page.get_invalidate_result()
        self.assertEqual(invalidate_msg_element.text, user_info[2])

    def test_login_03_success(self):
        self.login_page.login('18684720553', 'python')
        user_element = HomePage(self.driver).user_element
        self.assertEqual(user_element.text, '我的帐户[唐太宗]')


if __name__ == '__main__':
    unittest.main()
    pass