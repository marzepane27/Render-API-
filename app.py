from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config.from_object('config.Config')  


db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Hello, Render API!"

@app.route('/api/v1/productentitiestool-ui-admin/partner/getAll', methods=['GET'])
def get_all_partners():
    partners = [{"id": 1, "name": "Partner 1"}, {"id": 2, "name": "Partner 2"}]
    return jsonify(partners)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    port = os.getenv('PORT', 10000)  
    app.run(host='0.0.0.0', port=port, debug=False)  
