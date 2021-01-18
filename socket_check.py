import socket

a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

location = ("192.168.1.186",5001)

result_of_check = a_socket.connect_ex(location)
print(result_of_check)
if result_of_check == 0:
    print("Port is open")
else:
    print("Port is closed")
