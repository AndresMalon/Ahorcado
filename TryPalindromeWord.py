#TryPalindromeWord
import TryDeque.py as TD
       

word=input("Introduce a word to be checked: ")

def check_Palindrome(word):
    chars=list(word)
    D=TD.Deque()
    for letter in chars:
        D.add_front(letter.upper())
    
    check=True
    print()
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