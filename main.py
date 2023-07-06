from itertools import count
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from faker import Faker
import random
import requests as req
import time
import os,colorama
from colorama import Fore
import json
from colorama import Fore
from selenium.webdriver.support import expected_conditions as EC
import calendar


colorama.init()
config = json.loads(open("config.json","r").read())

print(Fore.LIGHTBLUE_EX,f"""
     ######   ##     ##    ###    #### ##                                                                   
##    ##  ###   ###   ## ##    ##  ##                                                                   
##        #### ####  ##   ##   ##  ##                                                                   
##   #### ## ### ## ##     ##  ##  ##               By : {Fore.MAGENTA}{config["author"]}   {Fore.LIGHTBLUE_EX}                                                 
##    ##  ##     ## #########  ##  ##               Version : {config["version"]}                 
##    ##  ##     ## ##     ##  ##  ##                                                                   
 ######   ##     ## ##     ## #### ########{Fore.LIGHTGREEN_EX}                                                             
                   ######   ######## ##    ## ######## ########     ###    ########  #######  ########  
                  ##    ##  ##       ###   ## ##       ##     ##   ## ##      ##    ##     ## ##     ## 
                  ##        ##       ####  ## ##       ##     ##  ##   ##     ##    ##     ## ##     ## 
                  ##   #### ######   ## ## ## ######   ########  ##     ##    ##    ##     ## ########  
                  ##    ##  ##       ##  #### ##       ##   ##   #########    ##    ##     ## ##   ##   
                  ##    ##  ##       ##   ### ##       ##    ##  ##     ##    ##    ##     ## ##    ##  
                   ######   ######## ##    ## ######## ##     ## ##     ##    ##     #######  ##     ## {Fore.RESET}
      """)

fake = Faker()

def create():
    first_name = fake.first_name()
    last_name = fake.last_name()
    random_number = random.randint(35213, 999999)
    password = f"ItachiOnTop#0082"
    email = f"itxchiakar{random_number}"

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://accounts.google.com/signup/v2/createaccount?biz=false&cc=TR&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&authuser=0")
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.ID, "firstName")))
    time.sleep(2)
    first = driver.find_element(By.ID,"firstName")
    last = driver.find_element(By.ID,"lastName")
    first.send_keys(first_name)
    time.sleep(1)
    last.send_keys(last_name)
    next_btn1 = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button")
    next_btn1.click()
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.ID, "year")))
    driver.find_element(By.ID ,"month").send_keys(random.choice(calendar.month_name))
    time.sleep(0.5)
    driver.find_element(By.ID ,"gender").send_keys("Male")
    time.sleep(0.5)
    driver.find_element(By.ID ,"day").send_keys(str(random.randint(10,22)))
    time.sleep(0.5)
    driver.find_element(By.ID ,"year").send_keys("1978")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button").click()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input").send_keys(email)
    except:
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(email)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
    time.sleep(1.5)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(password)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(password)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button").click()
    time.sleep(1)
    driver.find_element(By.ID,"phoneNumberId").send_keys(config["tel"])
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button").click()
    time.sleep(1)
    txt = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[2]/div").text
    print(txt)
    if txt == "This phone number format is not recognized. Please check the country and number." or txt == "This phone number has been used too many times":
        print(f"{Fore.RED}[-] Telefon numarası sorunlu...{Fore.RESET}")
        exit()
    print("Doğrulamayı tamamlayın....")
    WebDriverWait(driver,100000).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input")))
    open("hesaps.txt","a").write(f"{email}@gmail.com:{password}\n")
    time.sleep(30)
    driver.close()

while True:
    create()