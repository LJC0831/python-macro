import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import pyperclip
import os

mp3_file = "C:/Users/dlwoc/OneDrive/Desktop/aa.mp3"

chrome_driver_path = r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#네이버 ID,PW
user_id = 'leejc831'
user_pw = 'qrg258*001'
url = "https://tickets.interpark.com/special/sports/promotion?seq=43" #삼성야구
url2 = "https://poticket.interpark.com/SportsBook/BookMain.asp?GroupCode=24013822&GoodsCode=24013822&PlayDate=20241020&PlaySeq=001&PlayTime=1400&Tiki=&BizCode=WEBBR&SessionId=24013822_M0000006340211728998958&SIDBizCode=WEBBR"
driver.get(url)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ent-ticket__header"]/div[2]/div[1]/div/div[4]/a[1]'))) #로그인
driver.find_element(By.XPATH, '//*[@id="ent-ticket__header"]/div[2]/div[1]/div/div[4]/a[1]').click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userId"]'))) #로그인

#아이디 입력
log_ID = driver.find_element(By.XPATH, '//*[@id="userId"]')
pyperclip.copy(user_id)
log_ID.send_keys(Keys.CONTROL, 'v')

#비밀번호입력
log_PID = driver.find_element(By.XPATH, '//*[@id="userPwd"]')
log_PID.click()
pyperclip.copy(user_pw)
log_PID.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="btn_login"]').click()

def play_mp3(file_path):
    os.startfile(file_path)

def check():
    try:

        try:
            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divRecaptcha"]')))
            div_recaptcha = driver.find_element(By.XPATH, '//*[@id="divRecaptcha"]')
            style = div_recaptcha.get_attribute('style')

            # style 속성 확인
            if 'display: none' in style:
                print("캡챠비활성화")
            else:
                print("캡챠처리필요")
                print("매크로 ` 누르면 재시작")
                each = 0
                while each < 1 :
                        if keyboard.read_key() == "`":
                            break
        except Exception as e:
            print(f"Error: {e}")

        
        # 예: iframe 내에서 body 태그의 텍스트를 가져오기
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[11]/span[2]')))
        seat01 = int(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[11]/span[2]').text.replace('석', '').strip())  #3루 익사이팅석
        seat02 = int(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[13]/span[2]').text.replace('석', '').strip())  #블루존
        seat03 = int(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[15]/span[2]').text.replace('석', '').strip())  #3루 내야지정석
        seat04 = int(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[25]/span[2]').text.replace('석', '').strip())  #3루 외야지정석
        seat05 = int(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[14]/span[2]').text.replace('석', '').strip())  #원정응원석
        seat06 = int(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[5]/span[2]').text.replace('석', '').strip())  #3루 테이블석2인
        seat07 = int(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[12]/span[2]').text.replace('석', '').strip())  #1루 익사이팅석
        
        print('자리체크1')
        if seat01 > 1 :
            print("3루 익사이팅석 자리발생")
            driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[11]/span[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/a[1]/img'))) #자동배정
            play_mp3(mp3_file)
            time.sleep(10000)
        elif seat02 > 1 :
            print("블루존 자리발생")
            driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[13]/span[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/a[1]/img'))) #자동배정
            play_mp3(mp3_file)
            time.sleep(10000)
        elif seat03 > 1 :
            print("3루내야지장석 자리발생")
            driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[15]/span[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/a[1]/img'))) #자동배정
            play_mp3(mp3_file)
            time.sleep(10000)
        elif seat04 > 1  :
            print("3루 외야지정석 자리발생")
            driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[25]/span[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/a[1]/img'))) #자동배정
            play_mp3(mp3_file)
            time.sleep(10000)
            
        elif seat05 > 1  :
            print("원정응원석 자리발생")
            driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[14]/span[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/a[1]/img'))) #자동배정
            play_mp3(mp3_file)
            time.sleep(10000)
        elif seat06 > 1  :
            print("3루 테이블석2인자리발생")
            driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[5]/span[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/a[1]/img'))) #자동배정
            play_mp3(mp3_file)
            time.sleep(10000)
        elif seat07 > 1  :
            print("1루 익사이팅석 자리발생")
            driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/a[12]/span[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/a[1]/img'))) #자동배정
            play_mp3(mp3_file)
            time.sleep(10000)
        else :
            print("자리없음")
            driver.get(url2)
            time.sleep(1)
            driver.switch_to.frame("ifrmSeat")
        time.sleep(0.5)

    except Exception as e:
        print(f'오류 발생: {e}')
        macro02()

def macro02():
    print("macro2 시작")
    each01 = 0
    while each01 < 1 :              
        check()
    

def macro01():

    try :
        each = 0
        print("매크로 ` 누르면 재시작")
        while each < 1 :
                if keyboard.read_key() == "`":
                    break
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/div[2]/ul/li[5]/div/div[2]/button'))) # 블루존Z
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/div[2]/ul/li[5]/div/div[2]/button').click()

        each = 0
        print("매크로 1 누르면 재시작")
        while each < 1 :
                if keyboard.read_key() == "1":
                    break
        time.sleep(1)


        driver.switch_to.frame("ifrmSeat")
        macro02()
    except Exception as e:
        print(f'오류 발생: {e}')


macro01()
