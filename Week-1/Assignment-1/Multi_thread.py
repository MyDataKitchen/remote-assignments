from threading import *
from time import sleep

def do_job(number): 
    sleep(3)
    print(f"Job {number} finished")
    # rewrite everything inside this main function and keep others untouched

def main(Thread):
    for i in range(5):
        do_job(i) 
        
t1 = main()
ti.start()