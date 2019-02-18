from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

class Message:
    def __init__(self):
        self.time = ""
        self.content = ""

# in-memory opslag van messages
# TODO: messages moeten uit database gehaald worden!
messages = []

m1 = Message()
m1.time = "2019-02-18 11:00"
m1.content = "Hallo!"
    
m2 = Message()
m2.time = "2019-02-18 11:05"
m2.content = "De muur?"

messages.append(m1)
messages.append(m2)

@app.route('/', methods=['GET'])
def the_wall():
    return render_template('thewall.html', 
        title = "The Wall",
        last_update="2019-02-18",
        messages = messages)

@app.route('/', methods=['POST'])
def post_msg():
    # TODO: message moet toegevoegd worden aan de database

    m = Message()
    m.content = request.form['content']
    m.time = str(datetime.now())

    # tijdelijk: voeg toe aan in-memory lijst
    messages.append(m)

    s = "<p>Deze content werd gepost:</p><block>"
    s += request.form['content']
    s += "</block>"
    s += "<p>en dit op <span>" + str(datetime.now()) + "</span></p>"
    s += "<p>Normaal zou je nu een bericht moeten tonen aan de gebruiker of een redirect doen...</p>"
    s += "<a href='/'>Voorlopig kan je hier klikken om terug te gaan</a>"

    return (s)

app.run(host='127.0.0.2', port='8080', debug=True)