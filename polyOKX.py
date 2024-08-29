from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

url_poly = 'https://star.legend.game/mint/ticket'
xpath_daily = '//span[text()="Claim Ticket"]'
xpath_wallet_confirm = '//div[text()="Confirm"]'
xpath_daily_done = '//*[text()="Done"]'
xpath_allready_claim = '//*[text()="Claim after "]'

debug_on = True


def daily_ticket(driver, sec=3): #index, ads_id, 
	debug('start polly claim')
	driver.get(url_poly)
	WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_daily))).click()
	try:
		WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_wallet_confirm))).click()
	except:
		WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH,xpath_allready_claim)))
		debug('polly allready claimed')

	WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_daily_done)))        
	debug('polly claimed')
		# driver.close()
  

def debug(txt):
    if debug_on:
        log(txt)
        

def log(txt):
    print(txt)
    file = open("log_gm.txt", "a")  # append mode
    file.write(f"{txt} \n")
    file.close()