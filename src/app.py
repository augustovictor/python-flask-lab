from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT
from user import User, UserRegister
from item import ItemApi

from security import authenticate, identity

app = Flask(__name__)

api = Api(app)

app.secret_key = '/x12;3117529110^%@!'

jwt = JWT(app, authenticate, identity) # /auth

items = []

api.add_resource(ItemApi, '/items/<int:_id>')
api.add_resource(UserRegister, '/users')

app.run(port=3000, debug=True)