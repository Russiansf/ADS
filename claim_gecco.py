from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

url_gecco = 'https://www.coingecko.com/account/candy'
url_raffle = 'https://www.coingecko.com/account/my-rewards/c56843e9-c55b-4bac-8558-10cc3067899e'
# https://www.coingecko.com/account/rewards/axieinfinity-raffle
url_raffle_pg = 'https://sweepwidget.com/c/76798-pbqwict2'


xpath_collect_gecco = '(//button[@type="submit"])[2]'
xpath_collect_gecco_confirmed = '//div[@class="btn bg-secondary col-12 text-sm text-white collect-candy-button"]'
xpath_allready_collect = '//span[@id="next-daily-reward-countdown-timer"]'

xpath_capcha = '//input[@type="checkbox"]'
xpath_login_btn = '(//button[@type="submit"])[1]'

debug_on = True


def start_gecco(index, ads_id, driver, sec=3):
    debug('start gecco claim')
    driver.get(url_gecco)
    try:
        gecco_claim = WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_collect_gecco)))
        gecco_claim.click()        
        gecco_confirm = WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_collect_gecco_confirmed)))        
        debug('gecco claimed')
        # driver.close()
    except:
        try:
            WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_allready_collect)))
            debug('gecco allready claimed')
            # driver.close()
        except:
            try:
                driver.refresh()
                gecco_claim.click()        
                gecco_confirm
                debug('gecco claimed')
            except:
                try:
                    driver.refresh()
                    gecco_claim.click()        
                    gecco_confirm
                    debug('gecco claimed')
                except:
                    debug('#######---Похоже капча---#######')
                    # input('...')
                    # input('continue')
                    # debug('gecco claimed')
                    file = open("exc_acc.txt", "a")  # append mode
                    file.write(f"Gecco bug капча - {index} - {ads_id}\n")
                    file.close()
                    # user_input = input('Проверишь что там? Y/N')


def debug(txt):
    if debug_on:
        log(txt)
        

def log(txt):
    print(txt)
    file = open("log_gm.txt", "a")  # append mode
    file.write(f"{txt} \n")
    file.close()