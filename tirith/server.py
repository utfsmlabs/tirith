import sys
from flask import Flask, jsonify
from flask_socketio import SocketIO, emit

clients = set()
app = Flask(__name__)
app.config["debug"] = True
app.config["port"] = 6969
socketio = SocketIO(app)

@app.route("/status.json")
def status():
    return jsonify(clients=clients)


@socketio.on("connected")
def connected(json):
    print("received: " + str(json))
    emit("status", "wena")

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("tirith server")
    socketio.run(app)
    

if __name__ == "__main__":
    main()
