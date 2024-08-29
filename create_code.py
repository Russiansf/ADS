from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys

url = 'https://www.orangecube.art/'

xpath_text = '//input[@type="text"]'
xpath_text2 = '//span[contains( text(), "Congratulations! Your unique code: ")]'
xpath_next = '//button[text() ="Next"]'

options = webdriver.ChromeOptions()
# options.add_argument('--headless')

def give_balance():
	driver = webdriver.Chrome(options=options)
	driver.get(url=url)
	for i in range(1,31):
		# number = i * 2
		# adress = number - 1
		# if not number % 2 == 0:
		# 	number += 1
		time.sleep(0.5)
		text = driver.find_element('xpath',xpath_text)
		text.send_keys('cube')
		AC(driver).send_keys(Keys.ENTER).perform()
		text.send_keys('y')
		AC(driver).send_keys(Keys.ENTER).perform()
		text.send_keys('2009')
		AC(driver).send_keys(Keys.ENTER).perform()
		text.send_keys('second bailout')
		AC(driver).send_keys(Keys.ENTER).perform()
		text.send_keys('genesis block')
		AC(driver).send_keys(Keys.ENTER).perform()
		text.send_keys('satoshi nakamoto')
		AC(driver).send_keys(Keys.ENTER).perform()
		time.sleep(0.5)
		code = driver.find_element('xpath',xpath_text2)
		text_code = code.text

		code_list = text_code.split()
		word_dot  = code_list[4]
		word = word_dot.replace('.','')

		file = open("code.txt", "a")  # append mode
		file.write(f"{word}\n")
		file.close()
		driver.refresh()
	driver.close()
	driver.quit()

give_balance()


	# try:
	# 	proxy_driver.find_element('xpath', '//div[text()="Смена прошла успешно"]')
	# 	status = 'The proxy IP has changed :)'
	# except:
	# 	status = 'The proxy IP has not changed :('
	# time.sleep(1)
	# proxy_driver.close()
	# proxy_driver.quit()
	# print(status)

