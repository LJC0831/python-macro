import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import pyautogui
import pyperclip



chrome_driver_path = r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

def macro01():

    try :
        #사이트이동
        #url = "https://camfit.co.kr/camp/654881e9d7262a001eebf044/654886e8d7262a001eebf045" #집밖으로
        url = "https://camfit.co.kr/camp/6446197cd3fd8c001e52ce80/644619c62eb46a001e5bcf89" #test
        driver.get(url)
        time.sleep(0.5)

        each = 0
        print("매크로 ` 누르면 재시작")
        while each < 1 :
                if keyboard.read_key() == "`":
                    break
        time.sleep(0.5)
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/div[1]/div[8]/div/div/button'))) #
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[8]/div/div/button').click()  #
        time.sleep(0.5)
        
        try :
            driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div[1]/div[1]/button[2]').click() # 다음달
            time.sleep(0.5)
        except :
            pyautogui.moveTo(1415 , 505 , 0.01) # 좌석상세 마우스이동
            time.sleep(0.1)
            pyautogui.click()
                   
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div[1]/div[5]/div[1]/div[5]/div[2]'))) #
        sta_ymd = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div[1]/div[5]/div[2]/div[1]/div[7]') #달력 29일 나중에 수정#####################
        sta_ymd.click() 
        end_ymd = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div[1]/div[5]/div[2]/div[2]/div[1]') #달력 30일 나중에 수정#####################
        end_ymd.click() 

        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/button').click() # 선택완료
        time.sleep(0.5)
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[3]/div/button'))) #
        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/button').click() # 선택완료2
        time.sleep(0.5)
        try :
            driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[8]/div/div[2]/div[2]/div[2]').click() # 자리 나중에 수정#####################
        except :
            print('자리없음')
            
        time.sleep(0.5)
        #사이트예약하기 버튼
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[10]/button').click() 
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[11]/div[2]/button').click()  #확인하고 예약계속
        time.sleep(0.5) 
        # ID,PW
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[2]/div[2]/input[1]').send_keys('leejc831')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[2]/div[2]/input[2]').send_keys('qrg258*01')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[2]/button').click()
        time.sleep(100000)
        #driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[2]/button').click() #예약하기 버튼.. 우선 주석
    # 예약가능여부
    except:
        macro01()


i = 0
while i < 1 : 
    try :
        macro01()
        time.sleep(100000)
    except :
         print('아직오픈X')
         macro01()
    




    