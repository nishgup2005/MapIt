from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys

driver=webdriver.Chrome()

elem=driver.find_element(By.NAME,"q")
if len(sys.argv)>1:
    address=" ".join(sys.argv[1:])
else:
    address=input("Enter Address to be searched here: ")

elem.send_keys(address)
elem.send_keys(Keys.RETURN)
address=input()
