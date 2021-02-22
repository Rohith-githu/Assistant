import time
from selenium import webdriver
import pyttsx3
def say(query):
    m = pyttsx3.init()
    print(query)
    m.setProperty("rate", 150)
    m.say(query)
    m.runAndWait()
def practically():
    driver = webdriver.Chrome()
    try :
        driver.get('https://www.practically.com')
        print('practically opened')
    except Exception as e :
        print(e)
        say('error occoured while opening practically.com')
        print('error occoured while opening practically.com')

    time.sleep(1)
    try :
        driver.find_element_by_link_text('Login').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="LoginID"]').send_keys('bpt0257')
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('rohith2078')
        driver.find_element_by_xpath('//*[@id="loginform"]/div[5]/button').click()
        print('loged in successfully')
    except Exception as e:
        print(e)
        print('error occoured while logging in')
        say('error occoured while logging in')
    time.sleep(2)
    try :
        driver.find_element_by_xpath('//*[@id="upcoming"]/div[2]/div/div[2]/div[3]/a').click()
        print('class joined')
        say('class joined')
    except Exception as e:
        print(e)
        print('error occoured while joining the class')
        say('error occoured while joining the class')