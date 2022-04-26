from pandas import json_normalize
import requests
import json
'''
def consulta_marca(tipo):
    headers_info={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'}
    url=f'http://parallelum.com.br/fipe/api/v2/{tipo}/brands'
    dados=requests.get(url=url,headers=headers_info)

    dados_json=json.loads(dados.content)

    return dados_json


def consulta_modelo_ano(codico_marca,ano):
    headers_info={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'}
    url=f'https://parallelum.com.br/fipe/api/v2/{tipo}/brands/{id_marca}/models'
    dados=requests.get(url=url,headers=headers_info)

    dados_json=json.loads(dados.content)

    return dados_json
'''
class API:
    def __init__(self,tipo_veiculo) :
        self.url_busca_marca=f'http://parallelum.com.br/fipe/api/v2/{tipo_veiculo}/brands'
        self.url_busca_veiculo=f''

    def busca_marca_por_tipo(self):
        headers_info={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'}
        dados = requests.get(url=self.url_busca_marca,headers=headers_info)
        if dados.status_code==200:
            json_dados=json.loads(dados.content)
            return json_dados
        return {}

    def busca_veiculo_por_marca(self):
        pass

