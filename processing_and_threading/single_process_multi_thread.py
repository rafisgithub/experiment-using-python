import os
import threading
import time


def task(name: str, seconds: int) -> None:
    thread_name = threading.current_thread().name
    print(f"[{os.getpid()}:{thread_name}] {name} started")
    time.sleep(seconds)
    print(f"[{os.getpid()}:{thread_name}] {name} finished")


if __name__ == "__main__":
    start = time.perf_counter()

    t1 = threading.Thread(target=task, args=("Task-1", 2), name="Worker-1")
    t2 = threading.Thread(target=task, args=("Task-2", 1), name="Worker-2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds")
