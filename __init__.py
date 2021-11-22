'''
__init__.py created by David Bootle
3/5/2021
'''

import os
import sys
import configparser
import time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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

    emails = []
    for key in config['Emails']:
        emails.append(config['Emails'][key])

    print('Loaded config.')
except:
    print('Invalid config file. Run setupconfigfiles.py.')
    sys.exit()

if len(emails) == 0:
    print('No emails specified. Quitting.')
    sys.exit()

try:
    chrome_options = Options()
    if run_in_background:
        chrome_options.add_argument("--headless")

    driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)

    driver.get(url)

    while True:
        if keyword not in driver.page_source:
            # send message
            message = Mail(
                from_email = 'alerts@bootle.tech',
                to_emails = emails,
                subject = f'{item_name} Alert!',
                html_content = f'''
                <p><a href="{url}">{url}</a></p>
                ''')
            try:
                sg = SendGridAPIClient('<SENDGRID API KEY HERE>')
                response = sg.send(message)
                
            except Exception as e:
                print(e)

            if stop_on_success:
                print(f'Keyword {keyword} is missing on {url}. Emails sent. Quitting...')
                driver.quit()
                sys.exit()
            else:
                print('Found keyword, and sent emails. Continuing to monitor.')
        time.sleep(refresh_rate * 60)
        driver.refresh()
except KeyboardInterrupt:
    print('Exiting...')
    driver.quit()
    sys.exit()