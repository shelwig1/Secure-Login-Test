import socket
import threading

HOST = 'localhost'
PORT = 9991

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == 'NICK':
				client.send(nickname.encode('ascii'))
			else:
				print(message)

			if message == 'P@SSW13RD':
				password(message)

		except:
			print('Error occured, disconnected from server.')
			client.close()
			break


def write():
	while True:
		message = f'{nickname}: {input("")}'
		client.send(message.encode('ascii'))


def password(message):
	#print the message
	#take input - hash the input, encode the input
	#send it up, baby
	print (message)
	password = input("")
	hashedpass = hashlib.md5(password.encode('ascii'))

	#If it throws an encoding error, it's here 
	client.send(hashedpass)


receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()


#If the server requests a password, we pass it to them PREHASHED
	#the server never even sees our plaintext
	#neat! We get to build this as secure