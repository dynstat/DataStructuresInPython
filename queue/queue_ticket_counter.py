# TODO: Implement practical ticket counter.
# DONE 1. Create 3 queues.
# DONE 2. randomly add or remove users from any queues.
# DONE 3. Display the vacant spaces in 3 queues in every 10 seconds

# -----------------------------------------


import random as rnd
import threading
from time import sleep
import uuid

# Queue implementation in Python
class Queue:
    def __init__(self, q_name: str, max_size: int):
        self.name = q_name
        self.queue = []
        self.max_size = max_size

    # Add an element
    def enqueue(self, item):
        if len(self.queue) < self.max_size:
            self.queue.append(item)
            # self.display()
        else:
            # print("The queue is possibly Full")
            pass
            # pass

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def max_size(self):
        return len(self.queue)

    def display_vacant(self):
        vc = self.max_size - len(self.queue)
        print(f"vacant spaces in {self.name} are = {vc}")
        return vc


# this function will add and remove random number of users in the given queue
def rndm_add_rem_users(q: Queue):
    while True:
        sleep(3)
        arb_value = rnd.randint(1, q.max_size)
        for _ in range(arb_value):
            q.enqueue(uuid.uuid4().hex[:4])
        arb_value = rnd.randint(1, q.max_size - 5)
        for _ in range(arb_value):
            q.dequeue()


if __name__ == "__main__":
    q_1 = Queue("q_one", 10)
    q_2 = Queue("q_two", 10)
    q_3 = Queue("q_three", 10)
    tq1 = threading.Thread(target=rndm_add_rem_users, args=(q_1,), daemon=True)
    tq2 = threading.Thread(target=rndm_add_rem_users, args=(q_2,), daemon=True)
    tq3 = threading.Thread(target=rndm_add_rem_users, args=(q_3,), daemon=True)

    tq1.start()
    tq2.start()
    tq3.start()

    i = 25
    while i:
        sleep(8)
        i -= 1
        q_1.display_vacant()
        q_2.display_vacant()
        q_3.display_vacant()
        print("")
        print("")
        print("")
