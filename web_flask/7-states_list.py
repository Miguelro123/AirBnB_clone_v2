#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """ Print the number """
    return render_template("7-states_list.html", states=storage.all(State))


@app.teardown_appcontext
def teardown(error):
    """ close storage """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
