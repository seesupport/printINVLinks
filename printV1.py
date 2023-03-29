from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 

options = Options()
#options.headless = True
options.add_argument(
        "--kiosk-printing"
)
options.add_argument(
        "--headless"
)
driver = webdriver.Chrome(options=options)

driver.get('https://preprod.invoicing.eta.gov.eg/print/documents/KAANRXWG1178G4D84ZFCJHWG10/share/GBTGTF753SYZKZ0M4ZFCJHWG10X9SL5U1679921922')
time.sleep(5)
myBtn = driver.find_element(By.ID, 'LanguageButton')
myBtn.click()
time.sleep(5)
myBtn = driver.find_element(By.ID, 'PrintButton')
myBtn.click()

# LanguageButton