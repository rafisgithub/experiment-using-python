import multiprocessing as mp
import os
import threading
import time


def thread_task(label: str, seconds: int) -> None:
    thread_name = threading.current_thread().name
    print(f"[{os.getpid()}:{thread_name}] {label} started")
    time.sleep(seconds)
    print(f"[{os.getpid()}:{thread_name}] {label} finished")


def process_worker(process_name: str) -> None:
    print(f"[{os.getpid()}] {process_name} started")

    t1 = threading.Thread(target=thread_task, args=(f"{process_name}-Task-1", 2), name="Thread-1")
    t2 = threading.Thread(target=thread_task, args=(f"{process_name}-Task-2", 1), name="Thread-2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"[{os.getpid()}] {process_name} finished")


if __name__ == "__main__":
    start = time.perf_counter()

    p1 = mp.Process(target=process_worker, args=("Process-1",))
    p2 = mp.Process(target=process_worker, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds")
