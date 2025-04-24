from flask import Flask
import time
time.sleep(5)  # Allow time sync to avoid msg_id error
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the Flask app on port 80
    app.run(host='0.0.0.0', port=80)
