import socket
import argparse

parser = argparse.ArgumentParser(description='Send a string to server and print response')
parser.add_argument('string', metavar='STR', type=str, nargs=1, help='The string to send to the server')
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 1234))

s.send(args.string[0].encode('utf-8'))
print(s.recv(1024).decode('utf-8'))
s.close()
