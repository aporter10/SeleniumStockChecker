import configparser

config = configparser.ConfigParser()

config['Settings'] = {
    "itemname": "Bunny",
    "url": "https://www.google.com",
    "keyword": "Google Search",
    "refreshrate": 30.25,
    "stoponsuccess": "no",
    "runinbackground": "no"
}

config['Phones'] = {
    "home": "+1xxxxxxxxxx",
    "work": "1xxxxxxxxxx"
}

config['Twilio'] = {
"accountsid": "x",
"authtoken": "x",
"fromphone": "x"
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)