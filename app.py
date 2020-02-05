from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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

# consulta, altera, e deleta um dev
@app.route('/dev/<int:id>/', methods=['GET', 'PUT','DELETE'])
def desenvolvedor(id):
    if request.method=='GET':
        try:
            response=desenvolvedores[id]
        except IndexError:
            mensagem = 'desenvolvedor de id {} não cadastrado'.format(id)
            response={'status': 'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'erro desconhecido'
            response={'status':'erro desconhecido',' mensagem':mensagem}
        return jsonify(response)
    elif request.method=='PUT':
        dados=json.loads(request.data)
        desenvolvedores[id]=dados
        return jsonify(dados)
    elif request.method=='DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':' dados removidos'})


# insere um novo dev
@app.route('/dev/',methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method=='POST':
        dados=json.loads(request.data)
        posicao = len(dados)
        dados['id']=posicao
        desenvolvedores.append(dados)
        return jsonify({desenvolvedores[posicao]})
    elif request.method=='GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)

