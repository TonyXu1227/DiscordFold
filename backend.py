import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

runtime_button = driver.find_element(By.XPATH, "//*[@id='runtime-menu-button']")
runtime_button.click()
run_all_button = driver.find_element(By.XPATH, "//*[@id=':1v']")
run_all_button.click()
sign_in = driver.find_element(By.XPATH, "//*[@id='button']/span[1]")
sign_in.click()

service = Service(executable_path="/Users/bigricce1227/Documents/Coding Projects/Boilermake 25/DiscordFold/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb")

sequence = driver.find_element(By.XPATH, "//md-outlined-text-field[@data-aria-label = 'query_sequence']")
sequence.send_keys((Keys.BACKSPACE*60))
sequence.send_keys("MASFGSDKLQWTEYRCVNQQPUINCO")

name = driver.find_element(By.XPATH, "//md-outlined-text-field[@data-aria-label = 'jobname']")
name.send_keys((Keys.BACKSPACE*4))
name.send_keys("new_protein")

runtime_button = driver.find_element(By.XPATH, "//*[@id='runtime-menu-button']")
runtime_button.click()
run_all_button = driver.find_element(By.XPATH, "//*[@id=':1v']")
run_all_button.click()
sign_in = driver.find_element(By.XPATH, "//*[@id='button']/span[1]")
sign_in.click()

time.sleep(100)

driver.quit()