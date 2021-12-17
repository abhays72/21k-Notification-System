# import requests

# payload = {
#     't_username': "210107045",
#     't_password': 'Abhaysudhir21kschool',
#     't_login': 'submit'
# }
# r = requests.post("https://www.21kschool.in/#portal/1/", data=payload)

# print(r.text)

# from bs4 import BeautifulSoup
# from requests import get
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(executable_path="/Users/AbhayS/Downloads/chromedriver")
# driver.get("https://www.21kschool.in/login?domain=1")
# # r = get('https://www.21kschool.in/login?domain=1')
# # soup = BeautifulSoup(r.content)
# driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Fowz")








# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path="/Users/AbhayS/Downloads/chromedriver")

# driver.get("https://www.21kschool.in/login?domain=1")

# driver.find_element(By.NAME, "t_username").send_keys("210107045")
# driver.find_element(By.NAME, "t_password").send_keys("Abhaysudhir21kschool")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from getpass import getpass
from selenium.common.exceptions import NoSuchElementException
import os
import schedule
import time


def check_notif():
    CHROMEDRIVER_PATH = '/Users/AbhayS/Downloads/chromedriver'

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    # chrome_options.binary_location = CHROME_PATH

    username = "210107045"
    password = "Abhaysudhir21kschool"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
    driver.get("https://21kschool.in/")


    username_textbox = driver.find_element_by_name("t_username")
    username_textbox.send_keys(username)

    password_textbox = driver.find_element_by_name("t_password")
    password_textbox.send_keys(password)

    login_button = driver.find_element_by_name("t_login")
    login_button.click()

    try:
        alerts = driver.find_element_by_xpath("/html/body/div[1]/div[6]/a[6]/span")
    
        if int(alerts.text) >= 2:
            print(f"You have {alerts.text} Notifications")
            os.system("""
                    osascript -e 'display notification "{}" with title "{}"'
                    """.format(f"You have {alerts.text} Notifications", "21k School"))
                    
        elif int(alerts.text) == 1:
            print(f'You have 1 Notification')
            os.system("""
                    osascript -e 'display notification "{}" with title "{}"'
                    """.format("You have 1 Notification", "21k School"))
                    
        else:
            os.system("""
                    osascript -e 'display notification "{}" with title "{}"'
                    """.format("You have NO Notifications", "21k School"))

    except NoSuchElementException:
        print('yo')
        pass

# check_notif(username, password)

# schedule.every(0.5).minutes.do(check_notif(username, password))
# while True:
    # schedule.run_pending()
    # time.sleep(1)
check_notif()

schedule.every(5).seconds.do(check_notif)

while 1:
    schedule.run_pending()
    time.sleep(1)