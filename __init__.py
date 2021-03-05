'''
__init__.py created by David Bootle
3/5/2021
'''

import os
import sys
import configparser
import time

try:
    from selenium import webdriver
except:
    print('Run "pip install selenium" and add chromedriver executable to path. See README for instructions.')
    sys.exit()

config = configparser.ConfigParser()

try:
    config.read('config.ini')
    item_name = config['Settings']['itemname']
    url = config['Settings']['url']
    keyword = config['Settings']['keyword']
    refresh_rate = config.getfloat('Settings', 'refreshrate')
    email = config['Settings']['email']
    stop_on_success = config.getboolean('Settings', 'stoponsuccess')
    print('Loaded config.')
except:
    print('Invalid config file. Run setupconfigfiles.py.')
    sys.exit()

driver = webdriver.Chrome('chromedriver.exe')

driver.get(url)

try:
    while True:
        if keyword not in driver.page_source:
            print('ALERT CRITERIA MET')
            if stop_on_success:
                driver.quit()
                sys.exit()
        time.sleep(refresh_rate * 60)
        driver.refresh()
except KeyboardInterrupt:
    print('Exiting...')
    driver.quit()
    sys.exit()