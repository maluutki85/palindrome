def check_palindrome(x):
    return x == x[::-1]
x = input("Wprowadź słowo:")    
print(check_palindrome(x))

'''
Program pozwalający sprawdzić czy wyraz
jest palindromem. Fukncja składa się 
z jednego argumentu, który podawany 
jest przez input
'''