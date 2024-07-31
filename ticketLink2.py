import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ctypes
import keyboard
import os

mp3_file = "C:/Users/dlwoc/OneDrive/Desktop/aa.mp3"

chrome_driver_path = r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
#티켓링크 이동
#url = "https://www.ticketlink.co.kr" #Kt야구
url = "https://www.ticketlink.co.kr/sports/baseball/57#reservation" #삼성야구
driver.get(url)


def play_mp3(file_path):
    os.startfile(file_path)
def check():
    try :
        print('check시작')
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[2]/div[1]/div[2]/a'))) #새로고침
        driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[2]/div[1]/div[2]/a').click()  #
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seat_grade_96160"]/a/div/span[2]/span[1]'))) # 블루존
        seat01 = int(driver.find_element(By.XPATH, '//*[@id="seat_grade_96160"]/a/div/span[2]/span[1]').text) #블루존
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seat_grade_96161"]/a/div/span[2]/span[1]'))) # 내야지정석
        seat02 = int(driver.find_element(By.XPATH, '//*[@id="seat_grade_96161"]/a/div/span[2]/span[1]').text) #블루존
        
        
        print('자리체크1')
        if seat01 > 1 :
            print("블루존 자리발생")
            play_mp3(mp3_file)
            time.sleep(10000)
        elif seat01 > 1:
            print("내야지정석 자리발생")
            play_mp3(mp3_file)
            time.sleep(10000)
        else :
             print(f"블루존자리: {seat01}")
             print(f"내야지정석: {seat02}")
             print("자리없음")
             time.sleep(0.5)
    except Exception as e:
        print(f'오류 발생: {e}')
        # try : 
        #     WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seat_grade_95525"]/a/div/span[1]'))) #
        #     driver.find_element(By.XPATH, '//*[@id="seat_grade_95525"]/a/div/span[1]').click()  #
        #     WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seat_grade_95525"]/div/div/span/a'))) #
        #     driver.find_element(By.XPATH, '//*[@id="seat_grade_95525"]/div/div/span/a').click()  #
            
        # except:
        #     print('')
        check()


def macro02():
    print("시작")
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seat_grade_96160"]/a/div/span[2]/span[1]'))) #
    seat01 = int(driver.find_element(By.XPATH, '//*[@id="seat_grade_96160"]/a/div/span[2]/span[1]').text)

    if seat01 == 0 :
            print("자리없음")
            each01 = 0
            while each01 < 1 :              
                check()
    else :
        print("자리발생")
        play_mp3(mp3_file)
        time.sleep(10000)
          
def macro01():

    try :
        each = 0
        print("매크로 ` 누르면 재시작")
        while each < 1 :
                if keyboard.read_key() == "`":
                    break
        driver.switch_to.window(driver.window_handles[-1])
        macro02()
        
        
    except:
        macro02()


macro01()
