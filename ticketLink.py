import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ctypes

if ctypes.windll.shell32.IsUserAnAdmin(): 
    print('관리자권한으로 실행된 프로세스입니다.')
else:
    print('일반권한으로 실행된 프로세스입니다.')

driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
#티켓링크 이동
#url = "https://www.ticketlink.co.kr/sports/baseball/62#reservation" #Kt야구
url = "https://www.ticketlink.co.kr/sports/baseball/57#reservation" #삼성야구
driver.get(url)
time.sleep(1)

#로그인 처리
driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()

#로그인 창 이동
time.sleep(1)
driver.switch_to.window(driver.window_handles[-1])
userId = driver.find_element(By.XPATH, '//*[@id="id"]')
userId.send_keys('leejc831@naver.com') # 로그인 할 계정 id
userPwd = driver.find_element(By.XPATH, '//*[@id="pw"]')
userPwd.send_keys('qrg258*001') # 로그인 할 계정의 패스워드
userPwd.send_keys(Keys.ENTER)
time.sleep(3)

# 예매하기 클릭
print("예매클릭시작")
driver.switch_to.window(driver.window_handles[-1])
time.sleep(1)


# 예약일정 path 지정
day_xpath='//*[@id="scheduleListDiv"]/ul/li[3]/div[3]/a' #테스트용 되는것
#day_xpath='//*[@id="scheduleListDiv"]/ul/li[8]/div[3]/a'

# 해당 일정 open 여부 체크
i = 0
while i < 1 :
    if driver.find_element(By.XPATH, day_xpath).text == "예매하기" :
        print("예약가능")
        driver.find_element(By.XPATH, day_xpath).send_keys(Keys.ENTER) #예매할일정 셋팅필요
        time.sleep(1)
        print("예매창활성화")
        driver.switch_to.window(driver.window_handles[-1])
        
        try :
            use_yn = driver.find_element(By.XPATH, '//*[@id="noticeModalClose"]').text
        except :
            use_yn = 0

        if use_yn != 0 :
            print('팝업on')
            driver.find_element(By.XPATH, '//*[@id="noticeModalClose"]').send_keys(Keys.ENTER) # 다음단계
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            

            
        #세팅한 좌석 선택
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[2]/div[1]/div[2]/a'))) #페이지로딩(최대300초)
        print("좌석선택")
        ################ 세팅필요 ########################
        #pyautogui.moveTo(473 , 600 , 0.01) # 좌석마우스이동 KT
        pyautogui.moveTo(226 , 633 , 0.01) # 좌석마우스이동 삼성블루존
        ################ 세팅필요 ########################
        pyautogui.click()
        # 좌석선택유형
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div[1]/strong'))) #페이지로딩(최대300초)
        #driver.find_element(By.XPATH, '//*[@id="area_bottom"]/form/fieldset/div/div/div/span/a').send_keys(Keys.ENTER)  # KT
        driver.find_element(By.XPATH, '//*[@id="area_bottom"]/form/fieldset/div/div/div/span[2]/a').send_keys(Keys.ENTER)  # 삼성
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main_view"]'))) #페이지로딩(최대300초)
        ################ 세팅필요 ########################
        #KT
        # pyautogui.moveTo(379 , 645 , 0.01) # 좌석상세 마우스이동
        # pyautogui.click()
        # pyautogui.moveTo(395 , 643 , 0.01) # 좌석상세 마우스이동
        # pyautogui.click()
        # KT 끝
        #삼성
        time.sleep(1)
        pyautogui.moveTo(302 , 789 , 0.01) # 좌석상세 마우스이동
        pyautogui.click()
        pyautogui.moveTo(414 , 796 , 0.01) # 좌석상세 마우스이동
        pyautogui.click()
        
        #삼성끝
        ################ 세팅필요 ########################
        driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[4]/a[2]').send_keys(Keys.ENTER)  # 예약버튼
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divPrice"]/div/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/div/a'))) #페이지로딩(최대300초)
        
        pyautogui.moveTo(695 , 544 , 0.01) 
        pyautogui.click()
        ################ 세팅필요 ########################
        pyautogui.moveTo(644 , 630 , 0.01) # 인원선택(2명기준)
        ################ 세팅필요 ########################
        pyautogui.click()
        driver.find_element(By.XPATH, '//*[@id="reserveNext"]').send_keys(Keys.ENTER) # 다음단계
        

        # 수령방법
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[4]/a[2]'))) #페이지로딩(최대300초)
        pyautogui.moveTo(59 , 654 , 0.01) # 동의1
        pyautogui.click()
        pyautogui.moveTo(59 , 708 , 0.01) # 동의2
        pyautogui.click()
        pyautogui.moveTo(59 , 755 , 0.01) # 동의3
        pyautogui.click()
        pyautogui.moveTo(59 , 801 , 0.01) # 동의4
        pyautogui.click()
        pyautogui.moveTo(59 , 845 , 0.01) # 동의5
        pyautogui.click()
        pyautogui.moveTo(676 , 383 , 0.01) # 동의5
        pyautogui.click()
        pyautogui.moveTo(767 , 714 , 0.01) # 동의6
        pyautogui.click()
        pyautogui.moveTo(778 , 804 , 0.01) # 결재수단 
        pyautogui.click()
    
        # 결재
        pyautogui.moveTo(919 , 888 , 0.01) # 결재하기
        pyautogui.click()

        
        break
    else :
        print("예약불가")
        driver.refresh()
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, day_xpath))) #페이지로딩(최대300초)




