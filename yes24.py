import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import easyocr
import keyboard

driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
#yes24 이동
url = "http://ticket.yes24.com/Perf/44653" 
driver.get(url)

#로그인
# WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consiceLogin"]'))) #페이지로딩(최대300초)
# driver.find_element(By.XPATH, '//*[@id="consiceLogin"]').click()
# WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="SMemberID"]'))) #페이지로딩(최대300초)
# driver.find_element(By.XPATH, '//*[@id="SMemberID"]').send_keys('leejc831')
# driver.find_element(By.XPATH, '//*[@id="SMemberPassword"]').send_keys('qrg258*01')
# driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()


a = 0
while a < 1 :
    if keyboard.read_key() == "`":  # ` 키로 매크로시작
        break
#예매하기
i = 0
while i < 1 : 
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consiceLogin"]'))) #페이지로딩(최대300초)
    try :
        use_yn = driver.find_element(By.CSS_SELECTOR, '#mainForm > div.renew-wrap.rw2 > div > div.rn-05 > a.rn-bb03').text
    except :
        use_yn = 0
    print("==========================")
    print(use_yn)
    if(use_yn == "예매하기") :
        driver.find_element(By.CSS_SELECTOR, '#mainForm > div.renew-wrap.rw2 > div > div.rn-05 > a.rn-bb03').click()
        #좌석영역잡기
        seat = 0
        while seat < 1 :
            print("시간 | 좌석선택완료 버튼 좌표 가져오기\n 마우스 가져다 대고 순서대로 a, b 를 누르면 됨\n")
            k = 0
            while k < 1 :
                if keyboard.read_key() == "1":
                    xxx, yyy = pyautogui.position()
                    break
            l = 0
            pyautogui.moveTo(xxx , yyy , 0.01) # 좌석상세 마우스이동
            pyautogui.click()
            while l < 1 :
                if keyboard.read_key() == "2":
                    selx, sely = pyautogui.position()
                    break
            pyautogui.moveTo(selx , sely , 0.01) # 좌석상세 마우스이동
            pyautogui.click()
            driver.switch_to.window(driver.window_handles[-1])
            driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="divFlash"]/iframe')) # iframe 이동
            driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/div[2]/div/div[2]/p[2]/a').click()  # 예약버튼
            try :
                da = Alert(driver)
                da.accept()
                time.sleep(1)
            except :
                print("좌석선택완료")
                break

        # 매수선택
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StepCtrlBtn03"]/a[2]'))) #페이지로딩(최대300초) 
        time.sleep(1)
        pyautogui.moveTo(1005 , 504 , 0.01) 
        pyautogui.click()
        ############### 세팅필요 #####################
        pyautogui.moveTo(1005 , 552 , 0.01) # 2장기준
        ############### 세팅필요 #####################
        pyautogui.click()
        driver.find_element(By.XPATH, '//*[@id="StepCtrlBtn03"]/a[2]').click()  # 다음단계

        # 수령방법
        time.sleep(1)
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StepCtrlBtn04"]/a[2]'))) #페이지로딩(최대300초) 
        driver.find_element(By.XPATH, '//*[@id="StepCtrlBtn04"]/a[2]').click()  # 다음단계

        # 결재방법
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rdoPays2"]'))) #페이지로딩(최대300초) 
        driver.find_element(By.XPATH, '//*[@id="rdoPays2"]').click()  # 신용카드
        driver.find_element(By.XPATH, '//*[@id="cbxAllAgree"]').click()  # 동의박스
        driver.find_element(By.XPATH, '//*[@id="StepCtrlBtn05"]/a[2]').click()  # 다음단계
        
        break
    else :
        print("아직예매불가")
        driver.refresh()
