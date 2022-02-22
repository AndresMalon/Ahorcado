# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:14:27 2022

@author: Andres.Malon
"""
import sys
class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop (self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty stack")
        topIdx = len(self.items)-1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item
    def top(self):
        if self.isEmpty():
                raise RuntimeError("Attempt to pop an empty stack")
        topIdx = len(self.items)-1
        item = self.items[topIdx]
        return item
    
    def isEmpty (self):
        return len(self.items) == 0
    
def Check_balance(a):
    s=Stack()
    check={')':'(', ']':'[', '}':'{'}
    for i in range(0,len(a)):
        if a[i]=='(' or a[i]=='[' or a[i]=='{':
            s.push(a[i])
        elif a[i]==')' or a[i]=='}' or a[i]==']':
            if check[a[i]]==s.pop():
                print()
            else:
                print('Not balanced')
                sys.exit(0)
    if  s.isEmpty():
        print('Balanced')
    else:
        print('Not balanced')







