from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
import time
import os

# serve tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

driver = webdriver.Chrome()
driver.get("http://captcha.challs.olicyber.it/")

while True:
    
    counters = driver.find_elements(By.TAG_NAME, "i")
    passed = int(counters[1].text)

    print(f"Superati: {passed}/100")

    if passed >= 100:
        print("\nfinito")
        break  


    captcha_element = driver.find_element(By.TAG_NAME, "img")
    driver.save_screenshot("page.png")


    location = captcha_element.location_once_scrolled_into_view
    size = captcha_element.size

    x = location["x"]
    y = location["y"]
    w = x + size["width"]
    h = y + size["height"]

    image = Image.open("page.png").crop((x, y, w, h))
    image.save("captcha.png")

    gray = image.convert("L")
    thresholded = gray.point(lambda t: 0 if t < 140 else 255)
    testo = pytesseract.image_to_string(thresholded, config="--psm 7").strip()

    print("CAPTCHA:", testo)

    box = driver.find_element(By.NAME, "risposta")
    box.clear()
    box.send_keys(testo)

    driver.find_element(By.ID, "next").click()

    os.remove("captcha.png")
    os.remove("page.png")

    time.sleep(0.1)

