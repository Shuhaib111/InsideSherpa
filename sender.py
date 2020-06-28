import requests
import http.server
import flask
from json import dumps as jsonstring
from flask import jsonify
from flask import request
import csv

def read_csv(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        fields = []
        fields = next(csvreader)

        rows = []
        for row in csvreader:
            rows.append(row)
        
        return fields,rows

class data(object):
    def __init__(self,SERVER_ID,CPU_UTILIZATION,MEMORY_UTILIZATION,DISK_UTILIZATION):
        self.SERVER_ID = SERVER_ID
        self.CPU_UTILIZATION = CPU_UTILIZATION
        self.MEMORY_UTILIZATION = MEMORY_UTILIZATION
        self.DISK_UTILIZATION = DISK_UTILIZATION

def main():

    filename = "data.csv"
    fields, rows = read_csv(filename)
    

    app = flask.Flask(__name__)
    app.config["DEBUG"] = True


    @app.route('/', methods=['GET','POST'])
    def handleRequests():
        if request.method=='GET':
            res = []
            for server in rows:
                newData = data(server[0],float(server[1]),float(server[2]),float(server[3]))
                res.append(jsonstring(newData.__dict__))
            return(jsonify(res))
        
        if request.method == 'POST':
            recievedData = (request.form).to_dict(flat=False)
            print(recievedData["result"][0],end=", ")
            print(', '.join(recievedData["alerts"]))
            return("Successfully recieved")
            

    app.run()


if __name__ == "__main__":
    main()