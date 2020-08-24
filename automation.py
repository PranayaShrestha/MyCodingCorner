from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://animeheaven.ru/")

try:
    
    search = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "keyword"))
    )

    search.send_keys("one piece")
    search.send_keys(Keys.RETURN)
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "iep"))
    )
    element.click()
    
    episode = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "centerv"))
    )
    episode.click()
    
except:
    driver.quit()