import threading
import socket

HOST = 'localhost'
PORT = 9991

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
	for client in clients:
		client.send(message)

def handle(client):
	#handle login process here
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast(f'{nickname} left the chat.')
			nicknames.remove(nickname)
			break

def receive():
	while True:
		client, address = server.accept()
		print(f'Connected with {str(address)}')

		#ask for username and password
		client.send(f'NICK'.encode('ascii'))
		nickname = client.recv(1024).decode('ascii')

		nicknames.append(nickname)
		clients.append(client)

		print(f'Nickname of client is {nickname}.')
		broadcast(f'{nickname} joined the chat.'.encode('ascii'))
		client.send('Connected to the chat.'.encode('ascii'))

		thread = threading.Thread(target = handle, args = (client,))
		thread.start()

def login():

	client.send(f'Welcome to Secret Word Storage!\nEnter your username: '.encode('ascii'))
	username = client.recv(1024)
	client.send(f'password: ')
	password = client.recv(1024)

	#create an SQL query - does this username have this password as the value?
		#if yes, grant them permission to their directory on the service
		#else, bounce them out



#need to actually run our main method
receive()


#login method
	#ask for username
	#ask for password

	#create a database query
	#does the hashed version of their password equal

