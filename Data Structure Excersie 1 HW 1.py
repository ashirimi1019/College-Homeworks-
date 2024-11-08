# Ashir Imran
# Date: 02/06/2024
def find_common_elements_brute_force(lst1, lst2):
    """
    Find common elements between two sorted lists using brute force method.
    
    Args:
    lst1 (list): The first sorted list.
    lst2 (list): The second sorted list.
    
    Returns:
    list: A list of common elements, duplicate-free.
    """
    common_elements = []  # Initialize an empty list to store common elements
    for element in lst1:  # Iterate through each element in the first list
        if element in lst2 and element not in common_elements:
            # Check if the element exists in the second list and not already in the common_elements list
            common_elements.append(element)  # Add the element to the common_elements list
    return common_elements  # Return the list of common elements


# Example usage
WST1 = [1, 5, 6, 6, 9, 9, 9, 11, 11, 21]
WST2 = [6, 6, 9, 11, 21, 21, 21]
print(find_common_elements_brute_force(WST1, WST2))

# Test Cases
# Test case 1: Null input case, so no output
# Test case 2: One of the lists is empty
# Test case 3: Both lists have no common elements
# Test case 4: All elements in both lists are common
# Test case 5: Lists with varying lengths
