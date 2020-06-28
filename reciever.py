import requests 
import json

configurations={
    "CPU_UTILIZATION": 85,
    "MEMORY_UTILIZATION": 75,
    "DISK_UTILIZATION": 60
}

def check(data):
    alert = [data["SERVER_ID"]]
    if(data["CPU_UTILIZATION"] > configurations["CPU_UTILIZATION"]):
        alert.append("CPU_UTILIZATION VIOLATED")
    if(data["MEMORY_UTILIZATION"] > configurations["MEMORY_UTILIZATION"]):
        alert.append("MEMORY_UTILIZATION VIOLATED")
    if(data["DISK_UTILIZATION"] > configurations["DISK_UTILIZATION"]):
        alert.append("DISK_UTILIZATION VIOLATED")
    if(len(alert) > 1):
        return("Alert",alert)
    else:
        return("No Alert",alert)

URL = "http://127.0.0.1:5000/"

res = requests.get(URL)

res_json = res.json()


for data_json in res_json:

    data = json.loads(data_json)

    result, alert = check(data)

    response = requests.post(URL,{"result":result,"alerts":alert})

    print(response.text)
