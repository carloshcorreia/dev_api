from flask import Flask, request
from  flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)
desenvolvedores = [
    {'id':0,
     'nome':'carlos',
     'habilidades':['pytohn','flask']},
    {'id':1,
     'nome':'henrique',
     'habilidades':['python','django']},
    {'id':2,
     'nome':'peixoto',
     'habilidades':['javascript','json']},
    {'id':3,
     'nome':'correia',
     'habilidades':['python','rest api']}
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response=desenvolvedores[id]
        except IndexError:
            mensagem = 'desenvolvedor de id {} não cadastrado'.format(id)
            response={'status': 'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'erro desconhecido'
            response={'status':'erro desconhecido',' mensagem':mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso','mensagem':'arquivo excluido'}

class Lista_desenvolvedor(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(dados)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor,'/dev/<int:id>/')
api.add_resource(Lista_desenvolvedor,'/dev/')


if __name__ == '__main__':
    app.run(debug=True)