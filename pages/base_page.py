from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from handle_log import do_logger
import config
import os, time


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver
        self.driver.maximize_window()

    def wait_click_element(self, locator):

        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    def wait_visible_element(self, locator):

        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    def wait_presence_element(self, locator):
        try:
            return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        except (NoSuchElementException, TimeoutException) as e:
            do_logger.error('定位出错:{}'.format(e))
            # 保存错误截图
            self.save_screenshot()

    def generate_screen_file_name_by_ts(self):
        '''生成文件名'''
        local_time = time.strftime('%Y-%m-%D-%H-%M-%S', time.localtime())
        return ''.join((local_time, '.png'))

    def save_screenshot(self):
        '''自动化保存截图'''
        picture_dir = config.LOG_IMG
        file_name = os.path.join(picture_dir, self.generate_screen_file_name_by_ts())
        self.driver.save_screenshot(file_name)

    def get_url(self):
        return self.driver.current_url

    def switch_window(self, window_name):
        pass

    def switch_iframe(self, frame_reference):
        pass

    def switch_alert(self):
        pass

    # 鼠标操作
    # 滚动窗口
    # 键盘操作
    def double_click(self, elem):
        '''双击'''
        action_chains = ActionChains(self.driver)
        action_chains.double_click(elem).perform()

    def context_click(self, elem):
        '''右击'''
        action_chains = ActionChains(self.driver)
        action_chains.context_click(elem).perform()

    def scroll_window(self, width, height):
        '''滚动窗口'''

        return self.driver.execute_script("window.scrollTo({}, {})".format(width, height))

    # 上传文件
    def upload_file(self, elem):
        # 判断 ， input  elem.send_keys()
        # pywin32
        pass


