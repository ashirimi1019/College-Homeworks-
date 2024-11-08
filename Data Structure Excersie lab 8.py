# Ashir Imran
# 3/3/2024

from collections import deque

class MaxQueued:
    def __init__(self):
        self.main_queue = deque()
        self.max_queue = deque()

    def enqueued(self, value):
        # Add the new value to the end of the main queue
        self.main_queue.append(value)

        # Remove elements from the back of the max queue if they are less than the new value
        # This ensures that the max queue is always ordered with the maximum element at the front
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()

        # Add the new value to the max queue
        self.max_queue.append(value)

    def dequeued(self):
        # Remove the element from the front of the main queue
        if self.main_queue:
            value = self.main_queue.popleft()

            # If the removed element is the same as the front of the max queue, also remove it from the max queue
            if value == self.max_queue[0]:
                self.max_queue.popleft()
            return value
        return None

    def get_maxed(self):
        # Return the front element of the max queue (maximum element of the main queue)
        if self.max_queue:
            return self.max_queue[0]
        return None

# Test Cases
# 1. Enqueue and get_max: Enqueue elements and verify get_max returns the correct maximum value.
# 2. Dequeue and get_max: Dequeue elements and verify get_max updates correctly.
# 3. Enqueue elements in decreasing order and verify get_max.
# 4. Enqueue elements in increasing order and verify get_max.
# 5. Dequeue until empty and verify get_max returns None.

mq = MaxQueued()
mq.enqueued(1)
assert mq.get_maxed() == 1, "Test 1 Failed: Expected max 1, got {}".format(mq.get_maxed())
mq.enqueued(4)
assert mq.get_maxed() == 4, "Test 2 Failed: Expected max 4, got {}".format(mq.get_maxed())
mq.enqueued(2)
assert mq.get_maxed() == 4, "Test 3 Failed: Expected max 4, got {}".format(mq.get_maxed())
mq.dequeued()
assert mq.get_maxed() == 4, "Test 4 Failed: Expected max 4, got {}".format(mq.get_maxed())
mq.dequeued()
assert mq.get_maxed() == 2, "Test 5 Failed: Expected max 2, got {}".format(mq.get_maxed())
print("All tests passed.")
