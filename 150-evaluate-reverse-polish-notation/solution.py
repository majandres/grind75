# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        """You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

        Evaluate the expression. Return an integer that represents the value of the expression.

        The division between two integers always truncates toward zero.
        """
        
        stack = []
        operators = ["+", "-", "*", "/"]

        for t in tokens:
            if t in operators:
                result = self.operate(stack.pop(), stack.pop(),t )
                stack.append(result)
            else:
                stack.append(int(t))
        
        print(f"DEBUG: len of stack: {len(stack)}")
        return(stack.pop())
        

    def operate(self, val1, val2, operator):
        if operator == "+":
            return val2 + val1
        if operator == "-":
            return val2 - val1
        if operator == "*":
            return val2 * val1
        if operator == "/":
            return int(val2 / val1)


s = Solution()

print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["4","13","5","/","+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))