import time
import threading
import os

def cpu_spike(duration_sec, cpu_percent):
    num_threads = os.cpu_count()
    busy_time = cpu_percent / 100.0
    idle_time = 1 - busy_time

    def _burn():
        while True:
            start = time.time()
            # Busy loop
            while (time.time() - start) < busy_time:
                pass
            # Sleep for the idle time
            time.sleep(idle_time)

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=_burn)
        t.daemon = True
        t.start()
        threads.append(t)
    time.sleep(duration_sec)

if __name__ == "__main__":
    while True:
        print("Spiking CPU to 80% for 30 seconds...")
        cpu_spike(30, 80)  # 80% for 30 seconds
        print("Sleeping for 90 seconds...")
        time.sleep(90)     # Sleep for the rest of the 2 minutes
