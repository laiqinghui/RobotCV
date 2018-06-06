import threading
import time

exitFlag = 0

class ThreadFactory (threading.Thread):
   def __init__(self, threadID, name, target):
      threading.Thread.__init__(self, target = target)
      self.threadID = threadID
      self.name = name
      self.target = target
