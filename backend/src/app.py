from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "CoreAuth API running"}

if __name__ == "__main__":
    app.run(debug=True)