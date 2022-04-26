#lib pera pegar dados da internet 

import json
import requests
import xlsxwriter
from tqdm import tqdm

headers_info={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'}

dados = requests.get('http://parallelum.com.br/fipe/api/v2/motorcycles/brands', headers = headers_info)
linha=1


lista_resposta=json.loads(dados.content)

documento_excel=xlsxwriter.Workbook('fipe.xlsx')
planilha_excel= documento_excel.add_worksheet('marcas')
tamanho_lista=0

planilha_excel.write(0,0,'MARCA')
planilha_excel.write(0,1,'CÓDICO')


print('*' * 164)

for marca in tqdm(lista_resposta):

    print(f"{marca.get('name')} - {marca.get('code')}")
    planilha_excel.write(linha,0,marca.get('name'))
    planilha_excel.write(linha,1,marca.get('code'))
    linha+=1


planilha_excel_motos= documento_excel.add_worksheet('motos')   
dados_modelo=requests.get(url='http://parallelum.com.br/fipe/api/v2/motorcycles/brands/101/models',headers=headers_info)

lista_modelo= json.loads(dados_modelo.content)
linha=1

planilha_excel_motos.write(0,0,'MARCA')
planilha_excel_motos.write(0,1,'CÓDICO')


for modelo in lista_modelo:
    planilha_excel_motos.write(linha,0,modelo.get('name'))
    planilha_excel_motos.write(linha,1,modelo.get('code'))
    linha+=1



planilha_excel_fipe_yamaha= documento_excel.add_worksheet('Fipe - Yamaha')
linha=0
for  modelo in tqdm(lista_modelo):

    for ano in range (2019,2023,1):
        api =f"http://parallelum.com.br/fipe/api/v2/motorcycles/brands/101/models/{modelo.get('code')}/years/{ano}-1"
        dados= requests.get(url=api,headers=headers_info)
        print(dados)

        if dados.status_code ==200:
            moto=json.loads(dados.content)
            planilha_excel_fipe_yamaha.write(linha,0,moto.get('model'))
            planilha_excel_fipe_yamaha.write(linha,1,moto.get('price'))
            planilha_excel_fipe_yamaha.write(linha,2,moto.get('fuel'))
            planilha_excel_fipe_yamaha.write(linha,3,moto.get('modelYear'))
            linha=+1














documento_excel.close()








#print(dados.content)
#print('*' * 174)
#print(f'Código de Resposta: {dados.status_code}')
#print('-' * 174)
#print(f'Cabeçalho da Resposta: {dados.headers}')
#print('-' * 174)
#print(f'Conteúdo da Resposta: {dados.content}')
print('*' * 164)