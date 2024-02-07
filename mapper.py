#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
import time






def Instantiate_Driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--headless")
    chrome_options.BinaryLocation = "/usr/bin/google-chrome"
    driver_path = "/usr/bin/chromedriver"
    chrome_options.page_load_strategy = 'eager'   # Only waits till html has been loaded + parsed
    #chrome_options.page_load_strategy = 'normal'  # Waits for all resources to dl inc. images
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
    return(driver)


def map_site(BASE_URL):
    driver = Instantiate_Driver()
    SEARCHED = set()
    UNSEARCHED = {BASE_URL}
    CONNECTIONS = [[]]
    while UNSEARCHED != set():
        URL = UNSEARCHED.pop() #grabs an element and modifies set in place as well
        SEARCHED.add(URL)
        driver.get(URL)
        a_tags = driver.find_elements("xpath","//a[@href]")
        internal_links = set()
        external_links = set()
        for x in a_tags:
            try:
                image_classes = x.find_elements(By.CLASS_NAME,"next-image") + x.find_elements(By.CLASS_NAME,"previous-image")
                x = x.get_attribute('href')
                if x.find('//wasp-group.com') in [5,6] and x[-1]=='/' and all([x.find(ext)==-1 for ext in ["jpg","png","pdf","docx","jpeg"]]) and len(image_classes)==0: 
                    internal_links.add(x.replace('#',''))
                else: #external link or images
                    external_links.add(x)
            except StaleElementReferenceException:
                pass
        new_links = internal_links.difference(SEARCHED) #removes already searched links
        UNSEARCHED = UNSEARCHED.union(new_links) 
        CONNECTIONS.append([URL,internal_links,external_links])
        print(f'SEARCHED:{len(SEARCHED)}|UNSEARCHED:{len(UNSEARCHED)}')
        '''
        if any([x.find('fuel')!=-1 for x in internal_links]):
            internal_links = set([x if x.find('fuel')!=-1 else None for x in internal_links])
            print(f'{URL}->{internal_links}')
        '''
    driver.quit()
    df = pd.DataFrame(CONNECTIONS,columns=['URL','Internal links','External links'])
    df.to_csv(f'Website_map_{BASE_URL.replace("https://","").replace("https://","").replace(".com","").replace(".co.uk","").replace("/","")}.csv',index=False)
     
    

map_site('https://wasp-group.com/')

