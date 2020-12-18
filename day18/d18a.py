from typing import Optional, List

lines = [n.strip().replace(' ', '') for n in open('d18in.txt').read().splitlines()]


def get_expression(string: str) -> str:
    if string[0].isdigit():
        return string[0]
    else:
        level, ptr = 1, 0
        while level > 0:
            ptr += 1
            level += 1 if string[ptr] == '(' else -1 if string[ptr] == ')' else 0
        return string[0: ptr+1]


def trim_expression(exp: str) -> str:
    return exp[1:-1] if exp[0] == '(' and exp[-1] == ')' else exp


class OperationNode:
    expression: str
    level: int
    operation: List[str]
    value: Optional[int]
    left: Optional['OperationNode']
    right: List['OperationNode']

    def __init__(self, expression: str, level: int = 0):
        self.expression = expression
        self.level = level
        self.operation = []
        self.right = []
        self.value = None
        self.decode_expression(expression)

    def decode_expression(self, expression):
        if len(expression) == 1:
            self.value = int(expression[0])
        else:
            left = get_expression(expression)
            self.left = OperationNode(trim_expression(left), self.level+1)
            next = len(left)
            while next < len(expression):
                if expression[next] == '(':
                    self.operation.append('*')
                else:
                    self.operation.append(expression[next])
                    next += 1

                right = get_expression(expression[next:])
                right_node = OperationNode(trim_expression(right), self.level+1)
                self.right.append(right_node)
                next += len(right)

    def get_value(self) -> int:
        if self.value:
            value = self.value
        else:
            expression = [self.left, *zip(self.operation, self.right)]

            while len(expression) > 1:
                if '+' in expression:
                    index = e


        return value


print(sum([OperationNode(line).get_value() for line in lines]))

