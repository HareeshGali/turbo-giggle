import os
import sqlite3
from flask import Flask, g, request

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
def index():
    return app.send_static_file('index.html')


@app.route('/signin')
def signin():
    return app.send_static_file('signin.html')


@app.route('/form')
def form():
    return app.send_static_file('form.html')


# takes in JSON from app
@app.route('/createSession', methods=['POST'])
def create_session():
    conn = get_db()
    c = conn.cursor()
    body = request.get_json()

    c.execute("INSERT INTO Sessions VALUES (time('now','+3 minutes'), ?, 1, ?)", (body['patientID'], body['hash']))
    return "Successfully created a session"


@app.route('/validateSession', methods=['POST'])
def validate_session():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT EXISTS(SELECT * from Patients WHERE patientID=? AND hash=?)", (request.form['patientID'], request.form['hash']))
    queryResult = c.fetchone()[0]
    if queryResult:
    	c.execute("UPDATE Patients \
            validate = TRUE \
            SET expires=time('now','+1 day') \
            WHERE patientID=request.form['patientID']")
    else:
        # todo send client(Doc) user does not exist error/wrong hash error
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
