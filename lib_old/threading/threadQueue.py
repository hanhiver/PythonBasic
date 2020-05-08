import queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print('%s processing %s' % (threadName, data))
            else:
                queueLock.release()

            time.sleep(1)

threadList = ['Thread-1', 'Thread-2', 'Thread-3']
nameList = ['One', 'Two', 'Three', 'Four', 'Five']
queueLock = threading.Lock()
workQueue = queue.Queue(10)

threads = []
threadID = 1

# Create new threads.
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# fill the threads to the queue.
queueLock.acquire()

for word in nameList:
    workQueue.put(word)

queueLock.release()

# Wait the queue empty.
while not workQueue.empty():
    pass

# Announce the thread to quite.
exitFlag = 1

# Wait for all thread ended.
for t in threads:
    t.join()

print('Exit the main thread.')
