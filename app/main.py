from flask import Flask, jsonify, request
from app.models.faq_model import FAQ
from app.routes.faq_routes import faq_blueprint
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.register_blueprint(faq_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
