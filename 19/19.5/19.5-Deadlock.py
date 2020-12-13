# 19.5 Deadlock 
# 12/12/20
# When threads need to acquire multiple locks to enter a critical section, deadlock can result.
# As an example, suppose both T1 and T2 need to acquire locks L and M. If T1 first acquires L, and then T2
# then acquires M, they end up waiting on each other forever.

# Identify a concurrency bug in the program below, and modify the code to resolve the issue.

# U1 initiates a transfer to U2, and immediately afterwards, U2 initiates a transfer to U1. 

class Account:

    _global_id = 0
    
    def __init__(self, balance):
        self._balance = balance
        self._id = Account._global_id
        Account._global_id += 1
        self._lock = threading.RLock()

    def get_balance(self):
        return self._balance

    
    @staticmethod
    def transfer(acc_from, acc_to, amount):
        th = threading.Thread(target=acc_from._move, args=(acc_to, amount))
        th.start()


    def _move(self,acc_to, amount):
        with self._lock:
            if amount > self._balance:
                return False
            acc_to._balance += amount
            self._balance -= amount
            print('returning True')
            return True



