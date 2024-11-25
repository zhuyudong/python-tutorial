import time
from threading import Thread

# def countdown(n: int):
#     while n > 0:
#         print("T-minus", n)
#         n -= 1
#         time.sleep(1)


# """
# T-minus 3
# Still running
# T-minus 2
# T-minus 1
# """
# # t = Thread(target=countdown, args=(3,))
# # NOTE: daemon=True 设置为守护线程
# """
# T-minus 3
# Still running
# """
# t = Thread(target=countdown, args=(3,), daemon=True)
# # NOTE: 启动线程
# t.start()

# if t.is_alive():
#     print("Still running")
# else:
#     print("Completed")


# ------------------------------------------------------------------------------------ #
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print("T-minus", n)
            n -= 1
            time.sleep(1)


c = CountdownTask()
# T-minus 3
t = Thread(target=c.run, args=(3,))
t.start()
c.terminate()
t.join()
