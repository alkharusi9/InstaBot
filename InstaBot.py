try:
    from selenium import webdriver
except:
    print("[!] Please install selenium with 'pip install selenuim' ")
from getpass import getpass
import time



def Automation():
    username = input('Username:')
    password = input('Password:')

    try:
        # Start chrome
        driver = webdriver.Chrome()
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        # Enter login credentials
        loginBar = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        loginBar.send_keys(username)
        loginPasswd = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        loginPasswd.send_keys(password)
        loginButton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]')
        loginButton.click()




    except KeyboardInterrupt:
        print('[!] You clicked CTRL+C to stop the Bot')

if __name__=='__main__':
    Automation()