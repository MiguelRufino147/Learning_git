from flask import Flask ,jsonify,make_response,request
from bd import listas
app=Flask(__name__)




#GET
@app.route('/get',methods=['GET'])
def get():
    return make_response(
        jsonify(listas))

#POST
@app.route('/get',methods=['POST'])
def post():
    lista=request.json
    listas.append(lista)
    return lista


app.run(debug=True)