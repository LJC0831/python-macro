import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
url = "https://pages.coupang.com/p/117571"  # 예: 뷰티/헤어가전 페이지
driver.get(url)

# 페이지가 로드될 때까지 대기
time.sleep(1)

# 상품 정보 크롤링
products = []

# 상품 리스트 탐색 (최대 20개만)
product_elements = driver.find_elements(By.CLASS_NAME, 'lazy-container.product-list-contents__product-unit')
for product_element in product_elements:
    try:
        # 링크
        link_element = product_element.find_element(By.TAG_NAME, 'a')
        product_url = link_element.get_attribute('href')
        # 썸네일 이미지 URL
        thumbnail_element = product_element.find_element(By.CLASS_NAME, 'product-unit-thumbnail')
        thumbnail_url = thumbnail_element.find_element(By.TAG_NAME, 'img').get_attribute('src')
        
        # 상품 제목
        title_element = product_element.find_element(By.CLASS_NAME, 'product-unit-info__title')
        title = title_element.text
        
        # 현재 금액
        price_element = product_element.find_element(By.CLASS_NAME, 'current-price__price')
        price = price_element.text
        
        # 할인 전 가격
        try:
            discount_price_element = product_element.find_element(By.CLASS_NAME, 'discount-price__base-price')
            discount_price = discount_price_element.text
        except:
            discount_price = None

        # 상품 정보 저장
        product_info = {
            'thumbnail': thumbnail_url,
            'title': title,
            'price': price,
            'discount_price': discount_price,
        }
        products.append(product_info)
    except Exception as e:
        print(f"상품 정보를 추출하는 중 오류 발생: {e}")

# 드라이버 종료
driver.quit()

# MariaDB에 연결
db_config = {
    'user': 'root',
    'password': 'qrg258*001',
    'host': '34.105.27.85',
    'database': 'item'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# 테이블 생성
create_table_query = """
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    thumbnail VARCHAR(1000),
    title VARCHAR(1000),
    price VARCHAR(50),
    discount_price VARCHAR(50)
)
"""
cursor.execute(create_table_query)

# 데이터 삽입
insert_query = """
INSERT INTO products (thumbnail, title, price, discount_price)
VALUES ( %s, %s, %s, %s)
"""
for product in products:
    cursor.execute(insert_query, (
        product['thumbnail'],
        product['title'],
        product['price'],
        product['discount_price']
    ))

# 커밋 및 연결 종료
conn.commit()
cursor.close()
conn.close()

# 추출한 상품 정보 출력
for product in products:
    print(product)