import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait
import unittest
import ddt


@ddt.ddt
class Test_search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 将driver定义成全局变量，可以供下面函数使用
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get("https://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        driver.quit()

    # 测试用例一、二，搜索"内卷"、"躺平"
    @ddt.file_data("../Datas/search_words.yaml")
    def test_search(self, search_word):
        search_ele = (By.ID, "kw")
        click_ele = (By.ID, "su")
        # 因为setUpClass方法浏览器只打开一次，所以我们需要清空搜索栏
        Wait(driver, 5).until(EC.presence_of_element_located(search_ele)).clear()
        # 定位搜索栏，输入搜索词
        Wait(driver, 5).until(EC.presence_of_element_located(search_ele)).send_keys(search_word)
        # 定位搜索按钮，并点击
        Wait(driver, 5).until(EC.presence_of_element_located(click_ele)).click()
        time.sleep(3)
        #获取当前页面title
        title = driver.title
        assert title == f"{search_word}_百度搜索", f"预期结果是‘{search_word}_百度搜索’， 实际结果是‘{title}’"