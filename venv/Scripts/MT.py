from time import sleep

from threading import *

class Hello(Thread):
    def run(self):

        for i in range(5):
            print('Hello', i+1)
            sleep(1)




class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi', i+1)
            sleep(1)

a = Hello()
b = Hi()
a.start()
sleep(0.1)
b.start()
a.join()
b.join()
print("BYE")