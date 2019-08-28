import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from pages.login_page import LoginPage
from pages.home_page import HomePage
from datas.login_data import users_info_error, user_info_invalidate
from ddt import ddt, data

# 某一变量，某一个方法，某个类
# 依据python  一切皆为对象
# users_info_error = [
#     ('', '', '请输入手机号'),
#     ('12', '', '请输入正确的手机号'),
#     ('12355', '12', '请输入正确的手机号')
# ]

@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.login_page = LoginPage(cls.driver)

    def setUp(self):
        pass

    def tearDown(self):
        self.driver.refresh()
        # self.login_page.user_elem.clear()
        # self.login_page.pwd_elem.clear()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*users_info_error)
    def test_login_01_error(self, user_info):
        """
        测试登录功能异常
        :return:
        """
        self.login_page.login(user_info[0], user_info[1])
        error_msg_element = self.login_page.get_actual_result()
        self.assertEqual(error_msg_element.text, user_info[2])

    @data(*user_info_invalidate)
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