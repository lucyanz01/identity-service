from flask import Flask
from src.routes.auth import bp as auth_bp
from flask_cors import CORS
import os
from src import models
from src.database import engine, Base 

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_secret_key')
CORS(app)

with app.app_context():
    Base.metadata.create_all(bind=engine)

app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def home():
    return {"message": "API is running"}, 200

if __name__ == "__main__":
    app.run(debug=True)