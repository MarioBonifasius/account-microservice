from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Konfigurasi Talisman untuk header keamanan
    Talisman(app, content_security_policy={
        'default-src': "'self'",
        'script-src': "'self'",
        'style-src': "'self'"
    })
    
    # Konfigurasi CORS untuk mengizinkan cross-origin request
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    return app
