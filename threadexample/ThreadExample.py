import threading
import time
import random
from builtins import range

class ThreadExample(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        max_iterations = 5
        for _ in range(max_iterations):
            seconds = random.randint(0, 3)
            print(self.name + " sleep " + str(seconds))
            time.sleep(seconds)

if __name__ == '__main__':
    threadExample = ThreadExample("first")
    threadExample.start()
    threadExample2 = ThreadExample("second")
    threadExample2.start()
    threadExample.join()
    threadExample2.join()
    print("done")