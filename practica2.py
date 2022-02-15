# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:23:53 2022

@author: ander
"""
import sys

############### HANGMAN GAME ###############
ctgs = {'transportation':["car", "truck", "scooter", "bicycle", "taxi", "train", "tram", "subway", "airplane", "van"],
            'food':["rice", "chicken", "pizza", "pasta", "salad", "porridge", "cake", "muffin", "tuna", "ham"],
            'cities':["Quebec City", "Los Angeles", "San Diego", "San Jose", "Ottawa", "Toronto", "Vancouver", "Edmonton", "Detroit", "Philadelphia", "Minneapolis"],
            'nationalities':["Canadian", "German", "French", "Italian", "Swedish", "Chinese", "Indian", "Spanish", "Argentinian", "Chilean"]}

def intro():
    print("Welcome to the Hang Man Game!")
    
def print_menu():
    print("\nPlease choose one of the following options:")
    print("1 - Modify words\n2 - Play\n3 - Exit")
    a = input("You choose:")
    
    return a

def print_categories(s):
    print("\nCategories:", end = " ")
    for i in ctgs:
        print(i,end = " ")
    print("\n")
    
def print_category_options():
    print("\nPlease choose one of the following options: ")
    print("1 - Add category\n2 - Modify category\n3 - Delete category\n4 - Return to Main Menu")
    sel = int(input("Your selection: "))
    
    return sel

def print_modify_options():
    
    print("\nPlease choose one of the following options: ")
    print("1 - Change category name\n2 - Add a new Word\n3 - Remove a Word\n4 - Return to Main Menu")
    sel = int(input("Your selection: "))
    
    return sel

def sel_error():
    print("Error! Choose a correct number")
    
    return print_modify_options()
    
    
###ADD CATEGORY
def add():
        ctg = input("Please enter the new category name: ")
            
        if ctg not in ctgs:
            print("Well done, %s has been created"%ctg)
            ctgs[ctg] = []
            print_categories(ctgs)
        else:
            print("\nInvalid name, %s already exists in the catalogue"%ctg)
            print_categories(ctgs)
            
        return print_category_options()

###MODIFY CATEGORY
#name
def change_name(dic):
    n1=input('Please introduce the category name you want to change: ')
    
    if n1 not in dic:
        print('This category does not exist in the catalogue')
        print_categories(dic)
                
    else:
        n2=input('Now write the name you want for it: ')
        ctgs[n2] = ctgs[n1]
        del ctgs[n1]
        print_categories(dic)
        
    return print_modify_options()
        
#add word
def add_word():
    c = input('Please introduce the category to be updated: ')
    
    if c in ctgs:
        n = input('Add the new candidate word to the category: ')
        if n not in ctgs[c]:
            ctgs[c].append(n)
        else:
            print('\nError! That word already exists')
    else:
        print('\nError! That category does not exist in the catalogue')
        
    return print_modify_options()

#remove word
def remove_word():
    c = input('Please introduce the category to be updated: ')
    
    if c in ctgs:
        r = input('Write the word you want to remove: ')
        if r in ctgs[c]:
            ctgs[c].remove(r)
        else:
            print('\nError! That word is not in the category')
    else:
        print('\nError! That category does not exist in the catalogue')
        print_categories(ctgs)
        
    return print_modify_options()

###DELETE CATEGORY
def delete_category():
    c = input('Please introduce the category to be updated: ')
    
    if c in ctgs:
        if ctgs[c] == []:
            del ctgs[c]
            print_categories(ctgs)
        else:
            print('\nThis category is not empty. You should remove the words first')
            print_categories(ctgs)
    else:
        print('\nError! That category does not exist in the catalogue\n')
        print_categories(ctgs)
        
    return print_modify_options()

#####MODIFY WORDS#######
def modify_words():
    sel = print_category_options()
    
    while sel != 1 and sel != 2 and sel != 3 and sel != 4:
        sel_error()
        sel = print_category_options()
        
    while sel == 1:   
        sel = add()
        
    while sel == 2:
        mod = print_modify_options()
        
        while mod != 1 and mod != 2 and mod != 3 and mod != 4:
            mod = sel_error()
            
        while mod == 1:
            mod = change_name(ctgs)
            
        while mod == 2:
            mod = add_word()
        
        while mod == 3:
            mod = remove_word()
            
        sel = print_category_options()        
        
            
    while sel == 3:
        sel = delete_category()
        
    return print_menu()

def main():
    
    print_categories(ctgs)

    a = print_menu()

    while a != '1' and a != '2' and a != '3':
        print('\nWrong option!')
        a = print_menu()

    while a == '1':
        a = modify_words()

    if a == '3':
        sys.exit()
        
if __name__ == "__main__":
    main()
     
        
