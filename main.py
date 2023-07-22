from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

webdriver = webdriver.Chrome()


# adding zip codes
for i in range(20602,21931,1):
    webdriver.get('https://www.dllr.state.md.us/cgi-bin/ElectronicLicensing/OP_Search/OP_search.cgi?calling_app=HIC::HIC_business_location')
    time.sleep(1)
    zip_input=webdriver.find_element(By.NAME,value='zip')
    zip_input.clear()
    zip_input.send_keys(i)
    time.sleep(1)
    zip_input.send_keys(Keys.ENTER)
    time.sleep(1)
    new_url=webdriver.current_url
    try:
        webdata = WebDriverWait(webdriver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/form/table"))).get_attribute("outerHTML")
        data  = pd.read_html(webdata)
        for datas in data:
            datas.to_csv("new.csv", header=False, index=False, mode='a')
    except Exception as ex:
        print(0)
