#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """ close storage """
    storage.close()


@app.route('/states_list')
def states_list():
    """ Print the number """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
