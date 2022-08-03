from calendar import month
import time
import random
from datetime import date, datetime
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("C:/Users/giuse/Desktop/virgilio/chromedriver.exe")
driver.get('https://registrazione.virgilio.it/')
time.sleep(3)

cookiereject = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[1]")
cookiereject.click()
time.sleep(1)

def generate_the_word(infile):
    with open(infile) as f:
        contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]

firstWord = generate_the_word("list.txt")
secondWord = generate_the_word("list.txt")
text_area = driver.find_element_by_id('username')
text_area.send_keys(firstWord+secondWord)
text_area = driver.find_element_by_id('password')
text_area.send_keys("Testing1234.")
text_area = driver.find_element_by_id('confirmpassword')
text_area.send_keys("Testing1234.")

next = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/section/form/div[5]/div[2]/button")
next.click()
time.sleep(2)
name = generate_the_word("list.txt")
text_area = driver.find_element_by_id('firstname')
text_area.send_keys(name)
surname = generate_the_word("list.txt")
text_area = driver.find_element_by_id('lastname')
text_area.send_keys(surname)

def generate_day():
    day = random.randrange(1,29)
    return day
day = generate_day()



def generate_month():
    
    month = random.randrange(1,13)
    return month

months = generate_month()



def generate_year():
    listValue = [1999,2000,2001,2002]  
    year = random.choice(listValue)  
    
    return year

year = generate_year()

sday = day.__str__()
smonth = months.__str__()
syear = year.__str__()

random_date = sday+'/'+smonth+'/'+syear
text_area = driver.find_element_by_id('dateofbirth')
text_area.send_keys(random_date)
time.sleep(1)

male = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/form/div[3]/div/div[2]/label')
male.click()

def  generate_city():
    listValue = ['A','B','C','D','E','F']
    city = random.choice(listValue)
    return city

city = generate_city()
text_area = driver.find_element_by_id('comune_provincia')
text_area.send_keys(city)

selectedCity = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/form/div[4]/div/div/ul')
selectedCity.click()

next = driver.find_element_by_id("button_submit")
next.click()

email = name+"@test.it"
text_area = driver.find_element_by_id('emailsecondaria')
text_area.send_keys(email)

cookie1 = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/form/div[3]/div/div[3]/label')
cookie1.click()

cookie2 = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/form/div[3]/div/div[7]/label')
cookie2.click()

time.sleep(3)
next = driver.find_element_by_id("button_submit")
next.click()
time.sleep(4)
next = driver.find_element_by_id("button_submit")
next.click()
time.sleep(4)
next = driver.find_element_by_id("button_submit")
next.click()