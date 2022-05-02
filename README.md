# Fipeexcel
projeto dds inspirado bruno games
<h1>FIPEXCEL</h1>

Uma concessionaria de veiculos realiza consultas online a tabela FIPE(tabela de valores de automoveis)mensalmente.O tempo gasto nessa consulta é em media de <b>2 horas</b> diárias .Visando solucionar esse problema criamos um sistema que consulta os dados online e os armazena em uma planilha excel.Utilizando o sistema o <b>tempo gasto na consulta cai para média de 5 minutos</b>



# Requesitos Funcionais do sistema

RF:001 - O Sistema deve permitir a busca de informação a partir de um codigo e ano de fabricação.

RF:002: - O Sistema deve Gravar os dados retornados em um arquivo Excel, os dados armazenados são:Codigo do Veiculo, Marca, Modelo, Ano, Preço, Tipo de Combustível, Mês de Referênisa da Consulta.



# Requisitos não Funcionais 

RNF:001 - O Sistema deve salvar o arquivo em XLSX versão 2007 ou superior

RNF:002 - O Sistema deve ter acesso a internet

RNF:003 - O usuário deve ter instalado em seu computador o Python na versão 3.7 ou superior.


# Regra de negócio

Regra de negocio: 001 - Consulta a tabela FIPE.A consulta a tabla FIPE deve ser feita pelo códico oficial do veículo,todo veículo possui um códico ,gerenciado pela orgaização que cuida de FIPE.Requesito Funcional - 001. 


# Caso de uso

![uc 1 2](https://user-images.githubusercontent.com/82292857/164120338-83203d17-27c9-49e7-a710-50c4ed0953d2.png)



<h3>Enviar tabela por e-mail:</h3>
• O usuário deve acessar a opção de envio da planilhar gerada por email.O usuário insere o e-mail desejado e clica no botão selicionar para buscar o relatório em excel.Ele então seleciona o relatório e clica na opção enviar. O sistema emite um alerta dizendo que o e-mail com o relatório foi enviado com sucesso

<h3>Gerar planilha excel baseada na tabela</h3>
• O usuário acessa o sistema e seleciona uma caixa de seleção o tipo de veículo que ele ta buscando (caminhão ,carro ou moto),deve informar também o ano inicia da busca e o ano final da busca.Após o usuario clica no botão Gerar Planilha e o sistema começa a busca baseado nos parametros informados (Caso de Uso:Consultar FIPE). Após gerar o relatorio o sistema deve emitir um alerta dizendo que a atividade foi comcluida com sucesso .No arquivo excel deve ser exibidos os seguintes dados: Código FIPE do veiculo,nome do veiculo,valor ,ano e tipo de combustivel.

<h3>Consultar FIPE:</h3>
• O sistema deve realizar uma busca atravez de uma api web que tras dados oficiais de tabela fipe que sao os veiculos de acordo com os parametros selecionados.Esses dados irão para a planilha excel






# diagrama de classe




![Untitled (3)](https://user-images.githubusercontent.com/82292857/165190758-08cc0055-a3d8-41c6-849d-9b5711f8aae3.png)





[usuario2.0.pdf](https://github.com/GUILHERME-LOP/fipeexcel/files/8606601/usuario2.0.pdf)











