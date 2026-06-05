class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        for i in tokens:
            if not i.lstrip('-').isnumeric():
                a, b = stack.pop(), stack.pop()
                stack.append(int(eval("{2}{1}{0}".format(a, i, b))))
            else:
                stack.append(int(i))
        return stack[0]