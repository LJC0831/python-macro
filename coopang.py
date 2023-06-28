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
seat = 0
def check_go2(seatText):
    if (seatText == "A") :
        driver.find_element(By.XPATH, seatText).click()  # 예약버튼
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seat_grade_83445"]/div/div/span[1]/a')))
        driver.find_element(By.XPATH, '//*[@id="seat_grade_83445"]/div/div/span[1]/a').click()  #
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[1]/form/fieldset/div/a')))
        driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[1]/form/fieldset/div/a').send_keys('2')
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[2]/a')))
        driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[2]/a').click()  #
    
    if (seatText == "B") :
        driver.find_element(By.XPATH, seatText).click()  # 예약버튼
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seat_grade_83446"]/div/div/span[1]/a')))
        driver.find_element(By.XPATH, '//*[@id="seat_grade_83446"]/div/div/span[1]/a').click()  #
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[1]/form/fieldset/div/a')))
        driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[1]/form/fieldset/div/a').send_keys('2')
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[2]/a')))
        driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[2]/a').click()  #
    
    if (seatText == "C") :
        driver.find_element(By.XPATH, seatText).click()  # 예약버튼
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seat_grade_83447"]/div/div/span[1]/a')))
        driver.find_element(By.XPATH, '//*[@id="seat_grade_83447"]/div/div/span[1]/a').click()  #
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[1]/form/fieldset/div/a')))
        driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[1]/form/fieldset/div/a').send_keys('2')
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[2]/a')))
        driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[5]/div[2]/a').click()  #
        
    

def check_go(seatName, i):
    if (seatName >= 2) :
                
                if (i == "STA") :
                    print("1등석A좌석 취소티켓발생")
                    check_go2("A")
                if (i == "MID") :
                    print("1등석B좌석 취소티켓발생")
                    check_go2("B")
                if (i == "END") :
                    print("1등석C좌석 취소티켓발생")
                    check_go2("C")
                # 알림 생성을 위한 자바스크립트 실행 예제
                
                
                driver.execute_script("alert('취소티켓발생');")
                # each = 0
                # while each < 1 :
                #     print("시간 | 좌석선택완료 버튼 좌표 가져오기\n 마우스 가져다 대고 순서대로 1, 2 를 누르면 됨\n")
                #     k = 0
                #     while k < 1 :
                #         if keyboard.read_key() == "1":
                #             xxx, yyy = pyautogui.position()
                #             break
                #     l = 0
                #     pyautogui.moveTo(xxx , yyy , 0.01) # 좌석상세 마우스이동
                #     pyautogui.click()
                #     while l < 1 :
                #         if keyboard.read_key() == "2":
                #             selx, sely = pyautogui.position()
                #             break
                #     pyautogui.moveTo(selx , sely , 0.01) # 좌석상세 마우스이동
                #     pyautogui.click()
                #     driver.switch_to.window(driver.window_handles[-1])
                #     driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="marketing-webview"]')) # iframe 이동
                #     driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[4]/a').click()  # 예약버튼
                #     try :
                #         da = Alert(driver)
                #         da.accept()
                #         time.sleep(1)
                #     except :
                #         print("좌석선택완료")

                #     if keyboard.read_key() == "`":
                #         break
    else :
        if (i == "STA") :
            print("1등석A좌석없음")
        if (i == "MID") :
             print("1등석B좌석없음")
        if (i == "END") :
            print("1등석C좌석없음")
            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[2]/div[1]/div[2]/a'))) #
            driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[2]/div[1]/div[2]/a').click() # 새로고침
            time.sleep(1)
    
   

driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () =&gt; undefined }) """})

url = "https://www.coupangplay.com/?_branch_match_id=1201762869960887227&utm_source=Microsite&utm_campaign=Microsite_CTA_Traffic_All_Organic_CPS&utm_medium=marketing&_branch_referrer=H4sIAAAAAAAAA8soKSkottLXT84vLUjMSy%2FISazUSywo0MvJzMvWj3I2rXByM3cPq0wCAHTwAAIoAAAA" 
driver.get(url)

##
## 이거 꼭수정
#seat_xpath = '/html/body/div[4]/div/div/div[2]/div[2]/div[1]/button'
seat_xpath = '/html/body/div[4]/div/div/div[2]/div[2]/div[2]/button' #마드리드
##
a = 0
while a < 1 :
    if keyboard.read_key() == "`":  # ` 키로 매크로시작
        break

print("매크로 시작")
WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="marketing-webview"]')))
driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="marketing-webview"]')) # iframe 이동
WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[1]/div[1]/div[2]/div/form/div[3]/div/span[1]'))) #동의1
driver.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[1]/div[1]/div[2]/div/form/div[3]/div/span[1]').click() # 동의1
WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[1]/div[1]/div[2]/div/form/div[4]/div/span[1]'))) #동의2
driver.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[1]/div[1]/div[2]/div/form/div[4]/div/span[1]').click() # 동의2
# 예매하기 버튼 클릭
i = 0
while i < 1 : 
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[1]/div[1]/div[2]/div/form/div[5]/button'))) #티켓구매시작버튼
    driver.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[1]/div[1]/div[2]/div/form/div[5]/button').click() # 티켓구매시작버튼


    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, seat_xpath))) #예약하기버튼 현재 K리그
    try :
        use_yn = driver.find_element(By.XPATH, seat_xpath).get_attribute("disabled") # 예약하기버튼 현재 K리그
    except :
        use_yn = 0

    if use_yn :  # 아직 비활성화
        print('아직신청불가')
        pyautogui.moveTo(1212 , 1000 , 0.01) # 좌석마우스이동 
        pyautogui.click()
        continue
    else :
        driver.find_element(By.XPATH, seat_xpath).click() # 예약하기버튼
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="marketing-webview"]')))
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="marketing-webview"]')) # iframe 이동
        while seat < 1 :
            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[4]/a'))) #테스트
            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seat_grade_83445"]/a/div/span[2]/span[1]'))) #
            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seat_grade_83446"]/a/div/span[2]/span[1]'))) #
            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seat_grade_83447"]/a/div/span[2]/span[1]'))) #
            seat01 = int(driver.find_element(By.XPATH, '//*[@id="seat_grade_83445"]/a/div/span[2]/span[1]').text)
            seat02 = int(driver.find_element(By.XPATH, '//*[@id="seat_grade_83446"]/a/div/span[2]/span[1]').text)
            seat03 = int(driver.find_element(By.XPATH, '//*[@id="seat_grade_83447"]/a/div/span[2]/span[1]').text)
            check_go(seat01, "STA")
            check_go(seat02, "MID")
            check_go(seat03, "END")
