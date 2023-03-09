import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

website = input("input website link: ")
print("input website link:", website)
email_xpath = input("input Xpath 1: ")
print("Xpath entered e-mail:", email_xpath)
submit_xpath = input("input Xpath 2: ")
print("The xpath submit that was entered:", submit_xpath)
time.sleep(1)

def start():
    data = pd.read_csv('emaildata.csv')
    recycle = data.shape[0]
    for i in range(recycle):
        print(i)
        driver = webdriver.Chrome(executable_path='fill with the path directory your chrome path')
        driver.get(website)
        time.sleep(3)

# Autofill Emails
        email = data.iloc[i]['email']
        input_email = driver.find_element(By.XPATH, email_xpath)
        for j in email:
            input_email.send_keys(j)
            time.sleep(0.05)

# click button
        submit = driver.find_element(By.XPATH, submit_xpath)
        submit.click()
        time.sleep(0.5)

start()
time.sleep(10)
