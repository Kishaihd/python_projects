#How to use locks

with lock:
    print 'critical section 1'
    print 'critical section 2'

#Once done, i.e., context leaves that function, it unlocks!
