#1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.
def unique(lst1):
    a=set()
    for i in range(len(lst1)):
        a.add(lst1[i])
    print("list's unique elements:-",a)

lst1=(input("Enter some number in list. with coma shepareted:- "))
lst2=lst1.split(',')
unique(lst2)
#2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.
def prime(a):
    for i in range(2,a):
        if a%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")    

a=int(input("Enter a  number to check prime or not="))
prime(a)
#3. Write a python program to create a function that prints the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even(lst):
    [print("Even numbers from a given list",x) for x in lst if x%2==0]

Sample_List=[1, 2, 3, 4, 5, 6, 7, 8, 9]
even(Sample_List)
#4. Write a python program to create a function that checks whether a passed string is palindrome or not
def palindrome(a):
    [print("Palindrome") if a == a[::-1] else print("Not Palindrome")]
a=input("Enter a string=")
palindrome(a)

#5. Write a python program to create a function to find the Min of three numbers.
def Min(a,b,c):
    d=min(a,b,c)
    return d

print("Enter three number using space=")
a,b,c=input().split(" ")
print("Min of three numbers:-",Min(a,b,c))   
#6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.
def square():
    l=[]
    for i in range(1,30+1,1):
        l.append(i**2)
    print(l)

square()    
#7. Write a python program to access a function inside a function.
def test(a):
        def add(b):
                nonlocal a
                a += 1
                return a+b
        return add
func= test(4)
print(func(4))
#8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.
def string(n):
    c,d=0,0
    for m in n:
        if m.islower(): #(or)if m==m.lower():
            c+=1
        else:
            d+=1
    print("upper",d)
    print("lower",c)        
string(input("Enter a string:-")) 
#9. Write a python program to create a function to check whether a string is a pangram or not.
#import string
def pangram(string):
    alphabet="mnbvcxzlkjhgfdsapoiuytrewq"
    for e in alphabet:
        if e not in string.lower():
            return False
    return True    
if (pangram(input("Enter a string="))== True):
    print("The string is a pangram")
else:
    print("The string is not a pangram")   
#10. Write a python program to create a function to check whether a string is an anagram or not.
def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        print("The string are Anagrams.")
    else:
        print("The string aren't Anagrams.")

s1="silent"
s2="listen"
anagram(s1,s2)
           
 
