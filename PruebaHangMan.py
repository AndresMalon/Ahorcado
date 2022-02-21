# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:23:53 2022

@author: Ander Aramburu,Ahmed Fayze and Andres Malon
"""
import sys
import random
import random,json


############### HANGMAN GAME ###############
ctgs = {'transportation':["car", "truck", "scooter", "bicycle", "taxi", "train", "tram", "subway", "airplane", "van"],
            'food':["rice", "chicken", "pizza", "pasta", "salad", "porridge", "cake", "muffin", "tuna", "ham"],
            'cities':["Quebec City", "Los Angeles", "San Diego", "San Jose", "Ottawa", "Toronto", "Vancouver", "Edmonton", "Detroit", "Philadelphia", "Minneapolis"],
            'nationalities':["Canadian", "German", "French", "Italian", "Swedish", "Chinese", "Indian", "Spanish", "Argentinian", "Chilean"]}
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

# def hangman(cont,s):
    
#     a = '---------'
#     b = '|';c = '|';d = '|';e = '|';f = '|'
#     g = '_'
    
#     if cont >= 1:
#         b = '|       |'
#     if cont >= 2:
#         c = '|       0'
#     if cont >= 3:
#         d = '|      \|/'
#     if cont >= 4:
#         e = '|       |'
#     if cont >= 5:
#         f = '|      / \\'
    
#     print('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n'%(a,b,c,d,e,f,g,s))    

def Play():
    while True:
        
        print ("Playing...\n ")
        print("Please choose one of the following options: \n")
        print("1 - The guessed word belongs to a certain category\n2 - Randomly from all bag of words\n")
        print("\n")
        selecplay=int(input("Your choose:"))
        while selecplay not in [1,2]:
            selecplay = int(input("Please choose between 1 and 2: "))
            print("\n")
            
            
        if selecplay==1:
            print ("Categories: ",ctgs.keys())#Print all the categories
            category = input("Please introduce the category: ")#The user select a certain category
            categorylist=list(ctgs.keys())
            while category not in categorylist:
                print("This category is not exists\n ")
                category = input("Please introduce the category: ")
            if category in categorylist:
                wordslist  = ctgs[category]#We get all values of the specific category
                word = random.choice(wordslist)#We obtain the word that we use for the game
                
        else:
            #Random word from all the words of the diccinary
            wordslist = []
            for category in ctgs:
                for word in ctgs[category]:
                    wordslist.append(word)
            word = random.choice(wordslist)
            print (word)
        WORD=word
        word=word.lower()
        word=list(word)

        ##Program
        errors=0
        progress = []
        progress='_ '*len(word)
        print(progress)
        
        
        while '_' in progress and errors<5:
            letter=input('Please guess a letter or word: ')
                    
            if letter==''.join(word):
                progress=[]
            else:
                    # Here, we have made the program for changing the low lines by
                        # the correct letters 
                 if letter in word:
                     index=0
                     progress=list(progress)  
                     while index<len(word):
                         if word[index]==letter:
                             progress[index*2]=letter
                             index+=1
                         else:
                            errors+=1
                            print(letter,'is not correct. \n')
                            
                            first_error = '---------'
                            second_err = '|';third_err = '|';fourth_err = '|';fifth_err = '|';sixth_err = '|'
                            if errors >= 1:
                                second_err = '|       |'
                            if errors >= 2:
                                third_err = '|       0'
                            if errors >= 3:
                                fourth_err = '|      \|/'
                            if errors >= 4:
                                fifth_err = '|       |'
                            if errors >= 5:
                                sixth_err = '|      / \\'
                            
                            print('%s\n%s\n%s\n%s\n%s\n%s\n%s\n'%(first_error,second_err,third_err,fourth_err,fifth_err,sixth_err,letter))
                            
                            
                            
        if errors<6:
            print('You win. The word is',WORD,'.')
            print("\n")
            break
        else:
            print('Sorry, you ran out of tries. The word was',word,'. Maybe next time!')
            print("\n")
            break


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
     
        
