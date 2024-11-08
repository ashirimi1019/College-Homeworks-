from typing import Optional

class MinStack:
    def __init__(self):
       
        self.mainStack = []  
        self.minStack = []   

    def push(self, val: int) -> None:
       
        self.mainStack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
       
        if self.mainStack:
            val = self.mainStack.pop()
            if val == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> Optional[int]:
       
        return self.mainStack[-1] if self.mainStack else None

    def getMin(self) -> Optional[int]:
        
        return self.minStack[-1] if self.minStack else None

# Test Cases
#Push elements in ascending order and check if getMin() always returns the first pushed element.
#Push elements in descending order and check if getMin() always returns the last pushed element.
#Push a series of elements and pop them one by one, verifying if getMin() returns the accurate minimum after each pop.
#Push identical elements and ensure getMin() and pop() behave correctly.
#Verify edge cases by testing with an empty stack for both top() and getMin().

