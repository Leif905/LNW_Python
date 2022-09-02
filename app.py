from flask import Flask, json,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost/fuckit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

# id
# firstname
# lastname
# city
# street
# bdate

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
    userdata=UserData.get_all()

    serializer=UserDataSchema()

    data=serializer.dump(userdata)

    return jsonify(
        
    )



@app.route('/userdata', methods=['POST'])
def create_userdata():
    pass

@app.route('/userdata/<int:id>', methods=['GET'])
def get_userdata(id):
    pass

@app.route('/userdata/<int:id>', methods=['PUT'])
def update_userdata(id):
    pass

@app.route('/userdata/<int:id>', methods=['DELETE'])
def delete_userdata(id):
    pass

if __name__== '__main__':
    app.run(debug=True)