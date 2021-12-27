#Ethan Armbruter
#12/20/21
#Flask App that takes in a POST request,
#connects to an AWS RDS MYSQL server and adds the data

####IMPORTS######
import datetime
from . import config
####FROM/IMPORTS######
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
username = config.username
password = config.password
webaddr = config.web_address
db = config.db_name

conn = 'mysql://{0}:{1}@{2}:3306/{3}'.format(username, password, webaddr, db)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn
Session = sessionmaker(bind=conn)
session = Session()

db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"


##Connect to the DB

class temperature_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    celsius = db.Column(db.Float)
    fahrenheit = db.Column(db.Float)

    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit


@app.route("/sensor_post", methods=['POST'])
def sensor_post():
    data_string = "Received post at: %s\n" % datetime.datetime.now()
    print(data_string)
    data = request.json
    data_string = data_string + str(data)
    #new_record = sensor_readings(celsius=25, fahrenheit=78)
    # db.session.add(new_record)
    # db.session.commit()

    # sensor_readings.add_new_reading("1","25", "77")

    #Sensor Data is the nested array that contains the data
    for entry in data["Temperature"]:
        new_record = temperature_data(celsius=entry["Celsius"], fahrenheit=entry["Fahrenheit"])
        data_string = "Received post at: %s\n" % datetime.datetime.now()
        print(data_string)
        print("Thanks for the post!!")

    db.session.add(new_record)
    db.session.commit()
    response = "Thanks for the post!!"

    return response


if __name__ == '__main__':
    app.run(debug=True)
