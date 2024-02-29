# Abhay's 21k School Notif System
Hello everyone, this is a small project I've been working on for some time and it taught me a lot. 
I noticed that my school (21k School) did not have a notification system for any messages/announcements that came to their website, so I built a Python script that can be run in the background to periodically check for any important info on the website and automatically send a push notification to your computer.
Have a great day!

## Requirements
- Selenium Chrome Driver [https://chromedriver.chromium.org/downloads]
- MacOS Monterey/Windows 10

## Setup - MacOS:

Install Brew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` <br>
Install pip: `curl https://bootstrap.pypa.io/get-pip.py | python`
Clone this Repository: `git clone https://github.com/abhays72/automation.git` <br>
Install Required Packages: `pip install -r [Path to requirements.txt]` <br>
Change Fields in `LoginAutomation.py` (Chrome Driver Path, Username, Password) <br>
Start the background process: `nohup python3 [Path to LoginAutomation.py] >/dev/null 2>&1 &`

## Setup - Windows

Clone this Repository: `git clone https://github.com/abhays72/automation.git` <br>
Install Required Packages: `pip install -r [Path to requirements.txt]` <br>
Change Fields in `LoginAutomation.py` (Chrome Driver Path, Username, Password) <br>
Still trying to find a way to start background processes for this in Windows.
