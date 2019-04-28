from flask import Flask
from flask_restful import Api, Resource, reqparse
import hashlib

app = Flask(__name__)
api = Api(app)

users = [
        {
            'id': '111',
            'username': 'guest',
            'password': 'qwertyuiop',
            'email': 'd.chanana777@gmail.com',
            'gallons': '5',
            'threshold': '10',
            'numberOfPeople': 4
        }
]

def encrypt_string(hash_string):
        sha_signature = \
                hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature

class User(Resource):
    
    def get(self, userid):
        for user in users:
            if(userid == user['id']):
                    return user, 200
            elif(userid == 'all'):
                    return users, 200
        return 'User not found', 404
    
    def post(self, userid):
        parser = reqparse.RequestParser()
        parser.add_argument('password')
        parser.add_argument('email')
        parser.add_argument('gallons')
        parser.add_argument('threshold')
        parser.add_argument('numberOfPeople')
        args = parser.parse_args()

        for user in users:
            if(userid == user['username']):
                return 'Username is taken', 400

        user = {
                'id': (args['password'] + userid),
                'username': userid,
                'password': args['password'],
                'email': args['email'],
                'gallons': args['gallons'],
                'threshold': args['threshold'],
                'numberOfPeople': args['numberOfPeople']
        }
        users.append(user)
        return user, 201

    def put(self, userid):
        parser = reqparse.RequestParser()
        parser.add_argument('password')
        parser.add_argument('email')
        parser.add_argument('gallons')
        parser.add_argument('threshold')
        args = parser.parse_args()
        user = {
                'id': (args['password'] + userid),
                'username': userid,
                'password': args['password'],
                'email': args['email'],
                'gallons': args['gallons'],
                'threshold': args['threshold']
        }
        for i in range(len(users)):
            if(userid == users[i]['username']):
                users[i] = user
                return user, 201

        users.append(user)
        return user, 201

 
api.add_resource(User, '/user/<string:userid>')
app.run(debug=True)
