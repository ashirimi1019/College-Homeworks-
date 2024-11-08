def evaluatepostfixexpressions(tokens):
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(int(left / right))  # Floor division for integer result

    return stack[0]

tokens = ["10", "2", "*", "15", "+"]
print(evaluatepostfixexpressions(tokens))

# Time Complexity: O(n), where n is the number of tokens.
# Space Complexity: O(n) for the stack in the worst case.