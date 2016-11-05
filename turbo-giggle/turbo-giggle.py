import os
import sqlite3
from flask import Flask, g

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'turbo-giggle.db'),
    SECRET_KEY='\x99n\x82\x9bG\xa7{+\xe2,\xf4\xf7|\x96\xa0\xeaD\xa9\xd9\xdae',
    USERNAME='admin',
    PASSWORD='default'
))


# Routes

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/createSession', method='POST')
def create_session():
    pass


@app.route('/form', methods=['POST', 'GET'])
def form():
    pass


# Database Functions

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


# Command line commands
@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
print 'Initialized the database.'
