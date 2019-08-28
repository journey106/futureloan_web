import os
# from pathlib import path


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_IMG = os.path.join(BASE_PATH, 'log_img')

LOG_DIR = os.path.join(BASE_PATH, 'logs')

CONF_DIR = os.path.join(BASE_PATH, 'confs')
CONF_FILE_PATH = os.path.join(CONF_DIR, 'cases.conf')
CONF_USER_FILE_PATH = os.path.join(CONF_DIR, 'users.conf')

if os.path.exists(LOG_IMG):
    pass
else:
    os.mkdir(LOG_IMG)

