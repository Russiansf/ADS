from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.common.keys import Keys


url_gm = 'https://layer3.xyz/quests'
url_ = ''
url_ = ''

xpath_gm = '(//button[text()="gm"])[2]'
xpath_streak = '//p[@class="body text-4xs font-normal text-content-tertiary"]' #'//p[text()="day gm streak!"]' 
xpath_close = '//button[text()="Close"]'
xpath_sign_in = '//span[text()="Sign in"]'

xpath_restart1 = '(//button[text()="Restart"])[1]'
xpath_restart2 = '(//button[text()="Restart"])[3]'

debug_on = True


def layer3_gm(index, ads_id, driver, sec=30):    
    debug('start layer3 gm')
    driver.get(url_gm)
    # try:
        # WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_sign_in)))
        # ac(driver)
        # debug('layer3 dont signed')
        # input('continue')
        # file = open("exc_acc.txt", "a")  # append mode
        # file.write(f"layer3 dont signed - {index} - {ads_id}\n")
        # file.close()
    # except:
    try:
        try:
            WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_gm))).click()    
            # WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_received)))
            debug('gm completed')        
        except:
            WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_streak)))
            debug('gm already completed')
    except:
        try:
            WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_close))).click()
            try:
                WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_gm))).click()    
                # WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_received)))
                debug('gm completed')        
            except:
                WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_streak)))
                debug('gm already completed') 
        except:
            try:
                WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_restart1))).click()
                WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_restart2))).click()
                debug('gm completed')
            except:
                debug('Что-то не так')
                # input('continue')
                # debug('gm completed')
                file = open("exc_acc.txt", "a")  # append mode
                file.write(f"Layer3 bug - {index} - {ads_id}\n")
                file.close()
    

def debug(txt):
    if debug_on:
        log(txt)
        

def log(txt):
    print(txt)
    file = open("log_gm.txt", "a")  # append mode
    file.write(f"{txt} \n")
    file.close()