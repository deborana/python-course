import pyautogui # type: ignore
import time
import pandas as pd

#após 5 seg de rodar o programa, pega a posicao do mouse
time.sleep(5)
print(pyautogui.position())

#nome das teclas
#print(pyautogui.KEYBOARD_KEYS)

#le arquivo e printa tabela
#tabela = pd.read_csv("produtos.csv")
#print(tabela)