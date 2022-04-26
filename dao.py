from cunsulta_api import API



class Marca:

    def __init__(self,codigo,marca) :
        self.codigo = codigo
        self.nome_marca = marca

    def busca_marca(self,tipo_veiculo):
        api_data=API(tipo_veiculo)
        lista_marca=[]
        for marca_recebida in api_data.busca_marca_por_tipo():
            marca_objeto=Marca(marca_recebida.get('code'),marca_recebida.get('name'))
            lista_marca.append(marca_objeto)

        return lista_marca
        