import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys

#Save Table References
Measurement = Base.classes.measurement
Station = Base.classes.station

sessions = Session(engine)

app = Flask(_name_)

#Convert the query results to a dictionary using date as the key and prcp as the value

@app.route("/")
def home()
    return("/api/v1.0/precipitation")






if __name__ == "__main__":
    app.run(debug=True)
