import configparser

config = configparser.ConfigParser()

config['Settings'] = {
    "itemname": "Cool Thingy at Google",
    "url": "https://www.google.com",
    "keyword": "Google Search",
    "refreshrate": 0.25,
    "stoponsuccess": "yes",
    "runinbackground": "no"
}

config['Emails'] = {
    "home": "home@example.com",
    "work": "work@example.com"
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)