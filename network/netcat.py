import socket


class Netcat:
    """ Python 'netcat like' module """

    def __init__(self, ip, port):
        self.buffer = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length=1024):
        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)

    def read_until(self, data):
        """ Read data into the buffer until we have data """

        while data not in self.buffer:
            self.buffer += self.socket.recv(1024)

        pos = self.buffer.find(data)
        rval = self.buffer[:pos + len(data)]
        self.buffer = self.buffer[pos + len(data):]

        return rval

    def write(self, data):
        self.socket.send(data)

    def close(self):
        self.socket.close()
