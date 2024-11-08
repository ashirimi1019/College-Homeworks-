# Ashir Imran
# CSc 2720 Homework #5
# Due time: 04/23/2024

def top_k_frequenting_sort(nums, k):
    # Count the frequency of each number using a dictionary
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Create a list of tuples (number, frequency) and sort it by frequency
    freq_list = [(num, freq) for num, freq in frequency.items()]
    freq_list.sort(key=lambda x: x[1], reverse=True)
    
    # Extract the top k elements
    top_k = [num for num, freq in freq_list[:k]]
    return top_k

# Example usage:
nums = [1, 2, 1, 3, 2, 2]
k = 2
print(top_k_frequenting_sort(nums, k))  # Output should be [2, 1]