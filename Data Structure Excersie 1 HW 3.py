def hasBalanceParentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:
            return False  # Invalid character

    return not stack

input_string = "([]{})"
print(hasBalanceParentheses(input_string))

#Time Complexity: O(n), where n is the length of the string.
#Space Complexity: O(n) for the stack in the worst case.