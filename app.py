from flask import Flask, request, jsonify
from database import db
from models.refeicao import Refeicao

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/daily-diet'

db.init_app(app)

@app.route('/refeicao', methods=['POST'])
def criar_refeicao():
    dados = request.json
    nova_refeicao = Refeicao(nome=dados['nome'], descricao=dados['descricao'],
                             dentro_dieta=dados['dentro_dieta'])
    db.session.add(nova_refeicao)
    db.session.commit()
    return jsonify({'mensagem': 'Refeição criada com sucesso!'})

@app.route('/refeicao/<int:id_refeicao>', methods=['PUT'])
def editar_refeicao(id_refeicao):
    dados = request.json
    refeicao = Refeicao.query.get(id_refeicao)
    
    refeicao.nome = dados['nome']
    refeicao.descricao = dados['descricao']
    refeicao.data_hora = dados['data_hora']
    refeicao.dentro_dieta = dados['dentro_dieta']
    db.session.commit()
    return jsonify({'mensagem': 'Refeição atualizada com sucesso!'})

@app.route('/refeicao/<int:id_refeicao>', methods= ['DELETE'])
def excluir_refeicao(id_refeicao):
    refeicao = Refeicao.query.get(id_refeicao)

    db.session.delete(refeicao)
    db.session.commit()

    return jsonify({"message": "Refeição deletada com sucesso!"})

@app.route('/refeicoes', methods= ['GET'])
def listar_refeicoes():
    refeicoes = Refeicao.query.all()
    resultado = []
    for refeicao in refeicoes:
        resultado.append({
            'id': refeicao.id,
            'nome': refeicao.nome,
            'descricao': refeicao.descricao,
            'data_hora': refeicao.data_hora.strftime('%Y-%m-%d %H:%M:%S'),
            'dentro_dieta': refeicao.dentro_dieta
        })
    return jsonify(resultado)

@app.route('/refeicoes/<int:id_refeicao>', methods= ['GET'])
def obter_refeicao(id_refeicao):
    refeicao = Refeicao.query.get(id_refeicao)
    return jsonify({
        'id': refeicao.id,
        'nome': refeicao.nome,
        'descricao': refeicao.descricao,
        'data_hora': refeicao.data_hora.strftime('%Y-%m-%d %H:%M:%S'),
        'dentro_dieta': refeicao.dentro_dieta
    })
    


if __name__ == '__main__':
    app.run(debug=True)