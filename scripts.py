# Algorithmic Methods of Data Mining - Homework 1
# Solutions to the HackerRank challenges I completed.
# Each solution is the code I submitted on HackerRank with status: Accepted


# ======================================================================
# PROBLEM 1
# ======================================================================


# ----------------------------------------------------------------------
# INTRODUCTION
# ----------------------------------------------------------------------

# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")


# Python If-Else

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")


# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a + b)
print(a - b)
print(a * b)


# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/b)


# Loops
if __name__ == '__main__':
    n = int(input())
i = 0
while i < n:
    print(i ** 2)
    i += 1


# Write a function
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return leap
        else: 
            return True
    
    return leap

year = int(input())
print(is_leap(year))


# Print Function
if __name__ == '__main__':
    n = int(input())
i = 1
while i <= n:
    print(i, end = "")
    i += 1


# ----------------------------------------------------------------------
# BASIC DATA TYPES
# ----------------------------------------------------------------------

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
lista = [[i, j, k] for i in range(0, x + 1) for j in range(0, y+1) for k in range(0, z+1) if i+j+k != n]

print(lista)


# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = list(arr)
arr.sort()
primo = arr[-1]
for el in arr:
    if el != primo:
        secondo = el
print(secondo)


# Nested Lists
if __name__ == '__main__':
    lista = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name, score])
    
lista_grades = []
for el in lista:
    if el[1] not in lista_grades:
        lista_grades.append(el[1])
    
lista_grades.sort()
lista_nomi = []

for el in lista:
    if el[1] == lista_grades[1]:
        lista_nomi.append(el[0])

lista_nomi.sort()

for i in range(0, len(lista_nomi)):
    print(lista_nomi[i])


# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

totale = 0
count = 0 
for student in student_marks:
    if student == query_name:
        for i in student_marks[student]:
            totale += i 
            count += 1
        print(f"{totale/count:.2f}")


# Lists
if __name__ == '__main__':
    N = int(input())

lista = []
for i in range(0, N):
    comando = input().split()
    if comando[0] == "insert":
        lista.insert(int(comando[1]), int(comando[2]))
    if comando[0] == "print":
        print(lista)
    if comando[0] == "remove":
        lista.remove(int(comando[1]))
    if comando[0] == "append":
        lista.append(int(comando[1]))
    if comando[0] == "sort":
        lista.sort()
    if comando[0] == "pop":
        lista.pop()
    if comando[0] == "reverse":
        lista = lista[::-1]


# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
t = tuple(integer_list)
print(hash(t)) 


# ----------------------------------------------------------------------
# STRINGS
# ----------------------------------------------------------------------

# sWAP cASE
def swap_case(s):
    stringa = ""
    for letter in range(0, len(s)):
        if s[letter].isupper():
            stringa += s[letter].lower()      
        elif s[letter].islower():
            stringa += s[letter].upper()  
        else: 
            stringa += s[letter]
    return stringa

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# String Split and Join
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# Mutations
def mutate_string(string, position, character):
    
    string = list(string)
    string[position] = character
    string = ''.join(string)    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Find a string
def count_substring(string, sub_string):
    totale = 0
    for char in range(0, len(string) - len(sub_string) + 1):
        if sub_string in string[char:char+len(sub_string)]:
            totale += 1
    return totale

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# String Validators
if __name__ == '__main__':
    s = input()
    alnum = alpha = digit = lower = upper = False
    for c in s:
        if c.isalnum():
            alnum = True
        if c.isalpha():
            alpha = True
        if c.isdigit():
            digit = True
        if c.islower():
            lower = True
        if c.isupper():
            upper = True

    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)


# Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))