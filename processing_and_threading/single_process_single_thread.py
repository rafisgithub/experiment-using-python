import os
import time


def task(name: str, seconds: int) -> None:
    print(f"[{os.getpid()}] {name} started")
    time.sleep(seconds)
    print(f"[{os.getpid()}] {name} finished")


if __name__ == "__main__":
    start = time.perf_counter()

    # Same process and same main thread: tasks run one after another.
    task("Task-1", 2)
    task("Task-2", 1)

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds")
