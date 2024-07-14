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
        url = "https://camfit.co.kr/camp/654881e9d7262a001eebf044/654886e8d7262a001eebf045" #집밖으로
        #url = "https://camfit.co.kr/camp/6446197cd3fd8c001e52ce80/644619c62eb46a001e5bcf89" #test
        driver.get(url)
        time.sleep(0.5)

        each = 0
        print("매크로 ` 누르면 재시작")
        while each < 1 :
                if keyboard.read_key() == "`":
                    break
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/div[1]/div[10]'))) #
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[10]').click()  #
        try :
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/div[1]/div[1]/button[2]'))) #
            pyautogui.moveTo(1723 , 1019 , 0.01) # 좌석상세 마우스이동
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(0.5)
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/div[1]/div[5]/div[2]/div[1]/div[6]'))) #
            pyautogui.moveTo(1633 , 1115 , 0.01) # 시작일
            time.sleep(0.1)
            pyautogui.click()
            pyautogui.moveTo(1277 , 1155 , 0.01) # 종료일
            time.sleep(0.1)
            pyautogui.click()
            driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/button').click() # 선택완료
        except :
             macro01()
            
        
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/button'))) #
        pyautogui.moveTo(1500 , 1363 , 0.01) # 2명 선택완료
        time.sleep(0.1)
        pyautogui.click()
        # time.sleep(0.5)
        # try :
        #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/div[1]/div[8]/div/div[2]/div[2]/div[1]'))) #
        #     driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[8]/div/div[2]/div[2]/div[1]').click() # 자리 나중에 수정#####################
        # except :
        #     print('자리없음')

        each2 = 0
        print("자리선택 완료후 ` 눌러")
        while each2 < 1 :
                if keyboard.read_key() == "`":
                    break
            
        # #사이트예약하기 버튼
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/div[1]/div[10]/button'))) #
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[10]/button').click() 
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/div[1]/div[11]/div[2]/button'))) #
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[11]/div[2]/button').click()  #확인하고 예약계속
        
        # # ID,PW
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/div[1]/div[2]/div[2]/input[1]'))) #
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[2]/div[2]/input[1]').send_keys('leejc831')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[2]/div[2]/input[2]').send_keys('qrg258*01')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[2]/button/span[1]').click()
        time.sleep(100000)
        #driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div[1]/div[2]/button').click() #예약하기 버튼.. 우선 주석
    # 예약가능여부
    except:
        print('에러')
        macro01()


i = 0
while i < 1 : 
    try :
        macro01()
        time.sleep(100000)
    except :
         print('아직오픈X')
         macro01()
    




    
