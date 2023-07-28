import pandas as pd
import pyautogui
import time
import pandas

pyautogui.press("win")
time.sleep(5)
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.click(x=568, y=45)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

pyautogui.click(x=529, y=361)
pyautogui.write('meuemail@gmail.com')
pyautogui.press('tab')
pyautogui.write('minhasenha')
pyautogui.click(x=621, y=515)
time.sleep(2)

tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:
    pyautogui.click(x=530, y=240)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    if not pd.isna(tabela.loc[linha, 'obs']):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)
