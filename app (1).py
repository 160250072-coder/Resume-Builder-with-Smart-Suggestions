from flask import Flask, render_template, request
from model import get_suggestions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        user_input = request.form["skills"]
        role, suggestions, missing = get_suggestions(user_input)

        result = {
            "role": role,
            "suggestions": suggestions,
            "missing": missing
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)