# fipeexcel
projeto dds inspirado bruno games
<h1>FIPEXCEL</h1>

Uma concessionaria de veiculos realiza consultas online a tabela FIPE(tabela de valores de automoveis)mensalmente.O tempo gasto nessa consulta é em media de <b>2 horas</b> diárias .Visando solucionar esse problema criamos um sistema que consulta os dados online e os armazena em uma planilha excel.Utilizando o sistema o <b>tempo gasto na consulta cai para média de 5 minutos</b>



# Requesitos Funcionais do sistema

RF:001 - O Sistema deve permitir a busca de informação a partir de um codigo e ano de fabricação.

RF:002: - O Sistema deve Gravar os dados retornados em um arquivo Excel, os dados armazenados são:Codigo do Veiculo, Marca, Modelo, Ano, Preço, Tipo de Combustível, Mês de Referênisa da Consulta.



# Requisitos Não Funcionais 

RNF:001 - O Sistema deve salvar o arquivo em XLSX versão 2007 ou superior

RNF:002 - O Sistema deve ter acesso a internet

RNF:003 - O usuário deve ter instalado em seu computador o Python na versão 3.7 ou superior.


# Regra de negocio

Regra de negocio: 001 - Consulta a tabela FIPE.A consulta a tabla FIPE deve ser feita pelo códico oficial do veículo,todo veículo possui um códico ,gerenciado pela orgaização que cuida de FIPE.Requesito Funcional - 001. 


# Caso de uso

![uc 1 2](https://user-images.githubusercontent.com/82292857/164120338-83203d17-27c9-49e7-a710-50c4ed0953d2.png)



# Gerar execel com caso de uso:
Ele vai coletar os dados (preço,ano,códico fipe,mês de referencia ) da tabela e salvar diretamente no excel

# Enviar a tabela por email:
Ele vai colar a tabela ja salva e enviar atrasvez do e-mail da empresa para o cliente

# Consultar fipe:
O sistema ira busca diretamente na api da tabela FIPE diretamente do site do GOV.BR  























,
