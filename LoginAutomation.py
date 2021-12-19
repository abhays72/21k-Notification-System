from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import schedule
import time
import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom

CHROMEDRIVER_PATH = "C:/Users/bluesinc/Downloads/chromedriver_win32/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("--headless")


username = "210107045"
password = "Abhaysudhir21kschool"

# keep track of how many previous notifs
var = 0
def check_notif():
    nManager = notifications.ToastNotificationManager
    notifier = nManager.create_toast_notifier();
    # setting up chromedriver -->
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
    # --> end of chrome driver setup
    while True:
        try:
            # get the number of messages unread
            alert = driver.find_element_by_xpath("/html/body/div[1]/div[6]/a[6]/span")
            global var
            if int(alert.text) > var:
                var = int(alert.text)

                if int(alert.text) >= 2:
                    # send notif
                    tString = f"""
                    <toast>
                        <visual>
                        <binding template='ToastGeneric'>
                            <text>You have {alert.text} Messages</text>
                            <text>From:</text>
                        </binding>
                        </visual>
                        <actions>
                        <action
                            content="Delete"
                            arguments="action=delete"/>
                        <action
                            content="Dismiss"
                            arguments="action=dismiss"/>
                        </actions>        
                    </toast>
                    """
                    xDoc = dom.XmlDocument()
                    xDoc.load_xml(tString)
                    notifier.show(notifications.ToastNotification(xDoc))

                    return (f"You have {alert.text} Notifications")
                            
                elif int(alert.text) == 1:
                    # send notif
                    tString = f"""
                    <toast>
                        <visual>
                        <binding template='ToastGeneric'>
                            <text>You have {alert.text} Message</text>
                            <text>From:</text>
                        </binding>
                        </visual>
                        <actions>
                        <action
                            content="Delete"
                            arguments="action=delete"/>
                        <action
                            content="Dismiss"
                            arguments="action=dismiss"/>
                        </actions>        
                    </toast>
                    """
                    xDoc = dom.XmlDocument()
                    xDoc.load_xml(tString)
                    notifier.show(notifications.ToastNotification(xDoc))
                    return (f'You have 1 Notification')
            # if the messages were read then just stop the program (starts again when schedule is called)
            elif int(alert.text) < var:
                break
            else:
                break

        # This error occurs when there are no notifs
        except NoSuchElementException:
            var = 0
            break

# Run check_notif() every 5 seconds
schedule.every(5).seconds.do(check_notif)

while 1:
    schedule.run_pending()
    time.sleep(1)