from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from src import schemas, crud
from src.security import create_access_token, verify_password, token_required
from src.database import get_db

bp = Blueprint("auth", __name__)

@bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if not data:
        return jsonify({"error": "request body is empty"}), 400
    
    try:
        user_in = schemas.UserCreate(**data)
    except Exception as e:
        return jsonify({"error": str(e)}), 422
    
    db: Session = next(get_db())

    if crud.get_user_by_email(db, user_in.email):
        return jsonify({"error": "user already exists"}), 400
    
    user = crud.create_user(db, user_in)

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email
    }), 201
