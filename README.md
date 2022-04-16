# REMOTE ACCESS

### Description:

Remote access is a command line interface that enables accessing other devices in your private network.

### Used technologies 

- Python
- TCP
- Sockets
- AF_INET
- Flask

### How to use ?
#### Steps

- Clone repo
- change the host host in [flask.py](https://github.com/Moody0101/RemoteAccess/blob/main/src/Flask_/app.py) to the ip that was granted by your router.

to get this ip you should type in windows:
```cmd
C:\Users> ipconfig
```
in linux:
```bash
moody@DESKTOP-Q65T2QS:/mnt/c$ ip a | grep 192.168
```
something like this will pop up

![IPV4](./img/IPV4.jpg)

when you find it change this line in [flask.py](https://github.com/Moody0101/RemoteAccess/blob/main/src/Flask_/app.py):

```python
app.run(host="192.168.137.1")
```

before connecting from the other device using this script [phoneClient.py](https://github.com/Moody0101/RemoteAccess/blob/main/src/client/phoneClient.py), run  the socket server using [server.py](https://github.com/Moody0101/RemoteAccess/blob/main/src/server/server.py) change the ip var in 
[phoneClient.py](https://github.com/Moody0101/RemoteAccess/blob/main/src/client/phoneClient.py)
to the one you found.
```python
ip = "192.168.137.1" #in my case it would be.
```

run [phoneClient.py](https://github.com/Moody0101/RemoteAccess/blob/main/src/client/phoneClient.py) from your other device.

Now you can execute commands remotely.

> You should be connected to the same network you dummy






















