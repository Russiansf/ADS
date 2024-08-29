from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from wallets import wallets
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
import time

url_faucet = 'https://artio.faucet.berachain.com/#dapps'
url_galxe = 'https://galxe.com/Berachain/campaign/GCTN3ttM4T' #'https://galxe.com/Berachain/campaign/GCjGGttCAG'
url_well3 = 'https://well3.com/mission'

xpath_checkbox = '//*[@role="checkbox"]'
xpath_i_agree = '//div//button[text()="I AGREE"]'
# xpath_i_agr = '//div[@role="dialog"]//button[text()="I AGREE"]'
xpath_i_agr = '//div[@class="flex gap-4"]'
xpath_wallet_adress = '//input'
xpath_head = '//div[@class="flex items-end justify-between px-6 py-3"]'
xpath_prove_not_a_bot = '//*[text()="Click here to prove you are not a bot"]'
xpath_drip_tokens = '//*[text()="Drip Tokens"]'

xpath_request_sub = '//h5[text()=" Request Submitted"]'
xpath_grey_list = '//h5[text()=" Wallet Grey-listed for 8 hours"]'
xpath_ohno = '//h5[text()=" Oh no!"]'
xpath_capcha = '//input[@type="checkbox"]'

# для галксе
# xpath_daily = '//div[@class="expand-icon"]' #'//div[contains(text(),"Daily Visit the Berachain Honey Dapp")]'
xpath_daily = '//div[@class="d-flex height-100 width-100 click-area"]'
xpath_check = '//div[@class="clickable refresh icon responsive ml-4"]' #'/html/body/div/div/div/div[3]/div[1]/main/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/button/div[2]/div/div/div/div/div/div'
#'(//div[@class="flex-all-center"])[2]'
xpath_btn_claim = '//div[text()="Claim 5 Points"]'
xpath_galxe_claimed = '//div[@class="btn-outter width-max-100"]'
xpath_x = '//*[@class="trp-close"]'
xpath_handle = '//span[text()="March of the Beras Daily Drip"]'

#well3

xpath_button = '(//button)[2]'
xpath_start = '(//button[text()="Start"])[1]'
xpath_imready = '//div[text()="I am ready"]'
# 30 sec
xpath_back = '//button[text()="Back to Questboard"]'
xpath_claimed = '(//button)[1]'

debug_on = True

def well3_daily(ads_id,index, driver, sec=15):
    debug('start well3')
    driver.get(url_well3)
    wait = WebDriverWait(driver, sec)
    time.sleep(5)
    # wait.until(ec.visibility_of_element_located((By.XPATH, xpath_button))).click()
    # driver.refresh()
    # input('...')
    try:
        try:
            try:
                start = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_start)))
                driver.execute_script("arguments[0].click();", start)
                wait.until(ec.visibility_of_element_located((By.XPATH, xpath_imready))).click()
                print(1)
            except:
                start = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_start)))
                driver.execute_script("arguments[0].click();", start)                
                wait.until(ec.visibility_of_element_located((By.XPATH, xpath_imready))).click()
                print(2)
            WebDriverWait(driver, 160).until(ec.visibility_of_element_located((By.XPATH, xpath_back))).click()
            time.sleep(3)
            debug('well3 claim')
        except:
            debug('well3 bug')
            # debug('well3 allready claimed')
            file = open("exc_acc.txt", "a")  # append mode
            file.write(f"well3 bug - {index} - {ads_id}\n")
            file.close()
    except:
        debug('well3 bug')
        file = open("exc_acc.txt", "a")  # append mode
        file.write(f"well3 bug - {index} - {ads_id}\n")
        file.close()
    # input('...')


def bera_faucet(index, ads_id, driver, sec=30):
    debug('start bara faucet')
    driver.get(url_faucet)
    wallet = wallets[ads_id]
    
    # try:    
        # try:
        #     # driver.execute_script("document.body.style.zoom='75%'")
        #     WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, xpath_checkbox))).click()            
        #     # print(0)
        #     time.sleep(2)
        #     # WebDriverWait(driver, sec=60).until(ec.visibility_of_element_located((By.XPATH,'//div[@class="rc-anchor-logo-img rc-anchor-logo-img-large"]')))
        #     button = driver.find_element(By.XPATH, xpath_i_agree)        
            
        #     driver.execute_script("arguments[0].click();", button)
        #     # WebDriverWait(driver, sec).until(ec.element_to_be_clickable((By.XPATH, xpath_i_agree))).click()
        #     # print(33)
        # except:        
        #     print('ok')
        # finally:
    # try:
    #     element = WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_head)))
    #     driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #     print(1)
    #     capcha = WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_capcha)))
    #     driver.execute_script("arguments[0].click();", capcha)
    #     print(2)        
    #     WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_wallet_adress))).send_keys(wallet)
    # except:
    #     time.sleep(3)
    #     element = WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_head)))
    #     driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #     print(3)  
    #     capcha = WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_capcha)))
    #     driver.execute_script("arguments[0].click();", capcha)      
    #     WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_wallet_adress))).send_keys(wallet)

    element = WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_head)))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # capcha = WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_capcha)))
    # driver.execute_script("arguments[0].click();", capcha)      
    WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_wallet_adress))).send_keys(wallet)
    # input('...')
    time.sleep(20)
    # WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_prove_not_a_bot))).click()
    # button2 = driver.find_element(By.XPATH, xpath_prove_not_a_bot)
    # driver.execute_script("arguments[0].click();", button2)

    # print(3)
    # time.sleep(5)

    # WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_drip_tokens)))
    # button3 = driver.find_element(By.XPATH, xpath_drip_tokens)
    # driver.execute_script("arguments[0].click();", button3)
    
    # print(4)
    # except:
        # debug('#######---Ups bara faucet bug---#######')
        # # input('continue')
        # # debug('gecco claimed')
        # file = open("exc_acc.txt", "a")  # append mode
        # file.write(f"bara faucet bug - {index} - {ads_id}\n")
        # file.close()
                    # user_input = input('Проверишь что там? Y/N')
    
    # try:
    #     try:
    #         WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_request_sub)))
    #         debug('bera tokens claimed')
    #         # driver.close()
    #     except:
    #         WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_grey_list)))
    #         debug('bera tokens allready claimed')
    # except:
    #     WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_ohno)))
    #     debug('bera false hight trafic')

    # except:
    #     debug('bera bug')
    #     file = open("exc_acc.txt", "a")  # append mode
    #     file.write(f"bera bug - {index} - {ads_id}\n")
    #     file.close()


def bera_galxe(ads_id,index, driver, sec=30):
    debug('start bera galxe')
    driver.get(url_galxe)
    wait = WebDriverWait(driver, sec)
    try:        
        # window = driver.current_window_handle
        # print(window)
        # wait.until(ec.visibility_of_element_located((By.XPATH, xpath_x))).click()
        wait = WebDriverWait(driver, sec)
        link = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_daily)))   
        # AC(driver).key_down(Keys.CONTROL).perform()
        AC(driver).key_down(Keys.COMMAND).perform() # for Mac
        # time.sleep(1)
        # driver.execute_script("arguments[0].click();", link)
        # print('click 1')
        link.click()
        print('click 1')
        time.sleep(30)
        check = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_check)))
        # AC(driver).move_to_element(link).perform()
        # print('find')
        try:
            driver.execute_script("arguments[0].click();", check)
            print('click1')
            time.sleep(3)
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_btn_claim))).click()
            time.sleep(3)
        except:
            time.sleep(3)
            # check = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_check)))
            # driver.execute_script("arguments[0].click();", check)
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_check))).click()
            print('click2')
            time.sleep(3)
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_btn_claim))).click()
            time.sleep(3)
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_x))).click()
        time.sleep(2)
        try:
            # wait.until(ec.visibility_of_element_located((By.XPATH, xpath_btn_claim))).click()
            # time.sleep(3)
            debug('bera galxe claim')
        except:
            debug('bera galxe claim')
    except:
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_galxe_claimed)))
        debug('bera galxe allready claim')
        file = open("exc_acc.txt", "a")  # append mode
        file.write(f"bera galxe bug - {index} - {ads_id}\n")
        file.close()
    # input('...')




def debug(txt):
    if debug_on:
        log(txt)
        

def log(txt):
    print(txt)
    file = open("log_gm.txt", "a")  # append mode
    file.write(f"{txt} \n")
    file.close()