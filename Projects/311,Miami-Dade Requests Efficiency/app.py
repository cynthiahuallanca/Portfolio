from sqlalchemy import create_engine
from config import password
import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Connect to local database
rds_connection_string = f"root:{password}@localhost/services_311_db"
engine = create_engine(f'mysql://{rds_connection_string}')

@app.route("/")
def index():
    #Return to Home
    return render_template('index.html')

@app.route("/services")
def service():
    #TEST small number 
    service = pd.read_sql_query('select * from requests_311 limit 500', con=engine)
    data = {
        "issue_type": service.issue_type.tolist(),
        "latitude": service.latitude.tolist(),
        "longitude": service.longitude.tolist(),
        "zip_code": service.zip_code.tolist() 
    }
    return jsonify(data)

@app.route("/census")
def census():
    #TEST small number 
    census = pd.read_sql_query('SELECT * FROM census where id > 1;', con=engine)
    data = {
        "Zipcode": census.name.tolist(),
        "Poverty": census.Poverty_perc.tolist(),
        "Population": census.Total_Poverty_Population.tolist(), 
        "Income": census.Total_Poverty_Population.tolist()
        
    }
    return jsonify(data)


@app.route("/plot2")
def plot2():
    return render_template('plot2.html')

# @app.route("/plot3")
# def plot3():
#     service = pd.read_sql_query('select * from service_chart', con=engine)
#     data = {
#         "symbol": service.symbol.tolist(),
#         "date": service.date.tolist(),
#         "price": service.price.tolist(),
#         }
#     return render_template('plot3.html')

# @app.route("/plot3-data")
# def plot3Data():
#     service = pd.read_sql_query('select * from service_chart', con=engine)

#     #print(service.to_dict())
#     data_list = list()
#     for i, v in service.iterrows():
#         data = {
#             "symbol": v['symbol'],
#             "date": v['date'],
#             "price": v['price'],
#             }
#         data_list.append(data)

#     print(data_list)

#     data = {
#         "symbol": service.symbol.tolist(),
#         "date": service.date.tolist(),
#         "price": service.price.tolist(),
#         }
#     return jsonify(data_lists)

@app.route("/efficiency-data")
def efficiency():
    efficiency = pd.read_sql_query('select * from city_efficiency limit 500', con=engine)
    data2 = efficiency.to_dict('records')
    data = {
        "city":efficiency.city.tolist(),
        "efficiency": efficiency.efficiency.tolist()
    }
    return jsonify(data2)

@app.route("/plot3")
def plot3():
    #Return to Home
    return render_template('plot3.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/links")
def links():
    return render_template('links.html')

@app.route("/efficiency-mean")
def mean():
    mean = pd.read_sql_query('select * from zip_mean', con=engine)
    data2 = mean.to_dict('records')
    return jsonify(data2)

if __name__ == "__main__":
    app.run()