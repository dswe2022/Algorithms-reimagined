# 19.9 Test the Collatz conjecture in parallel

# Design a multi-threaded program for checking the Collatz conjecture. 
# Make full use of the cores available to you. To keep your program from overloading the system, 
# you should not have more than n threads running at a time.
# hint: try using a multi-threaded checker.

def worker(lower, upper):
    for i in range(lower, upper+1):
        assert collatz_check(i, set())
    print('(%d,%d)' % (lower, upper))


def collatz_check(x, visited):
    if x ==1:
        return True
    elif x in visited:
        return False
    visited.add(x)
    if x & 1: # odd number
        return collatz_check(3 * x +1, visited)
    else: #even number
        return collatz_check(x>>1, visited) #divide by 2
    #Uses the library thread pool for task assignment and load balancing
    executor = concurrent.futures.ProcessPoolExecutor(max_owrkers=NTHREADS)
    with executor:
        for i in range(N //RANGESIZE):
            executor.submit(worker, i * RANGESIZE +1 , (i+1) * RANGESIZE)