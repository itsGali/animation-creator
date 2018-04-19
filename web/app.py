from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/make-animation/')
def hello(name=None):
    return render_template(
        'make_animation.html',
        invitiation="do stuff bro",
        name=name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
