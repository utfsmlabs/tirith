import asyncio
from autobahn.asyncio.wamp import ApplicationSession

class MonitorComponent(ApplicationSession):
    
    async def onJoin(self, details):
        print("session ready")
        
        def log(thing):
            print(str(thing))
            
        try:
            await self.register(log, u"tirith.log")
            print ("procedure registered")
        except Exception as e:
            print ("could not register procedure: {0}".format(e))