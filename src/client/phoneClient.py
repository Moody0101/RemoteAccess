from requests import get, post
from json import loads
from sys import argv
	
ip = "<IP of your pc>"
port = 5000

def main():
	try:
		run = True
		while True:
			command = input("cmd > ")
			if command != "!DISCONNECT":
				json_ = {"command": command}
				print(loads(post(f"{ip}:{port}/", json=json_).content.decode("utf-8"))["OUT"])
			else:
				run = False
	except Exception as e:
		print(e)
		print("SomeThing went wrong!!")

if __name__ == '__main__':
	main()