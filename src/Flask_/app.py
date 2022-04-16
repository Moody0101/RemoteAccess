"""
This api is acting as a middleware, phone sends http requests and the api 
forwards them to the host that is resposible of executing the commands
and returning the command's output then it gets forwarded again to phone as
json, in the client (which most of the time is Termux), it loads and decodes the
response.
then prints it.

[CLIENT] =|POST req|====> [FLASK] =|COMMAND|===> [SOCKET SERVER]

"""

from flask import Flask, request
import socket
import threading
app = Flask(__name__)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT: int = 4000
host = socket.gethostname()
sock.connect((host, PORT))


def send(msg):
	msg = msg.encode("utf-8")
	sock.send(str(len(msg)).encode("utf-8"))
	sock.send(msg)

def receive(BUFFERLEN):
	msg_len = sock.recv(BUFFERLEN).decode("utf-8")
	msg_len = int(msg_len)
	msg = sock.recv(msg_len).decode("utf-8")
	return msg



@app.route("/", methods=["POST", "GET"])
def main():

	if request.method == 'POST':
		send(request.json["command"])
		output = receive(10)
		return {
			"OUT": output
		}

	else:
		return {
		"Hello": "hello"
		}


# recv_t = threading.Thread(target=receive)
# send_t = threading.Thread(target=send)

if __name__ == '__main__':
	app.run(host='192.168.53.3', threaded=False, debug=True)