# Ashir Imran
# Date: 02/06/2024
"""
We can optimize the process by employing a single loop that traverses both lists simultaneously. 
Given that the lists are sorted, we compare the elements of both lists at the same index. 
If they match, we add that element to a new list and advance both pointers. 
If the element in 'lst1' is greater than that in 'lst2', we only move the pointer for 'lst2' 
to compare the next element in 'lst2' with the current element in 'lst1'. 
Conversely, if the element in 'lst2' is greater, we only move the pointer for 'lst1'. 
Since we only iterate through both lists once, without nesting, 
the time complexity is O(m + n), where m and n are the lengths of the respective lists.
"""
