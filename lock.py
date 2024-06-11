from threading import *
l = RLock()    # or use for lock use Lock()
print("Main thread trying to acquire lock")
l.acquire()
print("Main thread trying to acquire lock agian")
l.acquire()
