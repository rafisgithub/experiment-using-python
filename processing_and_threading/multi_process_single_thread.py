import multiprocessing as mp
import os
import time


def cpu_task(name: str, n: int) -> None:
    print(f"[{os.getpid()}] {name} started")
    total = 0
    for i in range(n):
        total += i * i
    print(f"[{os.getpid()}] {name} finished with total={total}")


if __name__ == "__main__":
    start = time.perf_counter()

    p1 = mp.Process(target=cpu_task, args=("Process-1", 700000))
    p2 = mp.Process(target=cpu_task, args=("Process-2", 700000))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds")
