from requests import get, post
from json import loads
from socket import gethostbyname, gethostname
ip = gethostbyname(gethostname())
print(ip)
port = 5000


def main():
	try:
		run = True
		while True:
			command = input("cmd > ")
			if command != "!DISCONNECT":
				json_ = {"command": command}
				print(loads(post(f"http://{ip}:{port}", json=json_).content.decode("utf-8"))["OUT"])
			else:
				run = False
	except Exception as e:
		print(e)
		print("SomeThing went wrong!!")

if __name__ == '__main__':
	main()