import time
from threading import Thread


def countdown(n: int):
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(1)


t = Thread(target=countdown, args=(3,))
# NOTE: daemon threads are abruptly terminated when the program exits
# t = Thread(target=countdown, args=(3,), daemon=True)
# NOTE: start() method is used to start the thread
t.start()
# NOTE: join() 加入当前线程，等待线程结束【optional】
# t.join()
# NOTE: is_alive() method can be used to check if a thread is still running
if t.is_alive():
    print("Still running")
else:
    print("Completed")
# T-minus 3
# Still running
# T-minus 2
# T-minus 1
