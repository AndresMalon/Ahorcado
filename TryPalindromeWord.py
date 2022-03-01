#TryPalindromeWord
from TryDeque import Deque
from Stack import Stack 

word=input("Introduce a word to be checked: ")
'''def Check_balance(a):
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
        return True
    else:
        return False'''

def check_Palindrome(word):
    chars=list(word)
    D=Deque()
    for letter in chars:
        D.add_front(letter.upper())
    
    check=True
    while D.size()>1 and check:
        if D.items[0]!=D.items[-1]:
            print('The word isn´t palindromic')
            check=False
            break     
        D.remove_rear()
        D.remove_front()
    if check:
        print('The word is palindromic')

check_Palindrome(word)
