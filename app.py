from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
from flask_cors import CORS
from schema import schema

app = Flask(__name__)
CORS(app, resources={r"/graphql": {"origins": "*"}})  # Configuración específica de CORS

# Middleware para registrar el payload de los requests
@app.before_request
def log_request_info():
    if request.method == 'POST':
        print(f"Headers: {request.headers}")
        print(f"Body: {request.get_data()}")

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

# Endpoint de health check
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
