from flask import Flask, render_template, request
import simplebot as cb

# flask index page initialisation
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test", methods=['GET', 'POST'])
def chat_response():
    if request.method == 'GET':
        msg = request.form["msg"]
        response_msg = cb.getResponse(msg)
        return response_msg
    elif request.method == 'POST':
        return render_template("index.html")

# run server
if __name__=="__main__":
    app.run(debug=True)