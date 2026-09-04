from flask import Flask, request, redirect
import mysql.connector
from config import DB_CONFIG


app = Flask(__name__)




def conectar():
   return mysql.connector.connect(**DB_CONFIG)




# --- PÁGINA INICIAL ---
@app.route("/")
def index():
   return """
   <h1>Sistema Biblioteca Escolar</h1>
   <p>Projeto iniciado com Python, Flask e MySQL.</p>
   <ul>
       <li><a href="/alunos">Ver alunos cadastrados</a></li>
       <li><a href="/alunos/novo">Cadastrar novo aluno</a></li>
       <li><a href="/professores">Ver professores cadastrados</a></li>
       <li><a href="/bibliotecarios">Ver bibliotecários cadastrados</a></li>
       <li><a href="/livros">Ver livros cadastrados</a></li>
   </ul>
   """




# --- LISTAR ALUNOS ---
@app.route("/alunos")
def listar_alunos():
   try:
       conexao = conectar()
       cursor = conexao.cursor(dictionary=True)


       cursor.execute("SELECT * FROM aluno")
       alunos = cursor.fetchall()


       cursor.close()
       conexao.close()


       html = """
       <h1>Alunos Cadastrados</h1>
       <a href="/">Voltar</a>
       <br><br>


       <table border="1" cellpadding="8">
           <tr>
               <th>ID</th>
               <th>Nome</th>
               <th>Série</th>
               <th>Turma</th>
               <th>Telefone</th>
           </tr>
       """


       for aluno in alunos:
           html += f"""
           <tr>
               <td>{aluno['id_aluno']}</td>
               <td>{aluno['nome']}</td>
               <td>{aluno['serie']}</td>
               <td>{aluno['turma']}</td>
               <td>{aluno['telefone']}</td>
           </tr>
           """


       html += "</table>"
       return html


   except Exception as erro:
       return f"Erro ao listar alunos: {erro}"

@app.route("/alunos/novo")
def formulario_aluno():
    return """
<h1>Cadastrar aluno</h1>

<form method="POST" action="/alunos/cadastrar">
 <label>Nome: </label></br>
 <input type="text" name="nome" required></br>

 <label>Série:</label></br>
 <input type="text" name="serie" required></br>

 <label>Turma:</label></br>
 <input type="text" name="turma" required></br>

 <label>Telefone:</label></br>
 <input type="text" name="telefone" required></br>

 <button type="submit">Salvar</button>
</form>
<br>
<a href="/alunos"> Voltar para lista</a>
"""

@app.route("/alunos/cadastrar", methods=["POST"])
def cadastrar_aluno():
    nome = request.form["nome"]
    serie = request.form["serie"]
    turma = request.form["turma"]
    telefone = request.form["telefone"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
 INSERT INTO aluno(nome, serie, turma, telefone)
 values (%s,%s,%s,%s)
 """

    valores = (nome, serie, turma, telefone)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/alunos")

# --- LISTAR PROFESSORES ---
@app.route("/professores")
def listar_professores():
   try:
       conexao = conectar()
       cursor = conexao.cursor(dictionary=True)


       cursor.execute("SELECT * FROM professor")
       professores = cursor.fetchall()


       cursor.close()
       conexao.close()


       html = """
       <h1>Professores Cadastrados</h1>
       <a href="/">Voltar</a>
       <br><br>


       <table border="1" cellpadding="8">
           <tr>
               <th>ID</th>
               <th>Nome</th>
               <th>Telefone</th>
               <th>E-mail</th>
           </tr>
       """


       for prof in professores:
           html += f"""
           <tr>
               <td>{prof['id_professor']}</td>
               <td>{prof['nome']}</td>
               <td>{prof['telefone']}</td>
               <td>{prof['email']}</td>
           </tr>
           """


       html += "</table>"
       return html


   except Exception as erro:
       return f"Erro ao listar professores: {erro}"




# --- LISTAR BIBLIOTECÁRIOS ---
@app.route("/bibliotecarios")
def listar_bibliotecarios():
   try:
       conexao = conectar()
       cursor = conexao.cursor(dictionary=True)


       cursor.execute("SELECT * FROM bibliotecario")
       bibliotecarios = cursor.fetchall()


       cursor.close()
       conexao.close()


       html = """
       <h1>Bibliotecários Cadastrados</h1>
       <a href="/">Voltar</a>
       <br><br>


       <table border="1" cellpadding="8">
           <tr>
               <th>ID</th>
               <th>Nome</th>
               <th>E-mail</th>
           </tr>
       """


       for biblio in bibliotecarios:
           html += f"""
           <tr>
               <td>{biblio['id_bibliotecario']}</td>
               <td>{biblio['nome']}</td>
               <td>{biblio['email']}</td>
           </tr>
           """


       html += "</table>"
       return html


   except Exception as erro:
       return f"Erro ao listar bibliotecários: {erro}"




# --- LISTAR LIVROS ---
@app.route("/livros")
def listar_livros():
   try:
       conexao = conectar()
       cursor = conexao.cursor(dictionary=True)


       cursor.execute("SELECT * FROM livro")
       livros = cursor.fetchall()


       cursor.close()
       conexao.close()


       html = """
       <h1>Livros Cadastrados</h1>
       <a href="/">Voltar</a>
       <br><br>


       <table border="1" cellpadding="8">
           <tr>
               <th>ID</th>
               <th>Título</th>
               <th>Autor</th>
               <th>Categoria</th>
               <th>Status</th>
           </tr>
       """


       for livro in livros:
           html += f"""
           <tr>
               <td>{livro['id_livro']}</td>
               <td>{livro['titulo']}</td>
               <td>{livro['autor']}</td>
               <td>{livro['categoria']}</td>
               <td>{livro['status']}</td>
           </tr>
           """


       html += "</table>"
       return html


   except Exception as erro:
       return f"Erro ao listar livros: {erro}"




if __name__ == "__main__":
   app.run(debug=True)
  
