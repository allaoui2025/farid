from flask import Flask, jsonify

app = Flask(__name__)

# Liste des utilisateurs
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route('/')
def home():
    return jsonify({"message": "Bienvenue sur mon API !"})

@app.route('/users')
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    # Changez le host de 127.0.0.1 à 0.0.0.0 pour rendre l'API accessible depuis l'extérieur de la conteneur
    app.run(host="0.0.0.0", port=5000, debug=True)
