from flask import Flask, jsonify, request

app = Flask(__name__)

Contacts = [
    {
        'id':1,
        'Name':'Sanchita',
        'Contact':'1234567890',
        'status':False,
        'added':'Pre Added'
    },
    {
        'id':2,
        'Name':'Notan',
        'Contact':'0987654321',
        'status':False,
        'added':'Pre Added'
    }
]

@app.route("/add-contact", methods=["POST"])

def addCont():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide the Contact Data'
        })
    contact = {
        'id':Contacts[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'status':False,
        'added':request.json['added']
    }
    Contacts.append(contact)
    return jsonify({
            'status':'success',
            'message':'Contact added Successfuly'
        })

@app.route("/get-data", methods=["GET"])

def getCont():
    return jsonify({
        'data':Contacts
    })

if(__name__ == "__main__"):
    app.run(debug=True)

#See the data by pasting this link in the respective browser http://127.0.0.1:5000/get-data