#1
class Queue:
    def __init__(self):
        self.items = []

    def insert(self, value):
        """Insert value at the rear"""
        self.items.append(value)

    def pop(self):
        """Remove from the front"""
        if self.is_empty():
            print("Warning: Queue is empty!")
            return None
        return self.items.pop(0)

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0


#2
import pickle

class QueueOutOfRangeException(Exception):
    """Custom exception for queue overflow"""
    pass


class NamedQueue:
    _queues = {} 

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.items = []
        NamedQueue._queues[name] = self

    def insert(self, value):
        if len(self.items) >= self.size:
            raise QueueOutOfRangeException(
                f"Queue '{self.name}' exceeded max size {self.size}"
            )
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print(f"Warning: Queue '{self.name}' is empty!")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    @classmethod
    def get_queue(cls, name):
        """Retrieve queue instance by name"""
        return cls._queues.get(name)

    @classmethod
    def save(cls, filename="queues.pkl"):
        """Save all queues to file"""
        with open(filename, "wb") as f:
            pickle.dump(cls._queues, f)

    @classmethod
    def load(cls, filename="queues.pkl"):
        """Load queues from file"""
        with open(filename, "rb") as f:
            cls._queues = pickle.load(f)
        return cls._queues



#ex
if __name__ == "__main__":
    print("=== Basic Queue Example ===")
    q = Queue()
    q.insert(10)
    q.insert(20)
    print(q.pop())   #10
    print(q.pop())   #20
    print(q.pop())   #None

    print("\n=== Named Queue Example ===")
    try:
        q1 = NamedQueue("queue1", 2)
        q1.insert(1)
        q1.insert(2)
        # q1.insert(3) 

        q2 = NamedQueue("queue2", 3)
        q2.insert(5)

        # Save queues
        NamedQueue.save()

        # Load queues
        loaded = NamedQueue.load()
        print("Loaded Queues:", list(loaded.keys()))

        # Access by name
        q_loaded = NamedQueue.get_queue("queue1")
        print("Queue1 items:", q_loaded.items)

    except QueueOutOfRangeException as e:
        print("Custom Error:", e)
