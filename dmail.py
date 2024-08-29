# Для Magic нужен кош

url_magic = 'https://magic.store/'

xpath_vote = '//a[text()="Vote"]'
xpath_continoe = '//a[text()="Continue on Voting"]'
xpath_vote_yes = '(//div[@class="radio-button-icon"])[5]'
xpath_poccet_btn = '//button[text()="Continue"]' # если вылезет поккет
xpath_next_btn = '//button[text()="Next"]'
xpath_confirm_btn = '//button[text()="Confirm"]'
# думаю надо переключится на последнюю вкладку, чтоб взаимод с кошелём
xpath_confirm_txn = '(//button)[6]'# кнопка из метамаска
# ниже для валидации войтинга
# //h2[text()="Vote Registered"]
# //button[text()="Close"]
xpath_metamask = '//span[text()="MetaMask"]' #//li[@class="item "]
xpath_rabby = '(//button)[1]' # это две кнопки

# рефреш и погнали по кругу

#  нужен кош





from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

# Ai Arena daily drop

url_dmail = 'https://mail.dmail.ai/compose'
url_dmail_log = 'https://mail.dmail.ai/login?path=%2Fcompose'

xpath_mail_to_1 = '(//span[@class="email"])[1]'
xpath_mail_to_2 = '(//span[@class="email"])[2]'
xpath_subject = '(//input[@type="text"])[3]'
xpath_mail_text = '(//div//p)[10]'
xpath_send_btn = '//span[text()="Send"]'
xpath_network = '(//span[text()="Polygon Mainnet"])[2]'
xpath_sent = '//div[text()="Sent"]'
xpath_compose = '//span[text()="Compose"]'

xpath_metamask = '//span[text()="MetaMask"]' #//li[@class="item "]
xpath_poccet_btn = '//button[text()="Continue"]'
xpath_rabby = '(//button)[1]' # это две кнопки

debug_on = True


def dmail_send_mail(index, ads_id, driver, sec=5):
    debug('start send Dmail')
    driver.get(url_dmail)
    if driver.current_url == url_dmail_log:
        dmail_wallet_log(index, ads_id, driver, sec)
    dmail_send(index, ads_id, driver, sec)
    debug('Dmail sent emails')
    input('...')



def dmail_wallet_log(index, ads_id, driver, sec=5):
    global wait
    wait = WebDriverWait(driver, sec)
    debug('wallet connect Dmail')
    try:
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_metamask))).click()
        # except:
        # тут переключится на окно -1
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_poccet_btn))).click()
            
        # тут переключится на окно -1
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_rabby))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_rabby))).click()
    except:
        debug('-----что-то не так с регой Dmail------')
        file = open("exc_acc.txt", "a")  # append mode
        file.write(f"Dmail reg bug - {index} - {ads_id}\n")
        file.close()

def dmail_send(index, ads_id, driver, sec=5):    
    # if driver.current_url != url_dmail:
    #     driver.get(url_dmail)
    # global escape
    try:        
        sent_mail(curr_xpath = xpath_mail_to_1)
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_compose))).click()
        sent_mail(curr_xpath = xpath_mail_to_2)

    except:
        debug('-----что-то не так Dmail------')
        file = open("exc_acc.txt", "a")  # append mode
        file.write(f"Dmail send bug - {index} - {ads_id}\n")
        file.close()


def sent_mail(curr_xpath, driver, sec=5):    
    select_adres = wait.until(ec.visibility_of_element_located((By.XPATH, curr_xpath)))
    select_adres.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath_subject))).send_keys('Hello world!')
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath_mail_text))).send_keys('Hello world!')
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath_send_btn))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath_sent)))


def debug(txt):
    if debug_on:
        log(txt)
        

def log(txt):
    print(txt)
    file = open("log_gm.txt", "a")  # append mode
    file.write(f"{txt} \n")
    file.close()


    