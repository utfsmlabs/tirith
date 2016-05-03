import sys
from socketIO_client import SocketIO, BaseNamespace

class DefaultNamespace(BaseNamespace):
    
    def on_connected(self):
        print("connected")
    
    def on_status(self, *args):
        print("on_status: ", args)
    

def main(args=None):
    if args is None:
        args = sys.argv[1:]    
    print("tirith client 0.1.0")
    
    print ("connecting...")
    with SocketIO('localhost', 5000, DefaultNamespace) as socketIO:
        socketIO.wait()


if __name__ == "__main__":
    main()
