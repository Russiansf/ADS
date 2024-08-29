from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

url_arena = 'https://gt.aiarena.io/'

xpath_balance = '(//td[@class="Leaderboard_leaderboard__cell__sRFm2"])'
xpath_lider = '//p[text()="Leaderboards"]'
xpath_next = '//button[text() ="Next"]'

options = webdriver.ChromeOptions()
# options.add_argument('--headless')

def give_balance():
	driver = webdriver.Chrome(options=options)
	driver.get(url=url_arena)
	driver.find_element('xpath',xpath_lider).click()
	time.sleep(35)
	for page in range(1,172): #172
		for i in range(1,51):
			number = i * 2
			adress = number - 1
			# if not number % 2 == 0:
			# 	number += 1
			time.sleep(0.5)
			wallet = driver.find_element('xpath',f'{xpath_balance}[{adress}]')
			balance = driver.find_element('xpath',f'{xpath_balance}[{number}]')
			# balance = WebDriverWait(driver, 300).until(ec.visibility_of_element_located('xpath',f'{xpath_balance}[{number}]'))
			text_wallet = wallet.text
			text_balace = balance.text
			file = open("balance_ai_champ.xls", "a")  # append mode
			file.write(f"{text_wallet}{text_balace}\n")
			file.close()
		driver.find_element('xpath',xpath_next).click()
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

