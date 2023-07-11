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
import ctypes
import cv2
import os

mp3_file = "C:/Users/dlwoc/OneDrive/Desktop/aa.mp3"

if ctypes.windll.shell32.IsUserAnAdmin(): 
    print('관리자권한으로 실행된 프로세스입니다.')
else:
    print('일반권한으로 실행된 프로세스입니다.')

driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
#yes24 이동
url = "http://ticket.yes24.com/Special/46234"

def play_mp3(file_path):
    os.startfile(file_path)

def macro():
    i = 0
    while i==0 :
        driver.switch_to.default_content()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="2023-10-20"]'))) #페이지로딩(최대300초)
        driver.find_element(By.XPATH, '//*[@id="2023-10-21"]').click()
        time.sleep(0.5)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnSeatSelect"]'))) #페이지로딩(최대300초)
        driver.find_element(By.XPATH, '//*[@id="btnSeatSelect"]').click()
        time.sleep(0.5)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divFlash"]/iframe'))) #페이지로딩(최대300초)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="divFlash"]/iframe')) # iframe 이동
        seat_array = []
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_P석"]/em'))) #페이지로딩(최대300초)
        seat_array.append(driver.find_element(By.XPATH, '//*[@id="grade_P석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_R석"]/em'))) #페이지로딩(최대300초)
        seat_array.append(driver.find_element(By.XPATH, '//*[@id="grade_R석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_스탠딩석"]/em'))) #페이지로딩(최대300초)
        seat_array.append(driver.find_element(By.XPATH, '//*[@id="grade_스탠딩석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_S석"]/em'))) #페이지로딩(최대300초)
        seat_array.append(driver.find_element(By.XPATH, '//*[@id="grade_S석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_A석"]/em'))) #페이지로딩(최대300초)
        seat_array.append(driver.find_element(By.XPATH, '//*[@id="grade_A석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_B석"]/em'))) #페이지로딩(최대300초)
        seat_array.append(driver.find_element(By.XPATH, '//*[@id="grade_B석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_C석"]/em'))) #페이지로딩(최대300초)
        seat_array.append(driver.find_element(By.XPATH, '//*[@id="grade_C석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_D석"]/em'))) #페이지로딩(최대300초)
        seat_array.append(driver.find_element(By.XPATH, '//*[@id="grade_D석"]/em').text)

        for z in seat_array :
            if(z == "(0석)") :
                continue
            else :
                play_mp3(mp3_file)
                print("토요일 좌석발생")
                seat = 0
                while seat < 1 :
                    print("매크로재시작 ` 키")
                    k = 0
                    while k < 1 :
                        if keyboard.read_key() == "`":
                            macro()
                            break
                
        
        print("토요일 좌석 현재없음")

        # 토요일
        #time.sleep(1)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form1"]/div[3]/div[2]/div/div[2]/p[1]/a[1]/img'))) #페이지로딩(최대300초)
        driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/div[2]/div/div[2]/p[1]/a[1]/img').click()
        #time.sleep(0.5)
        driver.switch_to.default_content()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="2023-10-21"]'))) #페이지로딩(최대300초)
        driver.find_element(By.XPATH, '//*[@id="2023-10-22"]').click()
        time.sleep(0.5)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnSeatSelect"]'))) #페이지로딩(최대300초)
        driver.find_element(By.XPATH, '//*[@id="btnSeatSelect"]').click()
        time.sleep(0.5)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divFlash"]/iframe'))) #페이지로딩(최대300초)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="divFlash"]/iframe')) # iframe 이동

        seat_array2 = []
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_P석"]/em'))) #페이지로딩(최대300초)
        seat_array2.append(driver.find_element(By.XPATH, '//*[@id="grade_P석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_R석"]/em'))) #페이지로딩(최대300초)
        seat_array2.append(driver.find_element(By.XPATH, '//*[@id="grade_R석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_스탠딩석"]/em'))) #페이지로딩(최대300초)
        seat_array2.append(driver.find_element(By.XPATH, '//*[@id="grade_스탠딩석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_S석"]/em'))) #페이지로딩(최대300초)
        seat_array2.append(driver.find_element(By.XPATH, '//*[@id="grade_S석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_A석"]/em'))) #페이지로딩(최대300초)
        seat_array2.append(driver.find_element(By.XPATH, '//*[@id="grade_A석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_B석"]/em'))) #페이지로딩(최대300초)
        seat_array2.append(driver.find_element(By.XPATH, '//*[@id="grade_B석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_C석"]/em'))) #페이지로딩(최대300초)
        seat_array2.append(driver.find_element(By.XPATH, '//*[@id="grade_C석"]/em').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade_D석"]/em'))) #페이지로딩(최대300초)
        seat_array2.append(driver.find_element(By.XPATH, '//*[@id="grade_D석"]/em').text)

        for x in seat_array :
            if(x == "(0석)") :
                continue
            else :
                play_mp3(mp3_file)
                print("일요일 좌석발생")
                seat = 0
                while seat < 1 :
                    print("매크로재시작 ` 키")
                    k = 0
                    while k < 1 :
                        if keyboard.read_key() == "`":
                            macro()
                            break

        print("일요일 좌석 현재없음")
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divFlash"]/iframe'))) #페이지로딩(최대300초)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="divFlash"]/iframe')) # iframe 이동
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form1"]/div[3]/div[2]/div/div[2]/p[1]/a[1]/img'))) #페이지로딩(최대300초)
        driver.find_element(By.CSS_SELECTOR, '#form1 > div.bx_seatbg > div.seatinfo > div > div.btn > p:nth-child(1) > a:nth-child(1) > img').click()

    
 
driver.get(url)

#로그인
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consiceLogin"]'))) #페이지로딩(최대300초)
driver.find_element(By.XPATH, '//*[@id="consiceLogin"]').click()
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="SMemberID"]'))) #페이지로딩(최대300초)
driver.find_element(By.XPATH, '//*[@id="SMemberID"]').send_keys('leejc831')
driver.find_element(By.XPATH, '//*[@id="SMemberPassword"]').send_keys('qrg258*01')
driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()

WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainForm"]/div[9]/div/div[4]/a[4]'))) #페이지로딩(최대300초)
driver.find_element(By.XPATH, '//*[@id="mainForm"]/div[9]/div/div[4]/a[4]').click()
driver.switch_to.window(driver.window_handles[-1])

while True:
    try :
        macro()
    except :
        seat = 0
        while seat < 1 :
            print("매크로재시작 ` 키")
            k = 0
            while k < 1 :
                if keyboard.read_key() == "`":
                    break
            break

