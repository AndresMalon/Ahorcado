# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:14:27 2022

@author: Andres.Malon
"""
class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append()
    def pop (self,item):
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
        return self.items[topIdx]
    
    def isEmpty (self):
        return len(self.items) == 0








