import platform
import multiprocessing
import socket

def showinfo(tip, info):
    print("{}:{}".format(tip, info))


showinfo("Name of machine: ",platform.node())
showinfo("operating system name: ",platform.system())
showinfo("operating system version: ",platform.version())
showinfo("number of cup",multiprocessing.cpu_count())
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
showinfo("IP address: ",ip)