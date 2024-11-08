def custom_counting_sort(input_list):
    max_value = max(input_list)
    count_array = [0] * (max_value + 1)

    for num in input_list:
        count_array[num] += 1

    sorted_list = [value for value, count in enumerate(count_array) for _ in range(count)]

    return sorted_list

# Test the function
test_list = [50, 11, 33, 21, 40, 50, 40, 40, 21]
sorted_list = custom_counting_sort(test_list)
print("Sorted List:", sorted_list)

