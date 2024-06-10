from flask import Flask,jsonify
from db import Session,engine
from models import Usuario

app = Flask(__name__)



@app.get("/")
def hello_world():
    return jsonify({"res":"true","message":"todo ok!"})



@app.get("/users")
def getUsers():
    return jsonify({"Users":"Todos los usuarios estan aqui"})




@app.get("/powerBI")
def getPower():
    return jsonify({"datos":"Datos de Power BI"})