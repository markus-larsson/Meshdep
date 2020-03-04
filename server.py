# the server class,
# will run the server

import asyncore
from includes import database
from includes import nodeserver
import time


ACTIVE = True
db = database.Database("192.168.1.240", "8159", "root", "lol123", "meshdep")
ns = nodeserver.NodeServer("127.0.0.1", "6220", 3)

while ACTIVE:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        del db
        del ns
        ACTIVE = False
        
