import signal
import stomp
import sys
import time

PORT = 61501

def send_message(hosts, destination):
    hosts1 = map(lambda h: (h, PORT), hosts)
    print('Sending to %s' % hosts1)
    c = stomp.Connection(hosts1)
    try:
        c.start()
        c.connect()
        c.send('hello world', destination=destination)
    finally:
        c.stop()

def signal_handler(signal, fame):
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    destination = sys.argv[1]
    hosts = sys.argv[2:]
    send_message(hosts, destination)

if __name__ == '__main__':
    main()
