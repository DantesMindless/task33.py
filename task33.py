import threading
lock:threading.Lock =threading.Lock()
lock2:threading.Lock =threading.Lock()
counter = 0

def count(lock:threading.Lock):
    global counter
    for i in range(1000000):
        with lock, lock2:
            counter += 1

t1 = threading.Thread(target=count, args=(lock,))
t2 = threading.Thread(target=count, args=(lock,))
t1.start()
t2.start()
t1.join()
t2.join()
print(counter)