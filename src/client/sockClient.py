import socket
from dataclasses import dataclass
from json import dumps, loads


@dataclass
class Client:
	PORT: int = 4000
	SERVER: str = socket.gethostbyname(socket.gethostname())
	SOCKET: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	HEADER: int = 64
	DISCONNECTING: str = "!DISCONNECT"
	FORMAT: str = "utf-8"
	USERNAME: str = ""

	def setup(self):
		self.login()

	def login(self):
		self.USERNAME = input("Enter your name : ")
		if len(self.USERNAME) < 2:
			print("The username shoud have atleast 2 characters")
			while len(self.USERNAME) < 2:
				self.USERNAME = input("Enter your name : ")
				print("The username shoud have atleast 2 characters")
		print(f"THANKS! {self.USERNAME}")

	def connect(self):
		self.SOCKET.connect((self.SERVER, self.PORT))
		self.setup()
		self.prepareMessage()

	def close(self):
		self.SOCKET.close()
	def prepareMessage(self):
		run = True
		while run:
			MSG = input(f"Send msg {socket.gethostname()}@{self.SERVER}: ")
			if len(MSG) == "": MSG = " "
			
			MSG = {
				"msg": MSG,
				"name": self.USERNAME
			}

			self.send(dumps(MSG))
			self.receiveMessage()

	def receiveMessage(self):
		
		msg_len = self.SOCKET.recv(self.HEADER).decode(self.FORMAT)
		print(msg_len)
		msg_len = int(msg_len)
		msg = self.SOCKET.recv(msg_len).decode(self.FORMAT)
		print(msg)

	def send(self, msg: str):
		msg = msg.encode(self.FORMAT)
		self.SOCKET.send(str(len(msg)).encode(self.FORMAT))
		self.SOCKET.send(msg)
		

	@property
	def properties(self):
		return [i for i in dir(self.SOCKET) if not str(i).startswith("__")]

client_ = Client()
client_.connect()
client_.close()
