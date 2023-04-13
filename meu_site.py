from flask import Flask

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return "homepage.html"

@app.route("/contatos")
def contatos():
    return "contatos.html"

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return "usuarios.html"

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku

