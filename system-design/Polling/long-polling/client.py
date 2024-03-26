import requests 
import time 

url = "http://127.0.0.1:5000/long_polling"

def initiateLongPolling():
    try:
        print("Making request")
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print("Received Data:",data )
            initiateLongPolling()
        else:
            print("Failed to fetch data:", response.status_code)
            initiateLongPolling()
    except Exception as e:
        print("Error occured: ",e)


initiateLongPolling()
