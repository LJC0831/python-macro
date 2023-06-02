import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



import pyperclip




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

#search_url = '23004325' #팝업 2개뜨는거
search_url = '23007423'  #팝업 아예X

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

    try :
        use_yn = driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[2]/a[1]').text
    except :
        use_yn = 0
    
    if use_yn == "예매하기" : 
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[2]/a[1]').click() # 예매하기 클릭

        # 새창으로 이동
        driver.switch_to.window(driver.window_handles[-1])
        # 새창이 팝업인경우
        try :
            use_yn = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]').is_displayed
            print("aaaaaaaaaaaaaaaaaaa")
            print(use_yn)
        except :
            use_yn = 0
        if use_yn != 0 :
            print("팝업뜸1")
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[-1])
            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/a[2]'))) #페이지로딩(최대300초)
            print("팝업뜸2")
            driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/a[2]').send_keys(Keys.ENTER)
        else :
            # 새창이 예약인경우
            try :
                WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ifrmSeat"]'))) #페이지로딩(최대300초)
            except :
                print("에러발생")

        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)
        # #  iframe 이동
        driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmSeat']")) # iframe 이동
        select = Select(driver.find_element(By.XPATH, '//*[@id="PlayDate"]'))

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
        

        break
    else :
        print('아직신청불가')
        driver.refresh()
#날자선택
#select.select_by_value('20210728') 

