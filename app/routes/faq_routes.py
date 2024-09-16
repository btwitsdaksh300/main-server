from flask import Blueprint, jsonify, request
from app.models.faq_model import FAQ

faq_blueprint = Blueprint('faq_blueprint', __name__)

@faq_blueprint.route('/faqs', methods=['GET'])
def get_faqs():
    return jsonify(FAQ.get_all()), 200

@faq_blueprint.route('/faqs', methods=['POST'])
def create_faq():
    data = request.json
    new_faq = FAQ.create(data['question'])
    return jsonify(new_faq), 201
