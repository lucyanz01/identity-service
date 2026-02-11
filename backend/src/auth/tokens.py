import os 
import jwt 
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITH = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY no definida")

