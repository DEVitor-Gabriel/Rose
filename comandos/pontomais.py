from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tkinter import messagebox



##### CONFIGURAÇÕES ######
LOGIN = '0054.416.181-59'
PASS = 'alemar12345'


def pontomais():

    browser = webdriver.Chrome()

    browser.get('https://app.pontomaisweb.com.br/#/acessar')
    #assert 'Google' in browser.title


    login = browser.find_element(By.NAME, 'login')
    login.send_keys(LOGIN)

    password = browser.find_element(By.NAME, 'password')
    password.send_keys(PASS+Keys.ENTER)


    time.sleep(10)
    btn = browser.find_element(By.CLASS_NAME, 'btn-registrar')
    btn.click()

    time.sleep(10)

    msg_box = messagebox.askyesno(title='Confirmar', message='Tem certeza que deseja bater o ponto agora ?')
    
    if (msg_box == True):
        btn = browser.find_element(By.XPATH, '/html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div[1]/time-card-register/div/div[2]/div[2]/pm-card/div/div/pm-time-card-register/div[1]/div[3]/div/pm-button')
        btn.click()

    time.sleep(10)

    browser.quit()

# pontomais()