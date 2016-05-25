import sys
import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from components.monitor import MonitorComponent

def main(args=None):
    
    if args is None:
        args = sys.argv[1:]
    print("tirith monitor 0.2.0")
    print("connecting")
    
    runner = ApplicationRunner(url=u"ws://frameshift:8080/ws", realm=u"realm1")
    runner.run(MonitorComponent)
    
if __name__ == "__main__":
    main()