from flask import Blueprint,render_template, url_for, redirect, request
from loginapp.extensions import mongo 
from passlib.hash import sha256_crypt

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import jwt
from jwt_rsa.rsa import generate_rsa


main = Blueprint('main',__name__)
"""
    @param: file pem 
    @output: private-key, public-key
"""
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(
        f.read(), backend=default_backend()
    )
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(), None, backend=default_backend()
        )

@main.route('/')
def index():
    return "main"

@main.route('/register', methods=['POST'])  
def register():
    """
    @param 
    """

    user_collection = mongo.db.loginapp

    data = request.get_json('')

    pass_hash = sha256_crypt.hash(data['password'])

    data['password'] = pass_hash

    # checkpass    
    # print(sha256_crypt.verify("123456", pass_hash))

    encoded = jwt.encode(data, private_key, algorithm="RS256")

    return {
        "token": encoded.decode()
    }

@main.route('/getinfo', methods=['POST','GET'])
def getinfo():

    [scheme, token] = (request.headers.get('Authorization')).split()

    decoded = jwt.decode(token, public_key, algorithms=["RS256"])
    
    return {
        "data": decoded
    }