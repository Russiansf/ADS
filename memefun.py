import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import zipfile

# discord_tokens = [
#                   'MTIyNzA5NzE2Nzk0OTMzNjU3OA.GvOPnK.nQWhYknGRBZ-f4yeiQRiu0_5OGOcZE-isZgCvE',
# 				  'MTIyNzEwNTg3NDM0NzI5ODgyNg.GG5DhV.IwAvf-CQCVP51DwVy8IV8Rvp8TxWotb76sGfQg'
#                   ]

# Настройки прокси
proxy_host = "x54.fxdx.in"
proxy_port = "16193"
proxy_username = "excursorsf085542"
proxy_password = "dce23aqzfkrj"

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (proxy_host, proxy_port, proxy_username, proxy_password)

plugin_file = 'proxy_auth_plugin.zip'

with zipfile.ZipFile(plugin_file, 'w') as zp:
    zp.writestr('manifest.json', manifest_json)
    zp.writestr('background.js', background_js)

chrome_options = Options()

prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_extension(plugin_file)

# chrome_options.add_argument(f'--user-agent={user_agent}')

chrome_options.add_argument(f'--proxy-server=http://{proxy_host}:{proxy_port}')
chrome_options.add_argument(f"--proxy-auth={proxy_username}:{proxy_password}")

chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--disable-features=ImprovedCookieControls')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

# chrome_options.add_argument("--headless")  # Run Chrome WebDriver in headless mode (without UI)

webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

wait = WebDriverWait(driver, 30)

# # for i in range(1,3):
# for token, i in zip(discord_tokens, range(1,3)):

# 	time.sleep(5)

# 	if "https://discord.com/channels/@me" in driver.current_url:
# 		print("Login Successful")
# 	else:
# 		print("Login Failed")
		
# 	time.sleep(5)

# 	driver.get("https://meme.fun/login")

# 	wait.until(ec.visibility_of_element_located(('xpath', '(//button)[1]'))).click()

# 	wait.until(ec.visibility_of_element_located(('xpath', '(//button[@class="sc-jxOSlx sc-hHOBiw jNSoSx jAOnTc"])[3]'))).click()

# 	wait.until(ec.visibility_of_element_located(('xpath', '//div[text()="Authorize"]'))).click()

# 	time.sleep(15)

# 	driver.get('https://meme.fun/$delovoydao')
# 	time.sleep(5)

# 	wait.until(ec.visibility_of_element_located(('xpath', '//span[text()="post"]'))).click()
# 	time.sleep(5)
# 	download = driver.find_element('xpath', '//input[@type="file"]')

# 	download.send_keys(f'{os.getcwd()}/memes/meme{i}.jpeg')

# 	wait.until(ec.visibility_of_element_located(('xpath', '//button[text()="post"]'))).click()
# 	time.sleep(5)

# 	driver.get('https://discord.com/login')
# 	time.sleep(5)
# 	wait.until(ec.visibility_of_element_located(('xpath', '(//button)[4]'))).click()
# 	wait.until(ec.visibility_of_element_located(('xpath', '//div[text()="Log Out"]'))).click()
# 	wait.until(ec.visibility_of_element_located(('xpath', '(//button[@type="submit"])[2]'))).click()

# 	time.sleep(5)

# 	if i % 2 != 0:
# 		time.sleep(1800)


tokens = ["token1", "token2", "token3"]  # Замените на реальные токены

token_twiter = '0646d9c3510a5a015719c39736ab23076e724cee'

driver.get("https://twitter.com")

time.sleep(5)

driver.add_cookie({'domain': '.twitter.com', 
'expiry': 1749500881, 
'httpOnly': True, 
'name': 'auth_token', 
'path': '/', 
'sameSite': 'None', 
'secure': True,
'value': token_twiter
})

print(driver.get_cookie('auth_token'))

driver.refresh()

time.sleep(5)