import requests 
import time 

url = "http://127.0.0.1:5000/data"

def fetchData():
    try:
        response = requests.get(url) 

        if response.status_code == 200:
            data = response.json()
            print("Received data:",data)
        else:
             print("Failed to fetch data:", response.status_code)

    except Exception as e:
        print("Error occurred: ",e)



def shortPolling(duration):
    while True:
        fetchData()
        time.sleep(duration)


shortPolling(2)