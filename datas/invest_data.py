
user_info_success = [
    {'mobile': '18684720553', 'pwd': 'python'}
]


invest_data_error = [
    {'amount': 1, 'msg': '请输入10的整数倍'},
    {'amount': 12, 'msg': '请输入10的整数倍'},
    {'amount': 100.001, 'msg': '请输入10的整数倍'},
    {'amount': 100.100, 'msg': '请输入10的整数倍'}
]

invest_error_10_data = [
    {'amount': 10, 'msg': '投标金额必须为100的倍数'},
    {'amount': 20, 'msg': '投标金额必须为100的倍数'},
    {'amount': 0, 'msg': '请正确填写投标金额'},
    {'amount': -100, 'msg': '请正确填写投标金额'},
    {'amount': 3000, 'msg': '购买标的金额不能大于标剩余金额'}
]

invest_success_data = [
    {'amount': 100, 'msg': '投标成功！'},
    {'amount': 200, 'msg': '投标成功！'}
]