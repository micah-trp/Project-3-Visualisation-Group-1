# import necessary libraries
# from models import create_classes
import os

import numpy as np
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, or_
from sqlalchemy.ext.automap import automap_base

from flask import Flask, jsonify, request, render_template, redirect

import sqlite3
import pickle


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///quake_mmi_data.db")

# # reflect an existing database into a new model
# Base = automap_base()

# # reflect the tables
# Base.prepare(autoload_with=engine, reflect=True)

# # Save reference to the table
# print(Base.classes.keys())

# quake = Base.classes.quake_mmi_test



#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# main html index

@app.route("/")
def main():
    return render_template("index.html")

# ------------------------------------------------
# API 
# ------------------------------------------------

# Data table

@app.route("/api/data")
def quake_mmi_data():

    # with engine.connect as connection:
    connection = engine.connect()


    results = connection.execute('select * from quake_mmi_test')

    rows = results.fetchall()
    data = [dict(row) for row in rows]

    connection.close()

    return jsonify(data)

    # results = [list(r) for r in results]





# @app.route("/api/v1.0/quake_mmi")
# def quake_mmi_data():

#     session = Session(engine)

#     results = session.query( quake.date, quake.mmi, quake.magnitude, quake.longitude, quake.latitude, quake.time, quake.depth).all()
#     earthquake = list(np.ravel(results))

    # results = [list(r) for r in results]

    # earthquake = {
    #     "table": results
    # }

    # session.close()
    # Convert list of tuples into normal list

    
    # return jsonify(earthquake)
    

if __name__ == '__main__':
    app.run(debug=True)
