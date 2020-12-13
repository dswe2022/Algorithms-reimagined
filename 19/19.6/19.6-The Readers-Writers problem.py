# 19.6 
# 12/12/20
# Implement a synchronization mechanism for the first readers-writers problem.


# LR and LW are class attributes in the RW class.
# They serve as read and write locks. The integer
# variable read_count in RW tracks the number of readers

import threading

class Reader(threading.Thread):

    def run(self):
        while True:
            with RW.LR:
                RW.read_count +=1
            
            print(RW.data)
            with RW.LR:
                RW.read_count -=1
                RW.LR.notify()
            do_something_else()



class Writer(threading.Thread):

    def run(self):
        while True:
            with RW.LW:
                done = False
                while not done:
                    with RW.LR:
                        if RW.read_count == 0:
                            RW.data +=1
                            done = True
                        else:
                            #use wait/notify to avoid busy waiting
                            while RW.read_count != 0:
                                RW.LR.wait()
            
            do_something_else()


