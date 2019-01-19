from selenium import webdriver
from header.login import login_manager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

log = login_manager(driver,"jorge.cruces@corazondechileno.cl","cacatua123")
log.enter_ins()

time.sleep(1)

driver.get("https://www.instagram.com/p/BrhkBbJjArG/")
time.sleep(1)

