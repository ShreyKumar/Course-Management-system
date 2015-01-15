class EmptyStackError(Exception):
    """Exception used when calling pop on empty stack."""
    pass 


class Stack:

    def __init__(self):
        """ (Stack) -> NoneType """
        self.items = []

    def is_empty(self):
        """ (Stack) -> bool """
        return len(self.items) == 0

    def push(self, item):
        """ (Stack, object) -> NoneType """
        self.items.append(item)
        return None

    def pop(self):
        """ (Stack) -> object """
        try:
            return self.items.pop()
        except IndexError:
            raise EmptyStackError
