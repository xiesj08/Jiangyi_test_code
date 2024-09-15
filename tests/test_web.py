import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



'''
另一个接口测试网站
https://jsonplaceholder.typicode.com/

'''
# pytest 初始化base_url网址
@pytest.fixture
def base_url():
    return 'https://www.baidu.com'

# pytest 初始化webdriver
@pytest.fixture
def driver():
    return webdriver.Chrome()

# 测试 GET 打开浏览器
def test_get_url(driver, base_url):
    # url = 'https://jsonplaceholder.typicode.com/posts'
    driver.get(base_url)
    locator = (By.ID, "kw")
    try:
        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        driver.find_element(By.ID, "kw").send_keys('selenium')
        time.sleep(1)
        driver.find_element(By.ID, "su").click()
        time.sleep(1)
    except Exception as e:
        print('e')
        print(f'error: {e}')
    finally:
        driver.quit()

