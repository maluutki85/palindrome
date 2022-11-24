def chcek_palindrome(x):
    if (x == x[::-1]):
        return True
    else:
        return False
x = input("Wprowdź słowo:")
print(chcek_palindrome(x))

'''
Program pozwalający sprawdzić czy wyraz
jest palindromem. Fukncja składa się 
z jednego argumentu, który podawany 
jest przez input
'''