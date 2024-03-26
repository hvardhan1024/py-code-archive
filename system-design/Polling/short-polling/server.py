from flask import Flask,jsonify
import random
import time
import threading


app = Flask(__name__)

data = {"value":random.randint(0,100)}

# thread related
update_thread = None
running = True 

# to update the data periodically
def update_data():
    global data 
    time.sleep(5)
    while running:
        data = {"value":random.randint(0,100)}
        print("Server data updated")
        time.sleep(random.randint(2,9))


# to provide data to clients
@app.route('/data',methods=['GET'])
def get_data():
    return jsonify(data)



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

