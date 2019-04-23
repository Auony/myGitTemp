from selenium import webdriver
from time import sleep
import os
#######################################
driver = webdriver.Chrome()
driver,maximize_window()
driver.implicitly_wait(26)
url = "https://www.baidu.com/"
driver.get(url)
