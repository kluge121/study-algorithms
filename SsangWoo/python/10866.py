# deque

class Deque:
    def __init__(self, list=None):
        if list is None:
            list = []
        self.deque = list

    def push_front(self, x):
        self.deque.insert(0, x)

    def push_back(self, x):
        self.deque.append(x)

    def pop_front(self):
        if self.empty() == 0:
            return self.deque.pop(0)
        else:
            return -1

    def pop_back(self):
        if self.empty() == 0:
            return self.deque.pop(-1)
        else:
            return -1

    def size(self):
        return len(self.deque)

    def empty(self):
        return 1 if len(self.deque) < 1 else 0

    def front(self):
        return self.deque[0] if self.empty() == 0 else -1

    def back(self):
        return self.deque[-1] if self.empty() == 0 else -1

deque = Deque()
for _ in range(int(input())):
    command = input()
    value = 0
    if ' ' in command:
        command, value = command.split()
        value = int(value)
    if command == 'push_front':
        deque.push_front(value)
    elif command == 'push_back':
        deque.push_back(value)
    elif command == 'pop_front':
        print(deque.pop_front())
    elif command == 'pop_back':
        print(deque.pop_back())
    elif command == 'size':
        print(deque.size())
    elif command == 'empty':
        print(deque.empty())
    elif command == 'front':
        print(deque.front())
    elif command == 'back':
        print(deque.back())

