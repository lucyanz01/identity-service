import os 
import jwt 
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY").strip() if os.getenv("SECRET_KEY") else None
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY no definida")

def create_access_token(user_id: str):
    payload = {
        "sub": str(user_id),
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise RuntimeError("Token expirado")
    except jwt.InvalidTokenError:
        raise RuntimeError("Token inválido")
    
def token_required(f):
    @wraps(f)
    
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"error": "token requerido"}), 401
        
        try:
            token = auth_header.replace("Bearer", "").strip()
            payload = verify_access_token(token)
            request.user_id = payload["sub"]
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 401
        
        return f(*args, **kwargs)
    
    return decorated
