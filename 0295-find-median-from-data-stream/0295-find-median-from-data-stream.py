import heapq

class MedianFinder:

    def __init__(self):
        self.left = []      # Max heap
        self.right = []     # Min heap

    def addNum(self, num):

        # Add to left first
        heapq.heappush(self.left, -num)

        # Move largest from left to right
        value = -heapq.heappop(self.left)
        heapq.heappush(self.right, value)

        # Balance the heaps
        if len(self.right) > len(self.left):
            value = heapq.heappop(self.right)
            heapq.heappush(self.left, -value)

    def findMedian(self):

        # Odd number of elements
        if len(self.left) > len(self.right):
            return -self.left[0]

        # Even number of elements
        return (-self.left[0] + self.right[0]) / 2


# Create object
obj = MedianFinder()

# Add numbers
obj.addNum(1)
obj.addNum(2)

# Find median
print("Median:", obj.findMedian())

# Add another number
obj.addNum(3)

# Find median again
print("Median:", obj.findMedian())