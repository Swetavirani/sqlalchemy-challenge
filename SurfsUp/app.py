import sqlalchemy
from flask import Flask, jsonify, url_for
import datetime as dt
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# Database Setup
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Routes
@app.route("/")
def home_page():
  data = {
    'routes': [
        url_for('precip'),
        url_for('stations'),
        url_for('tobs'),
        url_for('start_date', start='start_date'),
        url_for('start_end', start='start_date', end='end_date'),
    ]
  }
  return jsonify(data)

    
@app.route("/api/v1.0/precipitation")
def precip():
    most_recent_date = dt.date(2017,8,23)
    prev_year = most_recent_date- dt.timedelta(days=365)
    scores = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).\
                order_by(Measurement.date).all()
    result_dict = dict(scores)
    session.close()
    return jsonify(result_dict)

@app.route("/api/v1.0/stations")
def stations():
    active_station = session.query(Measurement.station, func.count(Measurement.id)).\
            group_by(Measurement.station).order_by(func.count(Measurement.id).desc()).all()
    stations_dict = dict(active_station)
    session.close()
    return jsonify(stations_dict)

@app.route("/api/v1.0/tobs")
def tobs():
    most_recent_date = dt.date(2017,8,23)
    prev_year = most_recent_date- dt.timedelta(days=365)
    max_temp_obs = session.query(Measurement.station, Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prev_year).filter(Measurement.date < most_recent_date).\
                       order_by(Measurement.date).all()
    tobs_dict = dict(max_temp_obs)
    session.close()
    return jsonify(tobs_dict)


@app.route("/api/v1.0/<start>")
def start_date(start):
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
                                func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    
    session.close()
    tobsall = []

    for min,avg,max in result:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobsall.append(tobs_dict)
        
    return jsonify(tobsall)

@app.route('/api/v1.0/<start>/<end>')
def start_end(start,end):
    queryresult = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
                func.max(Measurement.tobs)).filter(Measurement.date >= start).\
                filter(Measurement.date <= end).all()

    session.close()

    tobsall = []
    for min,avg,max in queryresult:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobsall.append(tobs_dict)

    return jsonify(tobsall)


if __name__ == '__main__':
    app.run(debug=True)