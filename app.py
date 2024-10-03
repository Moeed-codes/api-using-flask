from flask import Flask, request
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)


data = [
    {'id':1,'name':'user 1','age':49},
    {'id':2,'name':'user 1','age':50} 
]

def find_person(person_id):
    for person in data:
        if person['id'] == person_id:
            return person
        
    return None

        


# GET, POST, PUT, PATCH,DELETE

class PeopleResource(Resource):
    def get(self):
        return data
    def post(self):
        new_person = {
            "id":len(data)+1,
            "name" : "User 3",
            "age" : 4
        }
        data.append(new_person)
        return new_person, 201
class PersonResource(Resource):
        def get(self, person_id):
            person = find_person(person_id)
            if person:
                return person
            return {"message":"person not found"}, 404
        
        def put(self, person_id):
            person = find_person(person_id)
            if person:
                person['name'] = request.json['name']
                person['age'] = request.json['age']
                return person
            return {"message":"person not found"}, 404
        def delete(self, person_id):
            global data
            data = [person for person in data if person['id'] != person_id]

            return {"message":"person deleted successfully"}, 200
    
api.add_resource(PeopleResource,'/people')
api.add_resource(PersonResource,'/person?<int:person_id>')

if __name__ == '__main__':
    app.run(debug=True)