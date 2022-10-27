from flask import  Flask,make_response,jsonify,request
import mysql.connector




app=Flask(__name__)
conexao=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Costa147#',
    database='filmes_novos'
)


lista=[list()]




#GET
@app.route('/' ,methods=['GET'])
def get():
    cursor=conexao.cursor()
    cursor.execute('SELECT * FROM filmes')
    meusfilmes=cursor.fetchall()
    for filmes in meusfilmes:
        lista.append(filmes)
    return make_response(jsonify('Filmes',lista))

#POST
@app.route('/' ,methods=['POST'])
def create():
    filme=request.json
    cursor = conexao.cursor()
    sql=f"INSERT INTO filmes (nome,ano)values ('{filme['nome']}','{filme['ano']}')"
    cursor.execute(sql)
    conexao.commit()
    return make_response(jsonify('Cadastrado'))





app.run(debug=True)

