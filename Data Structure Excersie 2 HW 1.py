# Ashir Imran
# Date: 02/06/2024
def find_common_elements_binary_search(lst1, lst2):
    # Checking if either of the lists is empty
    if len(lst1) == 0 or len(lst2) == 0:
        print("At least one of the lists is empty.")
        return []

    else:
        common_elements = []  # Initialize an empty list to store common elements

        # Iterate over elements in the first list
        for element in lst1:
            lowest_index = 0
            highest_index = len(lst2) - 1

            # Binary search to find the element in lst2
            while highest_index >= lowest_index:
                middle_index = (highest_index + lowest_index) // 2

                # If the element is found in lst2 and not already in the common_elements list, append it
                if lst2[middle_index] == element:
                    if element not in common_elements:
                        common_elements.append(element)
                    break
                
                # Adjust the boundaries of the search if the elements are not equal
                elif lst2[middle_index] < element:
                    lowest_index = middle_index + 1
                else:
                    highest_index = middle_index - 1

        if not common_elements:
            print("No common elements found.")
        else:
            print("Common elements found:", common_elements)  # Print the list containing common elements
        
        return common_elements  # Return the final list containing common elements

# Example lists
list1 = [1, 5, 6, 6, 9, 9, 9, 11, 11, 21]
list2 = [6, 6, 9, 11, 21, 21, 21]

# Call the function with the example lists
find_common_elements_binary_search(list1, list2)

