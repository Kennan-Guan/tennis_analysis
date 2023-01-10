from selenium import webdriver
from bs4 import BeautifulSoup
import csv
#url is the address in tennisabstract.com
#file_name is a string that is the name of csv 
#file_type is w(write over file of file_name) or x(create new file called file_name)
#function only works for 'http://www.tennisabstract.com/cgi-bin/leaders.cgi
def scraper(url, file_name, file_type):

    #Opens a chrome emulator in igognito mode accessing a specified address because site has dynamic javascript
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(r'C:/Users/kenna/OneDrive/Desktop/Coding/chromedriver.exe', chrome_options=options)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    #finds a table with id 'matches' and finds the data points
    t = soup.find('table', id='matches')
    tbody = t.find('tbody')
    thead = t.find('thead')
    headers = thead.find_all('th')
    data_set = []
    player_names = []
    header_names = []

    #Stores table headers in an array
    for tr in headers:
        header_names.append(tr.text)

    #Creates a new csv file or updates an existing csv file with data points given a name
    with open(file_name, file_type, newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header_names)
        for tr in tbody:
            for td in tr: 
                data_set.append(td.text)
            writer.writerow(data_set)
            data_set = []

    driver.close()

#calls scraper 4 times to access 4 different tables, only used 1 for project

scraper('http://www.tennisabstract.com/cgi-bin/leaders.cgi', 'serve.csv', 'x')
scraper('http://www.tennisabstract.com/cgi-bin/leaders.cgi?f=s00w1', 'return.csv', 'x')
scraper('http://www.tennisabstract.com/cgi-bin/leaders.cgi?f=s00l1', 'breaks.csv', 'x')
scraper('http://www.tennisabstract.com/cgi-bin/leaders.cgi?f=s00t1', 'more.csv', 'x')