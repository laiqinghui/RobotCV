from ThreadFactory import ThreadFactory
import threading

def funcToRun():
    count = 0
    while count < 5:
        print(count)
        count +=1
thread1 = threading.Thread(target = funcToRun)
#thread1 = ThreadFactory (1, "Thread-1", funcToRun)
thread1.start()
