import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from plyer import notification
import time

# user input of share price and name
def alert(name,Price,ques):

    URL = "https://www.tickertape.in/"
    driver = webdriver.Chrome(executable_path="D:\chromedriver\chromedriver.exe")
    driver.get("https://www.tickertape.in")

    inputelement = driver.find_element_by_id("search-stock-input").send_keys(name)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-link")))
    element.click()
    driver.minimize_window()
    while True:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        price = soup.find('span', {"class": "jsx-4273511946 current-price text-primary text-24"}).text
        time.sleep(5)
        if float(price) >= float(Price):
            notification.notify(
                title='Alert',
                message=f"Price has touched you can {ques} now",
                app_icon=None,
                timeout=20
            )
            break