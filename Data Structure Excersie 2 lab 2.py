#Name: Ashir
# Data Structure Excersie 2 Lab 2
def BinarySearch(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    checks = 0

    while low <= high:
        mid = (low + high) // 2
        checks += 1

        if sorted_list[mid] == target:
            return f"Found {target} in {checks} checks."
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return "Fail to find the input number..."

# Example usage with the provided example and additional test cases
sorted_list_example = [11, 21, 33, 40, 50]

# Testcase 1: Search for 33
target1 = int(input("Enter an integer to search: "))
result1 = BinarySearch(sorted_list_example, target1)
print(result1)

# Testcase 2: Search for 25
target2 = int(input("Enter an integer to search: "))
result2 = BinarySearch(sorted_list_example, target2)
print(result2)

# Testcase 3: Search for 50
target3 = int(input("Enter an integer to search: "))
result3 = BinarySearch(sorted_list_example, target3)
print(result3)
