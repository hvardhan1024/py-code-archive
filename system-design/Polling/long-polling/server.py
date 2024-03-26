from flask import Flask,jsonify
import random 
import threading 
import time 
import copy 

app = Flask(__name__)
data = {"value":random.randint(0,100)}
last_data = copy.deepcopy(data) 


# thread related
update_thread = None
running = True 

# updating data periodically
def update_data():
    global data, last_data
    time.sleep(5)
    while running:
        last_data = copy.deepcopy(data) 
        data = {"value":random.randint(0,100)}
        print(data,last_data)
        print("Server data updated")
        time.sleep(random.randint(1,40)) 


# long polling route
@app.route('/long_polling',methods=['GET'])
def long_polling():
    global data, last_data
    start_time = time.time()
    while True:
        # Long polling 30 second timeout
        if time.time() - start_time < 30:
            if data != last_data:
                last_data = copy.deepcopy(data) 
                return jsonify(data)
            else:
                time.sleep(1)
        else:
            return jsonify({"error":"Long polling timeout"})


if __name__ == '__main__':
    update_thread = threading.Thread(target=update_data)
    update_thread.daemon = True 
    update_thread.start()

    try:
        app.run(debug=True,port=5000)
    finally:
        if update_thread is not None:
            running = False 
            update_thread.join()
