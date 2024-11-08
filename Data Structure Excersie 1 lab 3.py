def custom_bubble_sort(input_list):
    length = len(input_list)
    is_sorted = False
    
    while not is_sorted:
        is_sorted = True
        
        for i in range(1, length):
            if input_list[i - 1] > input_list[i]:
                input_list[i - 1], input_list[i] = input_list[i], input_list[i - 1]
                is_sorted = False
                
    return input_list

# Test the function
test_list = [50, 11, 33, 21, 40, 50, 40, 40, 21]
sorted_list = custom_bubble_sort(test_list)
print("Sorted List:", sorted_list)

