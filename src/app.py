from flask import Flask, jsonify, request
import uuid

# app de personas
# Agregar (POST)
# Consultar (GET)
# Actualizar (PUT)
# Borrar (DELETE)
"""
    id, name, lastname
    {
        "id":1,
        "name":"Deimian"
        "lastname":"Vásquez"
    }
"""
myuuid = uuid.uuid4()

# simulación de database
people = [
    {
        "id":"1",
        "name":"Deimian",
        "lastname":"Vásquez"
    },
    {
        "id":"2",
        "name":"Martín",
        "lastname":"Coimbra"
    }
]


# hacer una instancia de flask (Crear un objeto flask)
app = Flask(__name__)

# ruta health_check
@app.route("/health_check", methods=["GET"])
def health_check():
    return jsonify("ok")


# consultar todas las personas
@app.route("/people", methods=["GET"]) # GET default
def get_all_people():
    response = jsonify(people)
    response.status_code = 200
    return response


# consultar la persona por identificador
@app.route("/people/<string:person_id>", methods=["GET"])
def get_one_people(person_id):
    result = list(filter(lambda item: item["id"] == person_id, people))  
    if result:
        return jsonify(result[0]), 200
    else:
        return jsonify({"message":"User not found"}), 404



# agregar una persona -- body (application/json)
@app.route("/people", methods=["POST"])
def add_new_person():
    body = request.json

    if body.get("name") is None :
        return jsonify({"message":"required name parameter"}), 400
    if body.get("lastname") is None:
       return jsonify({"message":"required lastname parameter"}), 400

    # body.update({"id":len(people)+1})
    body.update({"id":str(myuuid)})
    
    people.append(body)

    #diccionarios get
    return jsonify(body), 201



# editar persona
@app.route("/people/<string:person_id>", methods=["PUT"])
def update_person(person_id):
    body = request.json

    if body.get("name") is None :
        return jsonify({"message":"required name parameter"}), 400
    if body.get("lastname") is None:
       return jsonify({"message":"required lastname parameter"}), 400

    # buscar persona en el arreglo
    new_person = list(filter(lambda item: item["id"] == person_id, people))
    new_person = new_person[0]
    new_person["name"] = body.get("name")
    new_person["lastname"] = body["lastname"]

    return jsonify(new_person), 201


# eliminar una persona
@app.route("/people/<string:person_id>", methods=["DELETE"])
def delete_person(person_id = None):
    if person_id is not None:
        for item in people:
            if item["id"] == person_id:
                people.remove(item)
                return jsonify([]), 204
        return jsonify({"message":"user not found"}), 404
    return jsonify({"message":"user not found"}), 404
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3001", debug=True)