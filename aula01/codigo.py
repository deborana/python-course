#Passo a passo do projeto (lógica do programa)

#1. Abrir o sistema da empresa

import pyautogui
import time
pyautogui.PAUSE = 1

#entrando no chrome
pyautogui.press("win")
pyautogui.click(x=940, y=66)
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=999, y=625)

#entrando no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

#2. Fazer login

pyautogui.press("tab")
pyautogui.write("meu_email@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha_senha")
pyautogui.press("tab")
pyautogui.press("enter")


#3. Importar base de dados do produto para cadastrar

import pandas as pd

tabela = pd.read_csv("produtos.csv")

#4. Cadastrar um produto
#5. Repetir até acabar a lista de produtos

for linha in tabela.index:

    pyautogui.click(x=838, y=319)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)




