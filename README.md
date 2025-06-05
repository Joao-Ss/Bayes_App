
# Projeto com Teorema de Bayes

## 📌 Descrição

Sistema de Cálculo de Probabilidades usando o Teorema de Bayes aplicado a provas de múltipla escolha. Este projeto consiste em uma aplicação web desenvolvida com Python (Flask) que permite ao usuário:

- Definir a chance de um aluno saber a resposta de uma questão
- Informar o número total de questões da prova
- Definir quantas questões deseja acertar
- Calcular a chance de acertar uma questão qualquer e a probabilidade de acertar exatamente um número específico de questões

Tudo isso de forma interativa, via navegador, com resultados exibidos diretamente na tela.

#### 🛠️ Tecnologias:

- Python
- Flask
- HTML5
- CSS3

#### 📊 Conceitos aplicados:

- Teorema de Bayes
- Distribuição Binomial
- Servidor web local com Flask

## Como rodar o projeto:

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
    python app.py

6. Abra o navegador e acesse:
    http://127.0.0.1:5000/


## 📁 Estrutura de pastas:

- app.py → Código Python principal (Flask)
- requirements.txt → Lista de dependências
- templates/index.html → Página web (HTML)
- static/style.css → Estilo da página (CSS)
- README.md