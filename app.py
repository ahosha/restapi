#!/usr/bin/python

import socket
import sys, getopt

def main(argv):
    print ('start')
    ip_addr = 'localhost'
    ip_port = 5001
    try:
        opts, args = getopt.getopt(argv, "hi:p:", ["ip_addr=", "ip_port="])
    except getopt.GetoptError:
        print('app.py -i <ip_addr> -p <ip_port>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('app.py -i <ip_addr> -p <ip_port>')
            sys.exit()
        elif opt in ("-i", "--ip_addr"):
            ip_addr = arg
        elif opt in ("-p", "--ip_port"):
            ip_port = arg
    print('ip_addr is "', ip_addr)
    print('ip_port"', ip_port)
    print('done')

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = (ip_addr, int(ip_port))
    my_str = 'starting up on %s port %s' % server_address
    print(my_str)

    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print ('waiting for a connection')
        connection, client_address = sock.accept()

        try:
            print ('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(160)
                print ('received "%s"' % data)
                if data:
                    print ('sending data back to the client')
                    connection.sendall(data)
                else:
                    print ('no more data from', client_address)
                    break

        finally:
            # Clean up the connection
            connection.close()


if __name__ == "__main__":
   main(sys.argv[1:])