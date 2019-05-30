from flask import Flask, render_template, request
from datetime import datetime

import db


app = Flask(__name__)


@app.route('/', methods=['GET'])
def the_wall():
    return render_template('thewall.html', 
        title = "The Wall",
        last_update="2019-02-18",
        messages = db.get_messages())


@app.route('/', methods=['POST'])
def post_msg():
    tijd = str(datetime.now())
    inhoud = request.form['content']
    db.add_message(tijd, inhoud)
    
    s = "<p>Deze content werd gepost:</p><block>"
    s += request.form['content']
    s += "</block>"
    s += "<p>en dit op <span>" + str(datetime.now()) + "</span></p>"
    s += "<p>Normaal zou je nu een bericht moeten tonen aan de gebruiker of een redirect doen...</p>"
    s += "<a href='/'>Voorlopig kan je hier klikken om terug te gaan</a>"

    return (s)


if __name__ == '__main__':    
    app.run(host='127.0.0.2', port='8080', debug=True)
