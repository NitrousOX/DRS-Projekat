from flask import render_template, Blueprint, jsonify
from app.services.user_service import get_data

api_bp = Blueprint('api', __name__)

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

@api_bp.route('/get_data', methods=['GET'])
def get_data_route():
    data = get_data()  # Calls the service to get data
    return jsonify(data)
