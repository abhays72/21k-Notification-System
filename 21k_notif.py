import requests
from bs4 import BeautifulSoup

login_data = {
    't_username': "210107045",
    't_password': "Abhaysudhir21kschool",
    't_login': 'submit'
}
with requests.Session() as s:
    url = "https://www.21kschool.in/login?domain=1"
    r = s.get(url)
    print(r.text)
    soup = BeautifulSoup(r.text, 'html5lib')

    r = s.post(url, data=login_data)

    print("https://www.21kschool.in/#portal/1/")

# def login(username, password):
#     s = requests.Session()
#     payload = {
#         't_username': username,
#         't_password': password,
#         't_login': 'submit'
#     }
#     res = s.post(
#         'https://www.21kschool.in/login?dir=/&hash=portal/1/', data=payload)
