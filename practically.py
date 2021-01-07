from selenium import webdriver
import time
from settings import *
def practically():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
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
