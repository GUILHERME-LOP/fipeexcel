import requests
import json

def consulta_marca(tipo):
    headers_info={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'}
    url=f'http://parallelum.com.br/fipe/api/v2/{tipo}/brands'
    dados=requests.get(url=url,headers=headers_info)

    dados_json=json.loads(dados.content)

    return dados_json