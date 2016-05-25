import sys
import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class TestComponent(ApplicationSession):
    
    async def onJoin(self, details):
        print("session ready")
        
        def add2(x, y):
            return x + y
            
        try:
            await self.register(add2, u"tirith.add2")
            print ("procedure registered")
        except Exception as e:
            print ("could not register procedure: {0}".format(e))
    

def main(args=None):
    if args is None:
        args = sys.argv[1:]    
    print("tirith client 0.2.0")
    
    print ("connecting...")
    
    runner = ApplicationRunner(url=u"ws://frameshift:8080/ws", realm=u"realm1")
    # throws socket.gaierror on 404
    runner.run(TestComponent)
    


if __name__ == "__main__":
    main()