from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def server_page():
    return render_template('index.html')


app.run(port=5000)