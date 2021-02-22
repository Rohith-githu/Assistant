import time
from selenium import webdriver
from pyttsx3 import speak

def Mapautomate(location):
	driver = webdriver.Chrome()
	driver.get(f'https://www.google.com/maps/dir/17.52048263697133,+78.38474645722229/{location}')
	time.sleep(5)
	driver.maximize_window()
	time_to = driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[1]/span[1]').text
	via_route = driver.find_element_by_xpath('//*[@id="section-directions-trip-title-0"]/span').text
	time_to = time_to.replace('hr','hour')
	via_route = via_route.replace('Rd','road')
	speak(f'It takes {time_to} To reach {location}')
	speak(f'via {via_route}')
	time.sleep(10000)
