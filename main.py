import requests
from time import sleep
import winsound
import os


URL_API = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
VALOR_LIMITE = 50000
INTERVALO = 60
ARQUIVO_SOM = "ativado.wav"

def obter_cotacao():
    resposta = requests.get(URL_API)
    dados = resposta.json()
    cotacao = dados["bpi"]["USD"]["rate_float"]
    return cotacao

while True:
    cotacao_atual = obter_cotacao()

    if cotacao_atual > VALOR_LIMITE:
        print('*'*30)
        print(f"Alerta! Cotação do Bitcoin ultrapassou o limite de {VALOR_LIMITE:.2f} USD!")
        print(f"Cotação atual: {cotacao_atual:.2f} USD")

        os.system("start " + os.path.join(os.getcwd(), "bitcoin.mp3"))

        break  

    else:
        print('-'*30)
        print(f"Cotação do Bitcoin está abaixo do limite de {VALOR_LIMITE:.2f} USD.")
        print(f"Cotação atual: {cotacao_atual:.2f} USD verificada há {INTERVALO} segundos atrás.")

    # Aguardar intervalo antes da próxima verificação
    sleep(INTERVALO)
