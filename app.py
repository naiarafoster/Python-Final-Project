from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "5615551212"


@app.route('/', methids=('GET', "POST"))
@app.route('/index')
def index():
    return render_template('index.html')


app.run(host='127.0.0.1', port=3900, debug=True)
