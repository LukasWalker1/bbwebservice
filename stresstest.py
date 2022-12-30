import requests
from multiprocessing import Process, Value
import time

processes = []
success = Value('i',0)
tested = Value('i',0)
to_test = 1000

def testing():
    global tested,to_test
    while tested.value < to_test:
        test()

def test():
    global success,tested
    response = requests.get('http://192.168.0.32:5000/')
    if response.status_code == 200:
        success.value += 1
    tested.value += 1
    print(tested.value)


if __name__ == "__main__":
    t1 = time.time()
    for i in range(5):
        p = Process(target= testing)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    t2 = time.time()

    print(f'{success.value}/{tested.value} {t2-t1}s')