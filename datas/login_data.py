users_info_error = [
    {"mobile": '', 'pwd': '', 'msg': '请输入手机号'},
    {"mobile": '12', 'pwd': '', 'msg': '请输入正确的手机号'},
    {"mobile": '18684720553', 'pwd': '', 'msg': '请输入密码'}
]

# 测试数据的分组
# 分组的依据
    # 操作步骤是否一致，定位表达式是否一致
user_info_invalidate = [
    {"mobile": '15678923456', 'pwd': 'python', 'msg': '此账号没有经过授权，请联系管理员!'},
    {"mobile": '18684720553', 'pwd': '12', 'msg': '帐号或密码错误!'}
]

user_info_success = [
    {"mobile": '18684720553', 'pwd': 'python'}
]

# 接口步骤
# 1.读取Excel,获取测试数据
# 2.发请求  http_request
# 区别：测试数据不同


