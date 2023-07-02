import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup
import ctypes
import cv2
import pytesseract
import urllib.request
import keyboard
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
#이동
url = "https://forest.maketicket.co.kr/ticket/GD41"
day_1 = '//*[@id="calendar_12"]/ul/li[3]/a' #8월12일
driver.get(url)

def play_mp3(file_path):
    os.startfile(file_path)

def macro():
    i = 0
    while i == 0 :
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar"]/a[2]'))) #페이지로딩(최대300초) *다음달 버튼
        driver.find_element(By.XPATH, '//*[@id="calendar"]/a[2]').send_keys(Keys.ENTER) # 다음단계       
        print("예약진행가능")

        j = 0
        while j == 0 :   
            time.sleep(2)
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar"]/table/caption'))) #페이지로딩(최대300초) 
            month = driver.find_element(By.XPATH, '//*[@id="calendar"]/table/caption').text
            if(month == "2023. 08") :
                break
            else :
                continue
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar"]/table/caption'))) #페이지로딩(최대300초) 
        month = driver.find_element(By.XPATH, '//*[@id="calendar"]/table/caption').text
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar_12"]/ul/li[3]/a/span'))) #페이지로딩(최대300초) 
        seat01 = int(driver.find_element(By.XPATH, '//*[@id="calendar_12"]/ul/li[3]/a/span').text)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar_12"]/ul/li[4]/a/span'))) #페이지로딩(최대300초) 
        seat02 = int(driver.find_element(By.XPATH, '//*[@id="calendar_12"]/ul/li[4]/a/span').text)
        if (seat01 >= 1) :
            play_mp3(mp3_file)
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, day_1))) #페이지로딩(최대300초) 
            driver.find_element(By.XPATH, day_1).send_keys(Keys.ENTER) # 다음단계
            i = 10
        elif(seat02 >= 1) :
            play_mp3(mp3_file)
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar_12"]/ul/li[4]/a'))) #페이지로딩(최대300초) 
            driver.find_element(By.XPATH, '//*[@id="calendar_12"]/ul/li[4]/a').send_keys(Keys.ENTER) # 다음단계
            i = 10
        else :
            print("아직 좌석없음")
            driver.get(url)
            time.sleep(1)
    
try :
    macro()
except :
    seat = 0
    while seat < 1 :
        print("매크로재시작 ` 키")
        k = 0
        while k < 1 :
            if keyboard.read_key() == "`":
                macro()
                break


