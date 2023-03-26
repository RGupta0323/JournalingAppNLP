# app.py
from flask import Flask ,render_template

app = Flask(__name__)
# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # returning a response
    return render_template("Home.html") 

if __name__ == "__main__":
    app.run(host='0.0.0.0')