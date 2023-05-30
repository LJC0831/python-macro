import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyperclip



driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
#인터파크 이동
url = "https://ticket.interpark.com/Gate/TPLogin.asp"
driver.get(url)
time.sleep(1)

driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']")) # iframe 이동
userId = driver.find_element(By.ID, 'userId')
userId.send_keys('leejc831') # 로그인 할 계정 id
userPwd = driver.find_element(By.ID, 'userPwd')
userPwd.send_keys('qrg258*001') # 로그인 할 계정의 패스워드
userPwd.send_keys(Keys.ENTER)


url2 = 'http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '23007423'
driver.get(url2)


# 예매하기 버튼 클릭
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[2]/a[1]').click()


# 예매하기 눌러서 새창이 뜨면 포커스를 새창으로 변경
#driver.switch_to.window(driver.window_handles[1])
#driver.get_window_position(driver.window_handles[1])
