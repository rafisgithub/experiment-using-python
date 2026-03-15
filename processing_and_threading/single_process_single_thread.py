import threading

def task1():
    print("Task 1 is starting")
    for i in range(50000):
        print(f"Task 1 is running iteration {i}")
    print("Task 1 is completed")


def task2():
    print("Task 2 is starting")
    for i in range(5000):
        print(f"Task 2 is running iteration {i}")
    print("Task 2 is completed")

# use thread

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task1)

t1.start()
t2.start()
