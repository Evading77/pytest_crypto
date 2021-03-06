import os
import sys

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

from common.log import Logger

logger=Logger(logger="conftest.py").getlog()

driver=None
#获取chromedriver.exe路径
base_dir = os.path.join(sys.path[1], '')
driver_path=base_dir+'/drivers/chromedriver.exe'

@pytest.fixture(scope='session',autouse=True)
def browser():
    global driver
    if driver is None:
        driver=Chrome(service=Service(driver_path))
        logger.info("成功得到driver")
    yield driver
    driver.quit()
    logger.info("关闭浏览器，自动化测试结束")