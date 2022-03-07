#
import time

import allure
from pytest_bdd import when, parsers, then, scenario
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_page import BasePage
from common.log import Logger

logger=Logger(logger="test_crypto.py").getlog()

@when(parsers.parse("谷歌访问{url}"))
@allure.step("谷歌访问https://crypto.com/exchange/markets")
def go_to_url(url,browser):
    browser.get(url)
    logger.info("打开浏览器，跳转至https://crypto.com/exchange/markets")
    browser.maximize_window()

@when("点击ZIL/USDT")
@allure.step("点击ZIL/USDT")
def click_trade(browser):
    js = "window.scrollTo(0,100000)"
    browser.execute_script(js)
    logger.info("拖动浏览器到最底部")
    click_target = browser.find_element(By.XPATH, "//img[@alt='ZIL']")
    result = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(click_target))
    if result!=False:
        browser.execute_script("arguments[0].click();", result)
        logger.info("找到元素，并点击跳转到目标页面")
    else:
        logger.error("元素不可点击")

@then("进入到了ZIL/USDT的交易页面")
@allure.step("进入到了ZIL/USDT的交易页面")
def zil_page(browser):
    time.sleep(3)
    js = "window.scrollTo(0,0)"
    browser.execute_script(js)
    logger.info("将页面拖到最上方")
    exec="ZIL/USDT"
    logger.info("页面需要断言判断的实际值为：{}".format(exec))
    target_ele = browser.find_element(By.XPATH, "//div[@class='toggle']")
    act = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(target_ele)).text
    logger.info("页面需要断言判断的实际值为：{}".format(act))
    #断言
    if exec in act:
        logger.info("成功跳转到了ZIL/USDT的交易页面")
        BasePage(browser).save_screen_allure()
        logger.info("用例运行成功并截图保存")
    else:
        logger.error("断言失败，预期值为{0}，实际值为{1}".format(exec,act))

@scenario("../features/crypto.feature","场景1：正常跳转到到ZIL/USDT的交易页面")
def test_crypt():
    pass



