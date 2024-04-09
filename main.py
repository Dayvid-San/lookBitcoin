import requests
from time import sleep
import winsound
import tkinter as tk


URL_API = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
VALOR_LIMITE = float(input("Qual o valor mínimo da cotação?\n"))
INTERVALO = 60
ARQUIVO_SOM = "bitcoin.wav"

def obter_cotacao():
    resposta = requests.get(URL_API)
    dados = resposta.json()
    cotacao = dados["bpi"]["USD"]["rate_float"]
    return cotacao

def mostrar_janela():
    janela = tk.Tk()
    janela.title("Bitcoins!!!")
    janela.geometry("500x250")
    label = tk.Label(text="Hora de comprar Bitcoins!", font=("Arial", 20))
    label.pack()
    janela.mainloop()

while True:
    cotacao_atual = obter_cotacao()

    if cotacao_atual > VALOR_LIMITE:
        print('*'*30)
        print(f"Alerta! Cotação do Bitcoin ultrapassou o limite de {VALOR_LIMITE:.2f} USD!")
        print(f"Cotação atual: {cotacao_atual:.2f} USD")

        winsound.PlaySound(ARQUIVO_SOM, winsound.SND_FILENAME)
        mostrar_janela()

        break  

    else:
        print('-'*30)
        print(f"Cotação do Bitcoin está acima do limite de {VALOR_LIMITE:.2f} USD.")
        print(f"Cotação atual: {cotacao_atual:.2f} USD verificada há {INTERVALO} segundos atrás.")

    sleep(INTERVALO)
