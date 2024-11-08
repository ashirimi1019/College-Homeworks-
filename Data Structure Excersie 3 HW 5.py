import heapq

def top_k_frequenting_heaping(nums, k):
    # Count the frequency of each number using a dictionary
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    # Use a heap to keep track of the top k elements
    # We want a min-heap so we will invert the frequency to sort from higher to lower
    heap = [(-freq, num) for num, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Extract the top k elements
    top_k = []
    for _ in range(k):
        top_k.append(heapq.heappop(heap)[1])
    
    return top_k

# Example usage:
nums = [1, 2, 1, 3, 2, 2]
k = 2
print(top_k_frequenting_heaping(nums, k))  # Output should be [2, 1]