import requests 

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
    print(alert)
    if(len(alert) > 1):
        return("Alert",alert)
    else:
        return("No Alert",alert)

URL = "http://127.0.0.1:5000/"

res = requests.get(URL)

data = res.json()

result, alert = check(data)

print(result,end=", ")

for i in range(len(alert)-1):
    print(alert[i],end=", ")

print(alert[len(alert) - 1])