def isValidParentheses(self, s):
    new_s = list(s)
    stack = []
    for c in new_s:
        if c == '(':
            stack.append(')')
        elif c == '{':
            stack.append('}')
        elif c == '[':
            stack.append(']')
        elif len(stack) == 0 or c != stack.pop():
            return False
    return not stack
