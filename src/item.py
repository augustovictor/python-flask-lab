import sqlite3
from flask_jwt import jwt_required
from flask_restful import Resource, Api, reqparse

class Item:
    def __init__(self, _id, name, price):
        self.id = _id
        self.name = name
        self.price = price
    
    @classmethod
    def findById(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM items WHERE id = ?'
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        item = cls(*row) if row else None
        connection.close()
        return item

class ItemApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be left blank!')

    # @jwt_required()
    def get(self, _id):
        result = Item.findById(_id)
        item = { '_id': result.id, 'name': result.name, 'price': result.price } if result else None
        if item: return item, 200
        else: return { 'message': 'Item not found' }, 404

    def post(self, name):
        if next(filter(lambda i: i['name'] == name, items), None) is not None:
            return { 'message': 'Item with given name already exists'}, 400

        data = ItemApi.parser.parse_args()
        item  = { 'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda i: i['name'] != name, items))
        return { 'message': 'Item has been removed' }

    def put(self, name):
        data = ItemApi.parser.parse_args()
        item = next(filter(lambda i: i['name'] == name, items), None)

        if item is None:
            item = { 'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
