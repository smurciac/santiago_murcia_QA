# Automation Project

## Copyright (c) 2019 Automation Project
```
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```

## Introduction
I choose this stack of tech for the project based on the knowledge of the company (Python), and the usability of the code using the pattern POM, BDD to write the test cases (features) and allure for report.

## Pre-Conditions
**HomeBrew:**

1. Link: https://brew.sh/

**XCode:**
    
1. Install latest version of XCode
2. Install component version 11.2, 12.0 and 12.1

**Android Studio:**

1. Install latest version of Android Studio
2. Create an AVD with at least this specs:
    - Resolution -> 1440 x 2560: 560 dpi
    - API 25 -> Android 7.1.1
    - CPU/ABI -> x86
    - RAM -> 3072 MB
    - Internal Storage -> 3000 MB
    - SD Card -> 6000 MB
3. Install JDK 11 -> https://www.oracle.com/technetwork/java/javase/downloads/jdk11-downloads-5066655.html
4. Paths
```
#Java
export JAVA_HOME=$(/usr/libexec/java_home)
export PATH=$JAVA_HOME/bin:$PATH

#Android
export ANDROID_HOME=/path/to/Android/sdk
export PATH=$PATH:$ANDROID_HOME/tools 
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH/:$ANDROID_HOME/platform-tools
export NODE_PATH=usr/local/bin/node
```

**Python 3.x:**

1. Download version 3.7.2: https://www.python.org/downloads/

**Drivers:**

**Link:** https://www.npmjs.com/package/selenium-webdriver

Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installedbefore the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needsto be in PATH.

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.

1. ***Chrome:***    https://sites.google.com/a/chromium.org/chromedriver/downloads
2. ***Edge:***	    https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
3. ***Firefox:***	https://github.com/mozilla/geckodriver/releases
4. ***Safari:***	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

And for Appium Chrome Driver see the Docs: 
    
1. http://appium.io/docs/en/writing-running-appium/web/chromedriver/
2. https://www.npmjs.com/package/appium-chromedriver

**Setup drivers path:**

1. Open terminal
2. Run -> `sudo nano /etc/paths`
3. Type password
4. Add path at the bottom (i.e. ~/path/to/drivers)
5. Press `ctrl+x` to quit
6. Press `Y` to save
7. Press `Enter` to confirm

**Appium Desktop**

1. Download Appium Desktop from: https://github.com/appium/appium-desktop/releases/tag/v1.10.0
2. Install and Launch Appium Desktop
3. IP -> 127.0.0.1
4. Port -> 4723
5. Start Appium Server

## virtualenvwrapper

**link:** https://virtualenvwrapper.readthedocs.io/en/latest/install.html

1. Install -> `pip3 install virtualenvwrapper`
2. Run to get the path -> `which virtualenvwrapper.sh`
2. Setup the following variables:

```
#Virtualenvs
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
source /put/path/to/virtualenvwrapper.sh
```

3. Create a virtual env: `mkvirtualenv <virtualenv_name>`
4. Run `workon <virtualenv_name>`

## Repo

**Link to Repo:** https://github.com/smurciac/Selenium-Appium-Python

1. `git clone git@github.com:smurciac/Selenium-Appium-Python.git`

## Install requirements.txt

Install one by one of the requirements or run:

1. `pip3 install -r requirements.txt`
2. To run allure, we need to install the Allure Command Line Tool -> `brew install allure` or `npm i allure-commandline`

## Executing Automated Tests

Once all the requirements are installed, go to the root's project and simply run:

1. `behave`
2. `behave -f allure_behave.formatter:AllureFormatter -o allure_results ./tests/features` -> For Allure Report
3. `allure serve allure_results/` -> Generate Allure Report
4. `behave -i name_of_the.feature` -> To run specific feature
5. `behave -i name_of_the.feature -D resize=Yes` -> To run only StoryBook

## Project's Structure
```
    /
        /drivers
            appium-chromedriver
            chromedriver
            geckodriver
        /src
            /control
                __init__.py
                helper_control.py
                webdriver_control.py
            /pages
                __init__.py
                main_page.py
            __init__.py
        /tests
            /features
                tutorial.feature
            /steps
                given_handler.py
                then_handler.py
                when_handler.py
            __init__.py
            environment.py
        .gitignore
        behave.ini
        constants.py
        README.md
        requirements.txt
```

## Visual Studio Code Ruler & Max Line Length for pep8
For this project, we use 120 line lenght, to overwrite the 79 line lenght of pep8, add this code to
setting.json

```
"editor.rulers": [120],
    "workbench.colorCustomizations": {
        "editorRuler.foreground": "#ff4081"
    },
    "python.linting.pep8Args": ["--max-line-length=120"],
    "python.venvPath": "~/.virtualenvs"
```

## Visual Studio Extensions

1. Cucumber (Gherkin) Full Support
2. Feature Syntax Highlight and Snippets (Cucumber/Gherkin)
3. Gherkin Indent
4. Python