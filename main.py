from flask import Flask, rndr_template

app = Flask(_name_)

@app.route("/", methods=["Get"])
def home_page():
    return render_template("home.html")

@app.route("/get-details", methods=["GET"])
def get_details():
    return{
        "name": "Arriane",
        "message": "Succesful"
         }


if __name__ == "__main__":
    app.run(debug=True)