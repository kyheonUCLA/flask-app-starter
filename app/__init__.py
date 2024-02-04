from flask import Flask, send_from_directory, send_file
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_folder='static')
CORS(app)

from app import routes