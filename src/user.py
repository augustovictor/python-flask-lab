import sqlite3
from flask_restful import Resource, Api, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        select_query = 'SELECT * FROM users WHERE username = ?'
        result = cursor.execute(select_query, (username,))
        row = result.fetchone()
        
        user = cls(*row) if row else None
        
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = 'SELECT * FROM users WHERE id = ?'
        result = cursor.execute(select_query, (_id,))
        row = result.fetchone()

        user = cls(*row) if row else None

        connection.close()
        return user

    @classmethod
    def signup(cls, username, password):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        create_user_query = 'INSERT INTO users VALUES (NULL, ?, ?)'
        # user = cls(None, username, password)
        result = cursor.execute(create_user_query, (username, password))
        # user = result.fetchone()
        connection.commit()
        connection.close()
        return True

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be left blank!')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank!')
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if User.find_by_username(data['username']):
            return { 'message': 'Username already taken!'}, 400

        # user = User(1, data['username'], data['password'])
        # createdUser = User.signup(data['username'], data['password'])
        # return createdUser, 201 if createdUser else None, 400

        User.signup(data['username'], data['password'])

        return { 'message': 'User created successfully!' }, 201