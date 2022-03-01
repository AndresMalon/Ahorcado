import sys


class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False
    def add_front(self,item):
        self.items.append(item)
    def add_rear(self,item):
        self.items.insert(0,item)
    def remove_front(self):
        if self.is_empty():
            raise RuntimeError("Attempt to access front of emppty queue")            
        return self.items.pop()
    def remove_rear(self):
        if self.is_empty():
            raise RuntimeError("Attempt to access front of emppty queue")
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def print_queue(self):
        print(self.items)


def menu():
    d = Deque()
    op = int(input("1.Add to the front\n\n2.Add to the back\n\n3.Remove from the front\n\n"
               "4.Remove from the back\n\n5.Is deque empty?\n\n6.Size of Deque\n\n"
               "7.Display content of the Deque\n\n8.Exit\n"))
    
    options = [1,2,3,4,5,6,7,8]
    while op not in options:
        print("Error! Please write a correct number!")
        op = int(input("1.Add to the front\n\n2.Add to the back\n\n3.Remove from the front\n\n"
               "4.Remove from the back\n\n5.Is deque empty?\n\n6.Size of Deque\n\n"
               "7.Display content of the Deque\n\n8.Exit\n"))
    while op in options:
        if op == 1:
            s = input("Write the character: ")
            d.add_front(s)
        elif op == 2:
            s = input("Write the character: ")
            d.add_rear(s)
        elif op == 3:
            d.remove_front()
        elif op == 4:
            d.remove_rear()
        elif op == 5:
            print(d.is_empty())
        elif op == 6:
            print(d.size())
        elif op == 7:
            d.print_queue()
        elif op == 8:
            sys.exit(1)
        op = int(input("1.Add to the front\n\n2.Add to the back\n\n3.Remove from the front\n\n"
               "4.Remove from the back\n\n5.Is deque empty?\n\n6.Size of Deque\n\n"
               "7.Display content of the Deque\n\n8.Exit\n"))
