# T: O(n)  S: O(n)
def isValid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in pairs:                        # closing bracket
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
        else:
            stack.append(c)                   # opening bracket

    return not stack   # stack must be empty at end