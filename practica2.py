# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:23:53 2022

@author: Ander Aramburu,Ahmed Fayze and Andres Malon
"""
import random,json

############### HANGMAN GAME ###############

with open('words.json') as f:
    words = f.read()
ctgs = json.loads(words)

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
    
    print_modify_options()
    
    
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
            
        print_category_options()

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
        

#####MODIFY WORDS#######
def modify_words():
    
    sellist = [1,2,3,4]
    modlist = sellist
    
    sel = print_category_options()
    while sel in sellist and sel != 4:
        
        if sel == 1:   
            add()
        
        if sel == 2:
            
            mod = print_modify_options()
            while mod in modlist and mod != 4:

                if mod == 1:
                    change_name(ctgs)
            
                if mod == 2:
                    add_word()
        
                if mod == 3:
                    remove_word()

                mod = print_modify_options()
            
            if mod not in modlist:
                sel_error()
            
        if sel == 3:
            delete_category()
            
        sel = print_category_options()
        
    if sel not in sellist:
        sel_error()
        
    return print_menu()
def Play():
    print ("Playing...\n ")
    print("Please choose one of the following options: \n")
    print("1 - The guessed word belongs to a certain category\n2 - Randomly from all bag of words\n")
    print("\n")
    selecplay=int(input("Your choose:"))
    if selecplay==1:
        print ("Categories: ",ctgs.keys())##Print all the categories
        category=input("Please introduce the category: ")#The user select a certain category
        categorylist=list(ctgs.keys())
        if category in categorylist:
            wordslist  = ctgs[category]#We get all values of the specific category
            wordnum = random.randint(0,len(wordslist)-1)
            word = wordslist[wordnum]#We obtain the word that we use for the game 
        else:
            print(ctgs[category])
            raise KeyError("This category is not exist")
                        
    else:
        #Random
        catnum = random.randint(0,len(ctgs)-1)
        wordnum = random.randint(0,len(list(ctgs[catnum]))-1)
        word = ctgs[catnum][wordnum]
    
    
    ##Program
    errors=0
    while errors<6:
        let=input("Please guess a letter or word:")
        if let in word:
            word=showletter(word,let)
            hangman(errors,word)
        else:
            errors+=1
            hangman(errors,let)

        
def hangman(cont,s):
    a = '---------'
    b = '|';c = '|';d = '|';e = '|';f = '|'
    g = '_'
    
    if cont >= 1:
        b = '|       |'
    if cont >= 2:
        c = '|       0'
    if cont >= 3:
        d = '|      \|/'
    if cont >= 4:
        e = '|       |'
    if cont >= 5:
        f = '|      / \\'
    
    print('%s\n%s\n%s\n%s\n%s\n%s\n%s\n\n%s\n'%(a,b,c,d,e,f,g,s)) 

def main():
    oplist=["1","2","3"]
    print_categories(ctgs)

    a = print_menu()
    if a not in oplist:
        print('\nWrong option!')
    else:
        while a in oplist:

            if a == "1":
                a = modify_words()
            if a == "2":
                a= Play()
            if a == "3":
                sys.exit("The program is finish")
        
if __name__ == "__main__":
    main()
     
        
