from typing import Optional, List, Union

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


def get_value(node: Union['OperationNode', int]):
    return node if isinstance(node, int) else node.get_value()


class OperationNode:
    expression: str
    level: int
    operation: List[str]
    value: Optional[int]
    left: Optional['OperationNode']
    right: List['OperationNode']

    def __init__(self, expression: str):
        self.expression = expression
        self.operation = []
        self.right = []
        self.value = None
        self.decode_expression(expression)

    def decode_expression(self, expression):
        if len(expression) == 1:
            self.value = int(expression[0])
        else:
            left = get_expression(expression)
            self.left = OperationNode(trim_expression(left))
            next = len(left)
            while next < len(expression):
                if expression[next] == '(':
                    self.operation.append('*')
                else:
                    self.operation.append(expression[next])
                    next += 1

                right = get_expression(expression[next:])
                right_node = OperationNode(trim_expression(right))
                self.right.append(right_node)
                next += len(right)

    def get_value(self) -> int:
        if self.value:
            return self.value
        else:
            expression = [self.left, *[x for pair in zip(self.operation, self.right) for x in pair]]

            while len(expression) > 1:
                if '+' in expression:
                    index = expression.index('+')
                    expression[index+1] = get_value(expression[index-1]) + get_value(expression[index+1])
                    expression = expression[:index-1] + expression[index+1:]
                else:
                    expression[2] = get_value(expression[0]) * get_value(expression[2])
                    expression = expression[2:]

            return expression[0]


print(sum([OperationNode(line).get_value() for line in lines]))

