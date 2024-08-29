from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

change_proxy_ip = 'https://i.fxdx.in/api-rt/changeip/PfN2khepA3/xBNPH7HBX6SFT3TN4A4GB'

options = webdriver.ChromeOptions()
options.add_argument('--headless')

service = Service(executable_path=ChromeDriverManager().install())

def change_proxy():
	proxy_driver = webdriver.Chrome(options=options, service=service)
	proxy_driver.get(url=change_proxy_ip)
	try:
		# proxy_driver.find_element('xpath', '//div[text()="Смена прошла успешно"]')
		status = 'The proxy IP has changed :)'
	except:
		status = 'The proxy IP has not changed :('
	time.sleep(1)
	proxy_driver.close()
	proxy_driver.quit()
	print(status)