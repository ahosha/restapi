import socket
import sys, getopt

def main(argv):
    print('start')
    ip_addr = 'localhost'
    ip_port = 5001
    message = ''
    try:
        opts, args = getopt.getopt(argv, "hi:p:m:", ["ip_addr=", "ip_port=", "message="])

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
        elif opt in ("-m", "--message"):
            message = arg
    print('ip_addr is "', ip_addr)
    print('ip_port"', ip_port)
    print('message"', message)
    print('done')


    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (ip_addr, int(ip_port))
    print ('connecting to %s port %s' % server_address)
    sock.connect(server_address)

    try:

        # Send data
        # message = 'This is the message.  It will be repeated.'
        print ('sending "%s"' % message)
        sock.sendall(str.encode(message))

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(160)
            amount_received += len(data)
            print ('received "%s"' % data)

    finally:
        print ('closing socket')
        sock.close()


if __name__ == "__main__":
   main(sys.argv[1:])