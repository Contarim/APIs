import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

nome_salvo = None  # Variável global para armazenar o nome

# Rota GET para mostrar o nome salvo
@app.route('/nome', methods=['GET'])
def mostrar_nome():
    if nome_salvo:
        return jsonify({'nome': nome_salvo})
    else:
        return jsonify({'mensagem': 'Nenhum nome foi enviado ainda.'}), 404

# Rota POST para receber e salvar o nome
@app.route('/nome', methods=['POST'])
def salvar_nome():
    global nome_salvo
    dados = request.json
    nome_salvo = dados.get('nome')
    return jsonify({'mensagem': f'Nome {nome_salvo} salvo com sucesso!'})

produto = None  # Variável global para armazenar o produto

@app.route('/teste', methods=['GET'])
def teste_get():
    if produto is None:
        return jsonify({'mensagem': f'Login negado! Senha incorreta ou inválida.'}), 404
    else:
        return jsonify({'mensagem': f'login feito com sucesso. Bem vindo {produto}'})

# Rota de teste para receber um produto
@app.route('/teste', methods=['POST'])
def teste():
    global produto
    dados = request.json
    produto = dados.get('produto')
    return jsonify({'mensagem': f'O produto {produto} foi cadastrado com sucesso!'})

@app.route('/preco-bitcoin', methods=['GET'])
def preco_bitcoin():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin,ethereum,dogecoin',
        'vs_currencies': 'brl'
    }
    resposta = requests.get(url, params=params)
    if resposta.status_code == 200:
        dados = resposta.json()
        return jsonify({
            'bitcoin_brl': dados['bitcoin']['brl'],
            'ethereum': dados['ethereum']['brl'],
            'dogecoin': dados['dogecoin']['brl']
            })
    else:
        return jsonify({'erro': 'Não foi possível obter o preço.'}), 500

# @app.route('/preco-cripto', methods=['GET'])
# def preco_cripto():
#     url = 'https://api.coingecko.com/api/v3/simple/price'
#     params = {
#         'ids': 'bitcoin,ethereum',
#         'vs_currencies': 'brl'
#     }
#     resposta = requests.get(url, params=params)
#     if resposta.status_code == 200:
#         dados = resposta.json()
#         return jsonify({
#             'bitcoin_brl': dados['bitcoin']['brl'],
#             'ethereum_brl': dados['ethereum']['brl']
#         })
#     else:
#         return jsonify({'erro': 'Não foi possível obter os preços.'}), 500

if __name__ == '__main__':
    app.run(debug=True)