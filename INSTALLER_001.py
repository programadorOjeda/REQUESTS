import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import *




def valor_moedas():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    requisicao_dic = requisicao.json()

    cotaco_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']


    texto = f'''

        Dólar: {cotaco_dolar}
        Euro: {cotacao_euro}
        BitCoin: {cotacao_btc}
'''

    texto_cotação['text'] = texto

janela = Tk()
janela.title('Cotação das Moedas')
janela.geometry('260x180')

texto_orientação = Label(janela, text='Clique no botão pra ver os valores das moedas')
texto_orientação.grid(column=0, row=0,padx=10, pady=10)

botão = Button(janela, text='Buscar cotação Dólar/Euro/Ouro', command=valor_moedas)
botão.grid(column=0, row=1,padx=10, pady=10)

texto_cotação = Label(janela, text='')
texto_cotação.grid(column=0, row=2,padx=1, pady=5)

janela.mainloop()