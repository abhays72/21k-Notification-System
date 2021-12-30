# Abhay's 21k School Notif System
Hello everyone, this is a small project I've been working on for some time and it taught me a lot. I hope it helps you too.
Have a great day!

## Requirements
- Selenium Chrome Driver [https://chromedriver.chromium.org/downloads]
- MacOS Monterey (Hasn't been tried on previous version)
- Newest Version of Chrome (Hasn't been tried out on previous versions)

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
Start the background process: 