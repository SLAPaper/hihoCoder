from __future__ import print_function, division, absolute_import, unicode_literals

while True:
    formula = raw_input()
    if formula == 'END':
        break
    else:
        # get raw_input and do all the calculation
        import re

        def add(a, b):
            return a + b

        def minus(a, b):
            return a - b

        def multiply(a, b):
            return a * b

        def divide(a, b):
            return int(a / b)

        op_func = {'+': add, '-': minus, '*': multiply, '/': divide}

        op_prior = {'+': 0, '-': 0, '*': 1, '/': 1}

        ops_re = "([-+*/()])"  # use parentheses so that ops won't be removed after split
        tokens = [
            t for t in (x.strip() for x in re.split(ops_re, formula))
            if len(t) > 0
        ]

        num_stack = []
        op_stack = []

        def process(op, num_stack=num_stack,
                    op_func=op_func):  # go with one operator
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            num_stack.append(op_func[op](num1, num2))

        def process_token(token, op_stack=op_stack):
            if not op_stack:
                op_stack.append(token)
            else:
                op = op_stack.pop()
                if op == '(' or op_prior[token] > op_prior[op]:
                    op_stack.append(op)
                    op_stack.append(token)
                else:
                    process(op)
                    process_token(token)

        for token in tokens:
            try:
                number = int(token)
                num_stack.append(number)
            except ValueError:  # here is operators
                if token == '(':
                    op_stack.append(token)
                elif token == ')':  # calc until the matching left param
                    op = op_stack.pop()
                    while op != '(':
                        process(op)
                        op = op_stack.pop()
                else:  # normal +, -, * and /
                    process_token(token)

        while op_stack:
            op = op_stack.pop()
            process(op)

        print(num_stack[-1])
