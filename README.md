# SeleniumStockChecker
Checks one page for keywords using selenium. Does not auto purchase, just notifies you via email when stock if available.

## Configuration
Run `python setupconfigfiles.py` in the repository directory to create a default config file. This file is named `config.ini` and contains the following parameters:

- `itemname`: The name of the item. Used in alerts.
- `url`: The url to check.
- `keyword`: The program checks to see if this keyword is found on the page. If not, it alerts you. Set the keyword to something that will disappear from the page when the item is back in stock, such as 'Sold Out'.
- `refreshrate`: The rate at which to check for stock (in minutes). Be aware that setting this too high may cause some pages to block your IP due to spam. Recommended setting, 1-5.
- `stoponsuccess`: Whether the program will quit when after it sends an alert. If this is set to no, then the program will continue sending emails every refresh cycle.
- `runinbackground`: Whether the app should run quietly in the background or show an actual chrome tab. Warning: some websites block browsers that are running in the background. For example, this app will not work on best buy links while in background mode.

Under the `Emails` section, you can put any number of emails that you want. The key doesn't matter, so you can set it to whatever you want.