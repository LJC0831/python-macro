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
import mysql.connector

# Chrome 드라이버 경로 설정
chrome_driver_path = r"D:\chromedriver_win32\chromedriver.exe"

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저를 표시하지 않음
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 웹 드라이버 초기화
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# 쿠팡 페이지로 이동
url = "https://shopping.naver.com/festa/gift/6683991aafa1c42522d4fc3e"  # 예: 뷰티/헤어가전 페이지
driver.get(url)

# 페이지가 로드될 때까지 대기
time.sleep(1)



# 상품 정보 크롤링
products = []

def is_scrolled_to_bottom(driver):
    # 현재 스크롤 위치와 페이지의 전체 높이를 가져옵니다.
    scroll_height = driver.execute_script("return document.documentElement.scrollHeight;")
    current_scroll_position = driver.execute_script("return window.pageYOffset + window.innerHeight;")
    return current_scroll_position >= scroll_height

# 상품 리스트 탐색 (최대 20개만)
product_elements = driver.find_elements(By.CLASS_NAME, '_emphasisProduct-module_emphasis_product_qhyTO')
for product_element in product_elements:
    try:
        # 링크
        link_element = product_element.find_element(By.TAG_NAME, 'a')
        product_url = link_element.get_attribute('href')
        
        # 썸네일 이미지 URL
        thumbnail_element = product_element.find_element(By.CLASS_NAME, '_emphasisProduct-module_image_area_6kk5-')
        thumbnail_url = thumbnail_element.find_element(By.CLASS_NAME, '_emphasisProduct-module_image_NM-FQ').get_attribute('src')

        echo = 1
        while echo > 0:
            if thumbnail_url == 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=':
                print('lazy 이미지확인')
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                thumbnail_element = product_element.find_element(By.CLASS_NAME, '_emphasisProduct-module_image_area_6kk5-')
                thumbnail_url = thumbnail_element.find_element(By.CLASS_NAME, '_emphasisProduct-module_image_NM-FQ').get_attribute('src')
                print(thumbnail_url)
                print('스크롤처리')
                if is_scrolled_to_bottom(driver):
                    print("페이지 맨 아래에 도달했습니다.")
                    echo = -1
                    break
            else :
                print('이미지 로딩완료')
                break

        
        
        # 상품 제목
        title_element = product_element.find_element(By.CLASS_NAME, '_emphasisProduct-module_title_4nQny')
        title = title_element.text
        
        # 현재 금액
        price_element = product_element.find_element(By.CLASS_NAME, '_emphasisProduct-module_price_aX4gs')
        price = price_element.find_element(By.CLASS_NAME, '_emphasisProduct-module_number_wnnX9').text
        
        # 할인 전 가격 _emphasisProduct-module_number_wnnX9
        try:
            discount_price_element = product_element.find_element(By.CLASS_NAME, '_emphasisProduct-module_origin_price_hbPjv')
            discount_price = discount_price_element.find_element(By.CLASS_NAME, '_emphasisProduct-module_number_wnnX9').text
        except:
            discount_price = None

        # 할인률
        try:
            discount_rate_element = product_element.find_element(By.CLASS_NAME, '_emphasisProduct-module_price_wrap_tE4G2')
            discount_rate = discount_rate_element.find_element(By.TAG_NAME, 'em').text
        except:
            discount_rate = None

        # 상품 정보 저장
        product_info = {
            'thumbnail': thumbnail_url,
            'title': title,
            'price': price,
            'discount_price': discount_price,
            'discount_rate' : discount_rate
        }
        products.append(product_info)
    except Exception as e:
        print(f"상품 정보를 추출하는 중 오류 발생: {e}")

# 드라이버 종료
# driver.quit()

# # MariaDB에 연결
# db_config = {
#     'user': 'root',
#     'password': 'qrg258*001',
#     'host': '34.105.27.85',
#     'database': 'item'
# }

# conn = mysql.connector.connect(**db_config)
# cursor = conn.cursor()

# # 테이블 생성
# create_table_query = """
# CREATE TABLE IF NOT EXISTS products (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     thumbnail VARCHAR(1000),
#     title VARCHAR(1000),
#     price VARCHAR(50),
#     discount_price VARCHAR(50)
# )
# """
# cursor.execute(create_table_query)

# # 데이터 삽입
# insert_query = """
# INSERT INTO products (header, thumbnail, title, price, discount_price, discount_rate)
# VALUES ('naver', %s, %s, %s, %s, %s)
# """
# for product in products:
#     cursor.execute(insert_query, (
#         product['thumbnail'],
#         product['title'],
#         product['price'],
#         product['discount_price'],
#         product['discount_rate']
#     ))

# # 커밋 및 연결 종료
# conn.commit()
# cursor.close()
# conn.close()

# 추출한 상품 정보 출력
for product in products:
    print(product)