#!/usr/bin/python3

# add command line arguments i.e. brutehash --sha1 <hash_value>
from urllib.request import urlopen
import hashlib

def hashword():
	counter = 1
	for password in passlist.split('\n'):
		print('Testing hash ' + str(counter) + '/1000000', end = '\r')
		counter += 1
		hashed_word = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
		if hashed_word == user_hash:
			print('\nFound solution for entered hash: ' + password)
			exit(0)
	print('\nHaven\'t found solution for entered hash')

user_hash = input('Enter SHA1 hash value: \n')
passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
hashword()
