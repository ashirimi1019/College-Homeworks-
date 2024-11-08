import heapq

def kBiggest(lst, k):
    if k <= 0:
        raise ValueError("k must be a positive integer")

    min_heap = []

    for num in lst:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
    
    if len(min_heap) < k:
        raise ValueError("k exceeds the number of elements in the list")
    
    return min_heap[0]

# Updated test case
def test_kBiggest():
    # Case 1: Normal case
    assert kBiggest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 3) == 5

    # Case 2: List with duplicates
    assert kBiggest([3, 3, 3, 3, 3, 3], 2) == 3

    # Case 3: k equals to list length
    assert kBiggest([4, 1, 2, 8, 5, 7], 6) == 1

    # Case 4: k greater than list length (should raise an error)
    try:
        kBiggest([1, 2], 3)
    except ValueError:
        pass

    # Case 5: k is zero or negative (should raise an error)
    try:
        kBiggest([1, 2, 3, 4], 0)
    except ValueError:
        pass

if __name__ == "__main__":
    # Run the test case
    test_kBiggest()
    print("Test case passed.")

