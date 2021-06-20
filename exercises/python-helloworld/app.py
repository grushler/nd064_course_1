import logging
logging.basicConfig(
        format='[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(name)s] [%(message)s]',
        level=logging.DEBUG, 
        filename='app.log')

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("Homepage called successfully!")
    return "Hello Udacity!"

@app.route("/status")
def healthCheck():
    app.logger.info("Health check API called successfully!")
    data = {"result": "OK: Healthy"}
    return jsonify(data), 200

@app.route("/metrics")
def metrics():
    app.logger.info("Metrics API called successfully!")
    data = {"status": "success", "data": {"UserCount": 100, "UserCountActive": 20}}
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
