import pyautogui
from time import sleep
from datetime import datetime

# funções
def abrir_navegador(navegador):
    pyautogui.press('win')
    pyautogui.write(navegador)
    pyautogui.press('enter')
    sleep(3)

def abre_aula(url):
    sleep(2)
    pyautogui.write(url)
    pyautogui.press('enter')
    sleep(2)

def desliga_cam_mic():
    sleep(5)
    pyautogui.hotkey('ctrlleft', 'd')
    pyautogui.hotkey('ctrlleft', 'e')
    pyautogui.click(1230,547, duration=0.25)
    print("foi")

def iniciar():
    aulas = {"seg": "https://meet.google.com/opb-wubt-bov", "ter": "https://meet.google.com/nnw-mkft-wos",
    "quar": "https://meet.google.com/wwu-tkhv-ysy", "qui": "https://meet.google.com/nmm-ukuy-htj"}

    a = datetime.now()
    dias = ['seg', 'ter', 'quar', 'qui', 'sex', 'sab', 'dom']
    dia_semana = dias[a.weekday()]

    if dia_semana in aulas.keys():
        abrir_navegador("brave")
        abre_aula(aulas[dia_semana])
        desliga_cam_mic()
    else:
        print("Hoje não tem aula")

iniciar()
