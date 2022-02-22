# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:51:50 2022

@author: Andres.Malon
"""
import os
import sys
##Menu 
def print_Menu():
    print("\tChoose an option:\n1-->Check parenthesis balancing\n2-->Check balance of parentheses (select file)\n3-->Exit")
    selection = int(input(""))
    return selection
#Option 1 
def check_Balance_Text_Screen():
    expresion=input("Please enter the text to check: ")
    return expresion
#Option 2
def check_Balance_Text_File():
    ruta=input("Introduce the path of the file: ")
#Option 3 Exit
def main():
    selec = print_Menu()
    if selec == 1:
        check_Balance_Text_Screen()
    if selec == 2:
        check_Balance_Text_File()
    if selec == 3:
        sys.exit(1)
if __name__ == "__main__":
    main()
    
    
