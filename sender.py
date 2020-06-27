import requests
import http.server
import flask
from json import dumps as jsonstring

class data(object):
    def __init__(self,SERVER_ID,CPU_UTILIZATION,MEMORY_UTILIZATION,DISK_UTILIZATION):
        self.SERVER_ID = SERVER_ID
        self.CPU_UTILIZATION = CPU_UTILIZATION
        self.MEMORY_UTILIZATION = MEMORY_UTILIZATION
        self.DISK_UTILIZATION = DISK_UTILIZATION

def main():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True


    @app.route('/', methods=['GET'])
    def sendData():
        newData = data(12345,50,92,50)
        return(jsonstring(newData.__dict__))

    app.run()


if __name__ == "__main__":
    main()