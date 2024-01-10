import pyautogui
import time

#Tempo de espera entre comandos
pyautogui.PAUSE = 0.5

#Abrindo o Sitema de Cadrastro

pyautogui.click(x=34, y=348,clicks=2)
time.sleep(2)
pyautogui.click(x=696, y=419)
time.sleep(2)
pyautogui.click(x=1341, y=92)
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Fazendo Login
time.sleep(1)
pyautogui.click(x=476, y=359)
pyautogui.write("gmailFicticio01@gmail.com")
time.sleep(2)
pyautogui.press("tab")
pyautogui.write("0987654321")
time.sleep(0.5) 
pyautogui.press("tab")
pyautogui.press("enter")

#Importando a Tabela
import pandas as pd
tabela = pd.read_csv("produtos.csv")

#cadastrando os Produtos
for linha in tabela.index:
    pyautogui.click(x=486, y=245)
    #Codigo do Produto
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    time.sleep(0.5)
    #Marca do Produto
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    #Tipo do Produto
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    #Categoria do Produto
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    #Preço do Produto
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    #Custo do Produto
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    #Obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
      pyautogui.write(obs)
    #Enviar Arquivo
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)



