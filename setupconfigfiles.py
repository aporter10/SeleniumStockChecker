import configparser

config = configparser.ConfigParser()

config['Settings'] = {
    "itemname": "Cool Thingy at Google",
    "url": "https://www.google.com",
    "keyword": "Google Search",
    "refreshrate": 0.25,
    "email": "example@example.com",
    "stoponsuccess": "yes"
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)