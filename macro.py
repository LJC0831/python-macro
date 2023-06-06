import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import easyocr




driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
#인터파크 이동
url = "https://ticket.interpark.com/Gate/TPLogin.asp"
driver.get(url)
time.sleep(1)

driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']")) # iframe 이동
userId = driver.find_element(By.ID, 'userId')
userId.send_keys('leejc831') # 로그인 할 계정 id
userPwd = driver.find_element(By.ID, 'userPwd')
userPwd.send_keys('qrg258*001') # 로그인 할 계정의 패스워드
userPwd.send_keys(Keys.ENTER)

#search_url = '23007269' # 팝업X
search_url = '23005708'  # 캡챠잇는거

url2 = 'http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + search_url
driver.get(url2)

# 예매하기 버튼 클릭
i = 0
while i < 1 : 
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="productSide"]/div/div[2]/a[1]'))) #페이지로딩(최대300초)
    # 예매안내가 팝업이 뜨면 닫기. START
    try :
        use_yn = driver.find_element(By.XPATH, '//*[@id="popup-prdGuide"]/div/div[3]/button').text
    except :
        use_yn = 0

    if use_yn == 0 :
        print("팝업없네")
    else :
        print("팝업있네")
        driver.find_element(By.XPATH, '//*[@id="popup-prdGuide"]/div/div[3]/button').send_keys(Keys.ENTER)

    # 예매안내가 팝업이 뜨면 닫기 END
    time.sleep(1)
    try :
        use_yn = driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[2]/a[1]').text
    except :
        use_yn = 0
    
    if use_yn == "예매하기" : 
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[2]/a[1]').click() # 예매하기 클릭

        # # 날짜입력
        # select.select_by_value('20230726')  #예약날자입력
        # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PlaySeq"]'))) #페이지로딩(최대300초)
        # selectTime = Select(driver.find_element(By.XPATH, '//*[@id="PlaySeq"]')) #예약시간
        # selectTime.select_by_index(1) #예약날짜입력

        # # 좌석선택
        # driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmSeatDetail']")) # iframe 이동
        # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ifrmSeatDetail"]'))) #페이지로딩(최대300초)
        #driver.find_element(By.XPATH, '//*[@id="TmgsTable"]/tbody/tr/td/img[236]').click() #좌석클릭
        #driver.find_element(By.XPATH, '//*[@id="TmgsTable"]/tbody/tr/td/img[238]').click() #좌석클릭
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ifrmSeat"]'))) #페이지로딩(최대300초)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmSeat']"))

        # 입력해야될 문자 이미지 캡쳐하기. (캡챠)
        j = 0
        while j < 1 :
            try : 
                capchaPng = driver.find_element(By.XPATH, "//*[@id='imgCaptcha']")
            except :
                capchaPng = 0
            if (capchaPng != 0 ) :
            # easyocr 이미지내 인식할 언어 지정
            
            # 캡쳐한 이미지에서 문자열 인식하기
                time.sleep(1)
                reader = easyocr.Reader(['en'])
                result = reader.readtext(capchaPng.screenshot_as_png, detail=0)

                # 이미지에 점과 직선이 포함되어있어서 문자 인식이 완벽하지 않아서 데이터를 수동으로 보정해주기로 했습니다.
                capchaValue = result[0].replace(' ', '').replace('5', 'S').replace('0', 'O').replace('$', 'S').replace(',', '')\
                .replace(':', '').replace('.', '').replace('+', 'T').replace("'", '').replace('`', '')\
                .replace('1', 'L').replace('e', 'Q').replace('3', 'S').replace('€', 'C').replace('{', '').replace('-', '').replace(';', '')
                
                # 입력할 텍스트박스 클릭하기.
                pyautogui.moveTo(365 , 541 , 0.01) 
                pyautogui.click()
                chapchaText = driver.find_element(By.XPATH, '//*[@id="txtCaptcha"]')
                print("========================")
                print(capchaValue)
                chapchaText.send_keys(capchaValue)
                driver.find_element(By.XPATH, '//*[@id="divRecaptcha"]/div[1]/div[4]/a[2]').send_keys(Keys.ENTER)
                time.sleep(1)
                use_yn = driver.find_element(By.XPATH, '//*[@id="divRecaptcha"]/div[1]/div[3]/div').text
                print(use_yn)
                if use_yn == "입력한 문자를 다시 확인해주세요" :
                    print("캡챠실패")
                if use_yn == "새로운 문자로 다시 인증해주세요" :
                    print("캡챠실패")
                else :
                    break


        # 좌석선택
        break
    else :
        print('아직신청불가')
        driver.refresh()
#날자선택
#select.select_by_value('20210728') 
