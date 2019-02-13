import requests
import json

class GraphFacebook():

    def requisicao(self, pesquisa, quantidade, token):
        preposto = 'https://graph.facebook.com/search?q={}&type=place&limit={}&access_token={}'

        url = preposto.format(pesquisa, quantidade, token)
        user_agent = {'User-agent': 'Mozilla/5.0'}
        conteudo = requests.get(url=url, headers=user_agent)
        return conteudo.text

    def leituraJSON(self, pessoa, quantidade):
        myToken ="xxxxxxxxxxxxxxxxxxxxxxxxx"
        dados = GraphFacebook().requisicao(pesquisa=pessoa, quantidade=quantidade, token=myToken)
        print(dados)
        json_data = json.loads(dados)
        for p in json_data['data']:
            usuario_faceook = p['name'], ' ' + p['id']
            print('Facebook : %s' %str(usuario_faceook).replace("('", '').replace("')", '   '))


pessoa = "jeferson fernandes"
quantidade = 4

GraphFacebook().leituraJSON(pessoa, quantidade)
