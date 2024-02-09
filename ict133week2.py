
""""

Link: 
https://www.w3schools.com/python/python_strings.asp
https://www.w3schools.com/python/python_string_formatting.asp
https://mkaz.blog/code/python-string-format-cookbook/ -- suggested by lecturer

1.elements are enclosed within '', "", "'"'
Str () data type start with 0
if integer , no need to ''

2.how to use index? 
--must have []


3.slicing
how to slice
[start:end:increment]

4.if increment is missing, 1 is used. 1 is default

5.how to reverse entire string?
just include -1 
so instead of putting 0. put -0
print(name[::-1])

6.concat
-combine two string together
"Hello" + "Aishah"


repetition (*) does a multiple of concat in a str


7.len
return the number of elemets 
find how long the string is. dalam aishah, ada 6 characters

len("spam") 4 

8.split(separator)

9.list is similar to string.
TMA is all about list

how to create a lsit?
nama anak = [sarah, zulkarnain]


Operator Meaning
+ Concatenation
* Repetition
aStr[index] Indexing
aStr[start:end:increment] Slicing
len(<sequence>) Length

10.method is like a function

11. string formatting

12.format 
<template-string>.format(<values>)

{} : "slot" for value in format. {} is where u store the value!!!! remember this

{0:0.2f}
<index>:<format_specifier>
format(value) -- this is where the value is

normally use for money

13.what does :< mean?
meaning left alignment
normally used in format
"""

#question 1 of lab
#only suss email
""""(String) Write a program that reads in an email address, e.g. joe@suss.edu.sg
Display the name and the organisation on separate lines. Example:
Input email address: joe@suss.edu.sg
Name is joe
Organisation is suss.edu.sg
Assume input is valid.
"""



name, emailaddress = input('Enter email address').split('@')
print('Email address :' ,name, '@' ,emailaddress)
print('Name :', name)
print('Organisation is :', emailaddress) # print org
# another way to print org

# question 2 lab

""""
(String) Write a program that reads in a string input consisting of 2 words with
a blank in between. The program displays each of the word in reverse.
Example:
Enter string: java python
Output: avaj nohtyp
Assume input is valid.
"""

word1, word2 = input('Enter the 2 words').split() # separate by space
updatedword1, updatedword2 = word1[::-1], word2[::-1]# returning it as a list
print('Output is :', updatedword1, updatedword2)

name= 'Aishah'

print(name[0:3] *3 )# print the output 3 times. putting it outside the bracket wont let it print

print(name[1]) #will return the output of i. [] is returning index

print(name[0:-3:2])

print(name[0:-3:2])

print(name[::-1]) # will reverse the entire string
""""
will return the output of AS. will start at index 0 which is A, then end at index 3, but increment by 0 +2 = 2. so index 2 is S
"""


result = "Hello" + "Aishah"
print(result)
print(len(name))

#split 
# define variable
# when there is space. when user put space, it willt ake the last name
firstname, lastname = input('Enter firstname and lastname').split()
print(firstname)
print(lastname)


# how to capitalise first character in the string?
#use capitalise()
#The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
capitalisedVersion = firstname.capitalize() 
print(capitalisedVersion) # going to capitalise the first character






# how to create a list?
# sarah is aged 4, while zulkarnain is aged 5

namaanak = ['sarah', 'zulkarnain', 4, 5] 


#string formatting

