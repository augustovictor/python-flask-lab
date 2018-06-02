from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'S1',
        'items': [
            { 'name': 'I1' , 'price': 14.22 },
            { 'name': 'I2' , 'price': 15.22 },
            { 'name': 'I3' , 'price': 16.22 },
            { 'name': 'I4' , 'price': 17.22 }
        ]
    }
]

@app.route('/')
def home():
    return 'Hello world'

# STORES
@app.route('/stores')
def getStores():
    return jsonify({ 'stores': stores })

@app.route('/stores', methods=['POST'])
def createStore():
    requestData = request.get_json()
    print(requestData)
    newStore = { 'name': requestData['name'], 'items': [] }
    print(newStore)
    stores.append(newStore)
    return jsonify(newStore)

@app.route('/stores/<string:name>')
def getStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    return jsonify({ 'message': 'no store was found for given name: {}'.format(name)})

# ITEMS
@app.route('/stores/<string:name>/items')
def getItemsFromStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    
    return jsonify({ 'message': 'No store with given name' })

@app.route('/stores/<string:name>/items/<string:item_name>')
def getItemFromStore(name, item_name):
    for store in stores:
        if store['name'] == name:
            for item in store['items']:
                if item['name'] == item_name:
                    return jsonify(item)
    
    return jsonify({ 'message': 'No item was found for given name'})

@app.route('/stores/<string:name>/items', methods=['POST'])
def createItem(name):
    data = request.get_json()
    for store in stores:
        if store['name'] == name:
            store['items'].append(data)
            return jsonify(store)
    
    return jsonify({ 'message': 'No store was found for given name' })

app.run(port=3000, debug=True)