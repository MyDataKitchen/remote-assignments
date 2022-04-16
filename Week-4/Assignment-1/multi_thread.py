import threading
from time import *

def do_job(number): 
    sleep(3)
    print(f"Job {number} finished")
    # rewrite everything inside this main function and keep others untouched

def main():
    for i in range(5):
        t1 = threading.Thread(target=do_job, args=(i,))
        t1.start()
          
main()