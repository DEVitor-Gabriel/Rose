from datetime import datetime

hr_atual = datetime.now().time()
hr_atual = str(hr_atual).split(':')

if (12 <= int(hr_atual[0]) <= 14):

    print('ponto batido')
        # btn = browser.find_element(By.CLASS_NAME, 'pm-btn-icon btn-register')
        # btn.click()

elif(17 <= int(hr_atual[0]) <= 19):
    print('ponto tarde batido')

else:
    print('Horario indisponivel')
