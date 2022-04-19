import time 
import threading 
import queue

job_queue = queue.Queue()
for job_index in range(1, 10): # We create 9 jobs with job_index 1 ~ 9
    job_queue.put(job_index)

class Worker(threading.Thread): 
    def __init__(self, worker_num):
        threading.Thread.__init__(self) 
        self.worker_num = worker_num

    def run(self):
        while(True):
            if not job_queue.empty():
                job = job_queue.get()
                self.do_job(job)
            else:
                break

        # Your code here

    def do_job(self, index):

        # Simulate a job (you can image it as doing something which need to take 1 second)
        print(f"worker {self.worker_num} start job {index}") 
        time.sleep(1)
        print(f"worker {self.worker_num} finish job {index}")

workers = []
worker_count = 3 # We have 3 workers 
for i in range(worker_count):
    worker = Worker(i+1) 
    workers.append(worker)
# Do the job
for worker in workers: 
    worker.start()

for worker in workers: 
    worker.join()

print("Done.")