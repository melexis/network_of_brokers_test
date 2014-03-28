import stomp
import sys
import time

class Listener:
    def on_error(self, headers, message):
        print('Received error %s' % message)

    def on_message(self, headers, message):
        print('Received a message %s' % message)

def listen(hosts, destination):
    hosts1 = map(lambda h: (h, 61501), hosts)
    print('Listening to %s' % hosts1)
    conn = stomp.Connection(hosts1)
    conn.set_listener('', Listener())
    conn.start()
    conn.connect()
    conn.subscribe(destination=destination, ack='auto')
    time.sleep(3600)

def main():
    destination = sys.argv[1]
    hosts = sys.argv[2:]
    listen(hosts, destination)

if __name__ == '__main__':
    main()
