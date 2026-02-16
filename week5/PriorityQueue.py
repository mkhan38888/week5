from Task import Task

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index].priority > self.heap[parent].priority:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left

            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_task = self.heap.pop()

        # Only heapify down if heap is not empty
        if not self.is_empty():
            self._heapify_down(0)

        return max_task


pq = PriorityQueue()

pq.insert(Task("A", 5, 0))
pq.insert(Task("B", 2, 1))
pq.insert(Task("C", 8, 2))

while not pq.is_empty():
    print("Executing:", pq.extract_max())
