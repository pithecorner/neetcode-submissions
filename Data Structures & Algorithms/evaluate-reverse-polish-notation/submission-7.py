class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        for i in tokens:
            if i == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(i))
        return stack[0]