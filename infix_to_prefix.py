OPERATORS = ('+', '-', '*', '/', '(', ')', '^')  # set of operators

PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities


def infix_to_postfix(expression):
    stack = []
    output = ''
    for ch in expression:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    return output


def infix_to_prefix(expression):
    s = expression[::-1]
    s = [x for x in s]
    for i in range(len(s)):
        if s[i] == '(':
            s[i] = ')'
        elif s[i] == ')':
            s[i] = '('

    s = ''.join(s)

    return infix_to_postfix(s)[::-1]


expression = input('Enter infix expression')
print('infix expression: ', expression)

print('prefix expression: ', infix_to_prefix(expression))
