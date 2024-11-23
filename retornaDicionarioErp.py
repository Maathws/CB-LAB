import json
import requests


def retornaDicionarioErpUsandoRequests():
    url = "https://....com/erp.json"

    try:
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dicionarioErp = resposta.json()

            print(f'Dicionario ERP:\n{dicionarioErp}')

            return dicionarioErp
        
        else:
            print(f'Erro: {resposta.status_code}')

    except Exception as e:
        print(f'Erro ao fazer a requisição: {e}')

def retornaDicionarioErp():
    erpJson = 'ERP.json'

    try:
        with open(erpJson, 'r') as file:
            dicionarioErp = json.load(file)
            print(f'Dicionario ERP:\n{dicionarioErp}')

            return dicionarioErp

    except Exception as e:
        print(f'Erro ao abrir o arquivo Json: {e}')
