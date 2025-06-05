
from flask import Flask, render_template, request
from math import comb

app = Flask(__name__)

def teorema_de_bayes(p_a, p_b_dado_a, p_b_dado_nao_a):
    p_nao_a = 1 - p_a
    numerador = p_b_dado_a * p_a
    denominador = (p_b_dado_a * p_a) + (p_b_dado_nao_a * p_nao_a)
    p_a_dado_b = numerador / denominador
    return p_a_dado_b

def probabilidade_acertar(p_sabe, alternativas):
    p_nao_sabe = 1 - p_sabe
    p_chute = 1 / alternativas
    return p_sabe + (p_nao_sabe * p_chute)

def probabilidade_exatamente_k(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        p_sabe = float(request.form['p_sabe'])
        num_questoes = int(request.form['num_questoes'])
        num_acertos = int(request.form['num_acertos'])
        alternativas = 5
        
        p_acertar_questao = probabilidade_acertar(p_sabe, alternativas)
        p_exatamente_k = probabilidade_exatamente_k(num_questoes, num_acertos, p_acertar_questao)
        
        resultado = {
            'p_acertar_questao': round(p_acertar_questao, 4),
            'p_exatamente_k': round(p_exatamente_k, 4),
        }

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
