from crypt import methods
import PySimpleGUI as sg
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema,fields
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost/data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

# id
# firstname
# lastname
# city
# street
# bdate

class Data(db.Model):
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

class CitySchema(Schema):
    id=fields.Integer()
    name=fields.String()
    street=fields.String()


@app.route('/data', methods=['GET'])
def get_all_data():
    data=Data.get_all()

    serializer=CitySchema()

    data=serializer.dump(data)

@app.route('/data', methods=['POST'])
def create_data():
    pass

@app.route('/data/<int:id>', methods=['GET'])
def get_data(id):
    pass

@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    pass

@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    pass

if __name__== '__main__':
    app.run(debug=True)