from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkinter import *
'''
//*[@id="identifierNext"]/div/button/span
//*[@id="passwordNext"]/div/button/span
//*[@id="password"]/div[1]/div/div[1]/input
'''
options = webdriver.ChromeOptions()
options.add_argument('start-minimized')
options.add_argument(r'--user-data-dir=C:\Users\Multimídia ADEV11\AppData\Local\Google\Chrome\User Data')
executavel_path = "C:/Users/Multimídia ADEV11/AppData/Local/Programs/Python/Python39/chromedriver.exe"
driver = webdriver.Chrome(executable_path=executavel_path, options=options)
driver.get('https://www.google.com')
'''driver.implicitly_wait(10)
driver.get("https://studio.youtube.com/video/QrBSuhX1D9g/livestreaming")
digitaremail = driver.find_element_by_xpath('//*[@id="identifierId"]')
digitaremail.click()
digitaremail.send_keys('adev.onze@gmail.com')
botao_email = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
botao_email.click()
digitarsenha = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
digitarsenha.click()
digitarsenha.send_keys('adev@2018')
botao_senha = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
botao_senha.click()'''
