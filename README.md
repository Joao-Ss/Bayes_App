
# 📈 Projeto com Teorema de Bayes

Aplicação web em Python (Flask) que calcula probabilidades usando o Teorema de Bayes e distribuição binomial para provas de múltipla escolha. Permite informar a chance de acerto, número de questões e visualizar as probabilidades diretamente no navegador.

## 📌 Descrição

Sistema de Cálculo de Probabilidades usando o Teorema de Bayes aplicado a provas de múltipla escolha. Este projeto consiste em uma aplicação web desenvolvida com Python (Flask) que permite ao usuário:

- Definir a chance de um aluno saber a resposta de uma questão
- Informar o número total de questões da prova
- Definir quantas questões deseja acertar
- Calcular a chance de acertar uma questão qualquer e a probabilidade de acertar exatamente um número específico de questões

Tudo isso de forma interativa, via navegador, com resultados exibidos diretamente na tela.

### 🛠️ Tecnologias:

- Python
- Flask
- HTML5
- CSS3

### 📊 Conceitos aplicados:

- Teorema de Bayes
- Distribuição Binomial
- Servidor web local com Flask

## 💻 Explicando o código

### 🔧 1. Importações

Arquivo app.py
```python
from flask import Flask, render_template, request
from bayes import calcular_probabilidade
```
Aqui o código importa:

- **Flask**, o framework que cria o servidor web;
- **render_template**, que carrega arquivos HTML;
- **request**, que lê dados enviados pelo formulário;
- E a função **calcular_probabilidade**, que está em outro arquivo (bayes.py) e faz o cálculo do Teorema de Bayes.

### 🚀 2. Criação da aplicação Flask

```python
app = Flask(__name__)
```
Essa instância é usada para configurar as rotas e iniciar o servidor.

### 🌐 3. Definição da rota principal

```python
@app.route("/", methods=["GET", "POST"])
def index():
    ...
```
Define o que acontece quando o usuário acessa o site pela URL principal ("/"). Essa função:
Exibe a página HTML se for um acesso comum (GET);
Ou processa os dados enviados pelo formulário (POST).

### 📥 4. Recebimento e processamento do formulário

```python
if request.method == "POST":
    prob_a = float(request.form["prob_a"])
    prob_b = float(request.form["prob_b"])
    prob_b_dado_a = float(request.form["prob_b_dado_a"])
    resultado = calcular_probabilidade(prob_a, prob_b, prob_b_dado_a)
```
Quando o usuário envia o formulário com os valores de probabilidade:
- O Flask pega os dados do formulário (request.form["..."]);
- Converte os dados para número decimal (float);
- E calcula a probabilidade de Bayes usando a função importada.

### 🖥️ 5. Renderização do HTML com o resultado

```python
return render_template("index.html", resultado=resultado)
```
Exibe a página HTML (index.html), passando a variável resultado para ser mostrada na interface, caso ela exista.

### 🧪 6. Execução do app

```python
if __name__ == "__main__":
    app.run(debug=True)
```
Garante que o servidor Flask seja executado apenas se o arquivo for rodado diretamente (e não importado por outro código).
O modo debug=True reinicia automaticamente o app ao fazer mudanças no código e mostra erros no navegador.



## 💡 Como rodar o projeto:

1. Abra o terminal ou prompt de comando.

2. Navegue até a pasta onde você extraiu o projeto:
```bash
    Exemplo:
    cd caminho/para/bayes_app
```
3. (Opcional, mas recomendado) Crie um ambiente virtual:
```bash
No Windows:
    python -m venv venv
    venv\Scripts\activate
```
4. Se for a primeira vez iniciando, rode o comando:
```bash
    pip install -r requirements.txt
```
5. Rode a aplicação:
```bash
    python app.py
```

6. Abra o navegador e acesse:
    http://127.0.0.1:5000/


## 📁 Estrutura de pastas:

- app.py → Código Python principal (Flask)
- requirements.txt → Lista de dependências
- templates/index.html → Página web (HTML)
- static/style.css → Estilo da página (CSS)
- README.md