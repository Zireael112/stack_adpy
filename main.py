class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def all_list(self):
        return self.stack

    def delete_by_value(self, value):
        self.stack.remove(value)

# unit = Stack()
# unit.push('z')
# unit.push('x')
# unit.push('c')
# print(unit.size())
# print(unit.peek())
# print(unit.pop())
# print(unit.isEmpty())
# print(unit.pop())
# print(unit.pop())
# print(unit.isEmpty())


def pair_checker(value):
    examp = Stack()
    balanced = True
    index = 0
    while index < len(value) and balanced:
        ind = value[index]
        if ind == '(' or ind == '[' or ind == '{':
            examp.push(ind)
        else:
            if examp.isEmpty():
                balanced = False
            else:
                if '(' in examp.all_list() and ind == ')':
                    examp.delete_by_value('(')
                elif '[' in examp.all_list() and ind == ']':
                    examp.delete_by_value('[')
                elif '{' in examp.all_list() and ind == '}':
                    examp.delete_by_value('{')
                else:
                    balanced = False


        index += 1

    if balanced and examp.isEmpty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


print(pair_checker('(((([{}]))))'))
print(pair_checker('[([])((([[[]]])))]{()}'))
print(pair_checker('{{[()]}}'))
print(pair_checker('}{}'))
print(pair_checker('{{[(])]}}'))
print(pair_checker('[[{())}]'))


