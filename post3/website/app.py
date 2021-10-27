# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run


from flask import Flask, g, render_template, request

import sqlite3


app = Flask(__name__)

@app.route('/')


def main():
    return render_template('main_better.html')

# Show url matching

@app.route('/submit-basic/', methods=['POST', 'GET'])
def submit_basic():
    if request.method == 'GET':
        return render_template('submit-basic.html')
    else:
        try:
            insert_message(request)
            return render_template('submit-basic.html', thanks = True)
        except:
            return render_template('submit-basic.html', error=True)

@app.route('/view/')
def view():
    message=random_messages(5)
    #print(message)
    return render_template('view.html',messages=message )

def get_message_db():
    if 'message_db' not in g:
        g.message_db = sqlite3.connect("messages_db.sqlite")

    cursor = g.message_db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS messages(id INT,handle TEXT,message TEXT);")


    return g.message_db

def insert_message(request):
    message=request.form["message"]
    handle=request.form["handle"]
    db=get_message_db()
    cursor=db.cursor()
    cursor.execute("SELECT COUNT(*) FROM messages;")
    number_row=cursor.fetchone()[0]
    cursor.execute(f"""INSERT INTO messages (id,handle,message) VALUES ({number_row+1}, "{handle}", "{message}");""")
    db.commit()
    db.close()
def random_messages(n):
    db=get_message_db()
    cursor=db.cursor()
    cursor.execute("SELECT COUNT(*) FROM messages;")
    number_row=cursor.fetchone()[0]
    if n > number_row:
        n=number_row
    a=[]
    for i in range(n):
        cursor.execute("SELECT handle,message FROM messages ORDER BY RANDOM() LIMIT 1;")
        message=cursor.fetchone()
        a.append(message)
    return a