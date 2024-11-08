#Name: Ashir
# Data Structure Excersie 2 Lab 1
def DeDuplication(input_list):
    # Find the maximum element in the input list
    max_element = max(input_list)
    
    # Initialize counting list with zeros
    counting_list = [0] * (max_element + 1)
    
    # Count the frequency for each element in the input list
    for element in input_list:
        counting_list[element] += 1
    
    # Generate the output list by iterating the counting list
    output_list = [num for num in range(len(counting_list)) if counting_list[num] != 0]
    
    return output_list

# Test the program with the given example and additional test cases
testcase1 = [50, 11, 33, 21, 40, 50, 40, 40, 21]
result1 = DeDuplication(testcase1)
print(f"Input: {testcase1}\nOutput: {result1}\n")

testcase2 = [5, 8, 2, 2, 8, 1, 5, 3]
result2 = DeDuplication(testcase2)
print(f"Input: {testcase2}\nOutput: {result2}\n")

testcase3 = [15, 10, 7, 15, 10, 5, 5, 7, 7]
result3 = DeDuplication(testcase3)
print(f"Input: {testcase3}\nOutput: {result3}")
