from flask import Flask, json,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
import PySimpleGUI as sg

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost/userdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

""" Class with the attributes for firstname, lastname, city, street and birthdate
"""

class UserData(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    firstname=db.Column(db.String(40),nullable=False)
    lastname=db.Column(db.String(40),nullable=False)
    city=db.Column(db.String(40),nullable=False)
    street=db.Column(db.String(40),nullable=False)
    bdate=db.Column(db.String(10),nullable=False)

    def __repr__(self):
        return self.firstname

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class UserDataSchema(Schema):
    id=fields.Integer()
    firstname=fields.String()
    lastname=fields.String()
    city=fields.String()
    street=fields.String()
    bdate=fields.String()


@app.route('/userdata', methods=['GET'])
def get_all_userdata():
    """gets all userdata from the db
    """
    userdata=UserData.get_all()

    serializer=UserDataSchema(many=True)

    data=serializer.dump(userdata)

    return jsonify(
        data
    )



@app.route('/userdata', methods=['POST'])
def create_userdata():
    """creates a new dataset and commits it to the db
    """
    data=request.get_json()

    new_userdata=UserData(
        firstname=data.get('firstname'),
        lastname=data.get('lastname'),
        city=data.get('city'),
        street=data.get('street'),
        bdate=data.get('bdate')

    )

    new_userdata.save()

    serializer=UserDataSchema()

    data=serializer.dump(new_userdata)

    return jsonify(
        data
    ),201

@app.route('/userdata/<int:id>', methods=['GET'])
def get_userdata(id):
    """gets userdata by <id>
    """
    userdata=UserData.get_by_id(id)

    serializer=UserDataSchema()

    data=serializer.dump(userdata)

    return jsonify(
        data
    ),200

    

@app.route('/userdata/<int:id>', methods=['PUT'])
def update_userdata(id):
    """updates userdata by <id>
    """
    

    userdata_to_update=UserData.get_by_id(id)
    data=request.get_json()

    

    userdata_to_update.firstname = data.get('firstname')
    userdata_to_update.lastname =  data.get('lastname')
    userdata_to_update.city = data.get('city')
    userdata_to_update.street= data.get('street')
    userdata_to_update.bdate = data.get('bdate')

    db.session.commit()

    serializer=UserDataSchema()

    userdata_update=serializer.dump(userdata_to_update)

    return jsonify(userdata_update),200


@app.route('/userdata/<int:id>', methods=['DELETE'])
def delete_userdata(id):
    """ deletes userdata by <id>
    """
    userdata_to_delete=UserData.get_by_id(id)

    userdata_to_delete.delete()

    return jsonify({"message":"Deleted"}),204


@app.errorhandler(404)
def not_found(error):
    return jsonify({"message":"Resource not found"}),404

@app.errorhandler(500)
def internal_server(error):
    return jsonify({"message":"There is a problem"}),500

if __name__== '__main__':
    app.run(debug=True)