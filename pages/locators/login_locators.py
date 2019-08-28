from selenium.webdriver.common.by import By

# Keys
class LoginLocaters:
    # 页面元素定位表达式，当需求发生变化，改的地方尽量的少，好找：可维护性强
    error_msg_locator = (By.CSS_SELECTOR, 'div.form-error-info')
    confirm_login_locator = (By.CSS_SELECTOR, 'button.btn-special')
    mobile_locator = (By.NAME, 'phone')
    pwd_locator = (By.NAME, 'password')
    invalidate_msg_locator = (By.CSS_SELECTOR, '.layui-layer-content')