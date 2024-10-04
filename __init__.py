'''
__init__.py created by David Bootle
3/5/2021
'''

import os
import sys
import configparser
import time
from twilio.rest import Client
from selenium.webdriver.chrome.service import Service  # Import for Service

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
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
    stop_on_success = config.getboolean('Settings', 'stoponsuccess')
    run_in_background = config.getboolean('Settings', 'runinbackground')

    # Twilio config
    twilio_account_sid = config['Twilio']['accountsid']
    twilio_auth_token = config['Twilio']['authtoken']
    twilio_phone_number = config['Twilio']['fromphone']
    phone_numbers = []
    for key in config['Phones']:
        phone_numbers.append(config['Phones'][key])
    print('Loaded config.')
except:
    print('Invalid config file. Run setupconfigfiles.py.')
    sys.exit()

if len(phone_numbers) == 0:
    print('No phone numbers specified. Quitting.')
    sys.exit()

# Try block for driver setup and monitoring
try:
    chrome_options = Options()
    if run_in_background:
        chrome_options.add_argument("--headless")  # Runs Chrome in background

    # Set up the service for chromedriver and initialize WebDriver with options
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    client = Client(twilio_account_sid, twilio_auth_token)

    while True:
        if keyword not in driver.page_source:
            # Send SMS message
            for phone in phone_numbers:
                message = f'{item_name} Alert! Check it here: {url}'
                try:
                    client.messages.create(
                        body=message,
                        from_=twilio_phone_number,
                        to=phone
                    )
                    print(f'SMS sent to {phone}')
                except Exception as e:
                    print(f'Error sending SMS to {phone}: {e}')

            if stop_on_success:
                print(f'Keyword {keyword} is missing on {url}. SMS sent. Quitting...')
                driver.quit()
                sys.exit()
            else:
                print('Found keyword, and sent SMS. Continuing to monitor.')
        time.sleep(refresh_rate * 60)
        driver.refresh()

# Catch script exit
except KeyboardInterrupt:
    print('Exiting...')
    driver.quit()
    sys.exit()
