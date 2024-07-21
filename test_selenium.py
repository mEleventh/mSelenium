from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# تحديد المسار الصحيح لـ ChromeDriver
service = Service(r'C:\Users\m7md7\Desktop\ChromeDriver-win64\chromedriver.exe')

# إنشاء مثيل لـ Chrome WebDriver
driver = webdriver.Chrome(service=service)

# فتح صفحة ويب
driver.get("https://www.google.com")

# البحث عن عنصر في الصفحة
search_box = driver.find_element(By.NAME, "q")

# إدخال نص في مربع البحث
search_box.send_keys("Selenium with Python")

# إرسال النموذج
search_box.submit()

# إغلاق المتصفح بعد 5 ثوانٍ
import time
time.sleep(5)
driver.quit()
