# ******************************************************
# Python threading tutorial
# ******************************************************
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time

def new_thread(func):
    def wrapper():
        print('wrapped func: {}'.format(func.__name__))
        print('new thread created')
        print(f'total count of thread are {threading.active_count()}\n')
        func()
    return wrapper

@new_thread
def eat_breakfast():
    time.sleep(3)
    print(f"You eat breakfast in {time.perf_counter()}")

@new_thread
def drink_coffee():
    time.sleep(4)
    print(f"You drunk cofee in {time.perf_counter()}")

@new_thread
def study():
    time.sleep(5)
    print(f"You finish studying in {time.perf_counter()}")

print(threading.active_count())
x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

# ******************************************************
