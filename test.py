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
#네이버이동
url = "https://www.naver.com"
driver.get(url)
time.sleep(1)

#네이버 ID,PW
user_id = 'leejc831'
user_pw = 'qrg258*01'

#네이버접속
elem = driver.find_element(by=By.CLASS_NAME, value="MyView-module__link_login___HpHMW")
elem.click()

#아이디입력
log_ID = driver.find_element(by=By.ID, value="id")
pyperclip.copy(user_id)
log_ID.send_keys(Keys.CONTROL, 'v')

#비밀번호입력
log_PID = driver.find_element(by=By.ID, value="pw")
log_PID.click()
pyperclip.copy(user_pw)
log_PID.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

#로그인 클릭
log_ENT = driver.find_element(by=By.ID, value="log.login")
log_ENT.click()


#예약할 url 이동
#reserv_url = "https://booking.naver.com/booking/3/bizes/2066/items/4313744?startDate=2023-06-29&endDate=2023-06-30"
#i = 0
#while i == 0 :
    
i = 0
while i < 1 : 
    #reserv_url = "https://booking.naver.com/booking/3/bizes/2066/items/4313744?startDate=2023-07-07&endDate=2023-07-09"
    reserv_url = "https://booking.naver.com/booking/3/bizes/2066/items/4313744?startDate=2023-06-29&endDate=2023-06-30"
    driver.get(reserv_url)
    time.sleep(1)

    #다음단계버튼
    next_btn = driver.find_element(By.XPATH, '//*[@id="container"]/bk-accommodation/div/div/div[2]/bk-submit/div/button')
    next_btn.click() 

    # 예약가능여부
    use_yn = driver.find_element(By.XPATH, '/html/body/app/bk-alert/div/div[2]').is_displayed()
    if use_yn : 
        print('다시체크')
    else :
        first_memo = driver.find_element(By.XPATH, '//*[@id="container"]/bk-accommodation/div/div/div[2]/div[2]/div[1]/bk-extra-input/div/div/form/div[1]/div/div/div/div/div[1]')
        first_memo.click()
        first_memo01 = driver.find_element(By.XPATH, '//*[@id="container"]/bk-accommodation/div/div/div[2]/div[2]/div[1]/bk-extra-input/div/div/form/div[1]/div/div/div/div/div[2]/div/ul/li[2]')
        first_memo01.click()
        second_memo = driver.find_element(By.XPATH, '//*[@id="container"]/bk-accommodation/div/div/div[2]/div[2]/div[1]/bk-extra-input/div/div/form/div[2]/div/div/div/div/div[1]')
        second_memo.click() 
        second_memo01 = driver.find_element(By.XPATH, '//*[@id="container"]/bk-accommodation/div/div/div[2]/div[2]/div[1]/bk-extra-input/div/div/form/div[2]/div/div/div/div/div[2]/div/ul/li[2]')
        second_memo01.click() 
        third_memo = driver.find_element(By.XPATH, '//*[@id="container"]/bk-accommodation/div/div/div[2]/div[2]/div[1]/bk-extra-input/div/div/form/div[3]/div/div/div/div/div[1]')
        third_memo.click() 
        third_memo01 = driver.find_element(By.XPATH, '//*[@id="container"]/bk-accommodation/div/div/div[2]/div[2]/div[1]/bk-extra-input/div/div/form/div[3]/div/div/div/div/div[2]/div/ul/li[2]')
        third_memo01.click() 
        forth_memo = driver.find_element(By.XPATH, '//*[@id="container"]/bk-accommodation/div/div/div[2]/div[2]/div[1]/bk-extra-input/div/div/form/div[4]/div/div/div/div/div[1]')
        forth_memo.click() 
        forth_memo01 = driver.find_element(By.XPATH, '//*[@id="container"]/bk-accommodation/div/div/div[2]/div[2]/div[1]/bk-extra-input/div/div/form/div[4]/div/div/div/div/div[2]/div/ul/li[2]')
        forth_memo01.click() 

        driver.find_element(By.XPATH, '//*[@id="name"]').click() 
        driver.find_element(By.XPATH, '//*[@id="tel"]').click() 
        driver.find_element(By.XPATH, '//*[@id="email"]').click() 
        driver.find_element(By.XPATH, '//*[@id="message"]').click() 
        #예약하기 버튼 주석풀면 예약됨
        #driver.find_element(By.XPATH, '//*[@id="container"]/bk-accommodation/div/div/div[2]/bk-submit/div/button/span').click()  
        break
    
    
        

    
