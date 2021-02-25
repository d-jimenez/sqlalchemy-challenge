import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

engine=create_engine('sqlite:///Resources/hawaii.sqlite')

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement=Base.classes.measurement
Station=Base.classes.station

#Flask Routes
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"Dates must be in the following formatt: yyyy-mm-dd with no leading zeros<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

#Precipitation list - key error (non unique values) needs to be fixed
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all measurment data for date as keys and percipitation (prcp) as values
    results = session.query(Measurement.date,Measurement.prcp).all()
    
    session.close()
    
#     all_prcp=[]
    for key, value in results:
        prcp_dict={}
        prcp_dict[key].append(value)

    # Convert list of tuples into normal list
#     all_prcp = list(np.ravel(results))

    return jsonify(prcp_dict)

#Stations list - working
@app.route("/api/v1.0/stations")
def stations():
    session=Session(engine)
    
    results=session.query(Station.station, Station.name).all()
    
    return jsonify(results)

#Temperature Observations - working
@app.route("/api/v1.0/tobs")
def tobs():
    session=Session(engine)
    
    station_activity=session.query(Measurement.station,func.count(Measurement.date))\
    .group_by(Measurement.station)\
    .order_by(func.count(Measurement.date).desc()).all()
    
    most_active_station=station_activity[0][0]
    
    year_ago=dt.date(2017,8,23)-dt.timedelta(days=365)
    
    sel=[Measurement.date,Measurement.tobs]
    
    results=session.query(*sel)\
    .filter(Measurement.station==most_active_station)\
    .filter(Measurement.date>=year_ago)\
    .order_by(Measurement.date.desc()).all()

    return jsonify(results)

# #When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# @app.route("/api/v1.0/stations/<start>")
# def start():
#     session=Session(engine)
    
#     temp_start=session.query(MEasurement.date,Measurement.
# #When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
# @app.route("/api/v1.0/stations/<start>/<end>")
# def start_end():
#     session=Session(engine)
    
if __name__ == '__main__':
    app.run(debug=True)