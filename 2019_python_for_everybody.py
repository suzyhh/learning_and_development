#!/usr/bin/env python
# coding: utf-8
#http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf

#function to return whether a number is odd or even
def odd_or_even(number):
    if number==0:
        print(number,"is neither odd nor even")
    elif number%2==0: #% is the remainder, is number/2 = 0 then it is even
        print(number,"is even")
    else:
        print(number,"is odd")




#first pay rate exercise
hours=input("what hours do you work?\n")
rate=input("what is your pay per hour, rounded to the nearest whole number?\n")

#a try except block. tell pyhton to try something and then give the explanation if the command fails
try:
    if int(hours)> 40:
        extra=int(hours)-40
        pay=40*int(rate)+(extra*(int(rate)*1.5))
    else:
        pay=int(hours)*int(rate)
except ValueError:
    print("not a number") #if a string is entered rather than a number that cannot be converted to int()
print("your pay will be",pay)


#temperature exercise using a try except block
celsius=input("Give me a temperature in celsius\n")
try:
    far=(float(celsius)*(9/5))+32
    print(celsius,"in fahrenheit is",far)
except ValueError:
    print("not a number")
    

#more mathsy type stuff
import math
import random

#make a random choice from list, 10 times (range(10)) and list all choices in x (x.append())
list=[1,2,3,4,5]
x=[]
for i in range(10):
    x.append(random.choice(list))

#append y with 10 random numbers between the values of 5 and 90
y=[]
for i in range(10):
        y.append(random.randint(5,90))


#simplest function
def adding(a,b):
    c=a+b
    return c


#turn the pay rate exercise into a function and pay base rate for the first 40 hours and 1.5x the rate for any hours over 40
def pay(hours,rate):
    if int(hours)> 40:
        extra=int(hours)-40
        pay=40*int(rate)+(extra*(int(rate)*1.5))
    else:
        pay=int(hours)*int(rate)
    print("your pay will be",pay)


#numbers exercise
def numbers():
    sum=0
    count=0
    while True:
        line=input("enter a number, type done when finished:")
        if line.isnumeric():
            sum=sum+float(line)
            count=count+1
            continue
        elif line =="done":
            print("you are done")
            break
        else:
            try:
                int(line)
            except:
                print("bad data")
    print("total=",sum,",", count, "numbers added together, mean =",sum/count)


    
    
#list comprehension    
a=[1,2,3,4,5,6,7,8,9]
b=[i**2 for i in a]
#the same as 
#    b=[]
#    for i in a:
#        b.append(i**2)

#dictionaries
dict={"guinea pigs" : "three","hamsters" : "one", "humans" : "two", "cactuses" : "sixty"}

def how_many_things():
    stdin=input("how many of what thing? ")
    print(dict[stdin],stdin,"in the house")

#numbers exercise but using a list to store input and printing min and max values
def min_max():
    list=[]
    count=0
    while True:
        line=input("enter a number, type done when finished:")
        if line.isnumeric():
            list.append(line)
            count=count+1
            continue
        elif line =="done":
            print("you are done")
            break
        else:
            try:
                int(line)
            except:
                print("bad data")
    print("minimum=",min(list),"maximum=",max(list))

    
    
#take an input and print out each character in reverse order
index=input("What string?")
for i in index[::-1]:
    print(i)
 
#create a function that will count the number of letters in a word usinf user input
def words_and_letters(word,letter):
    count = 0
    for i in word:
        if i == letter:
            count = count + 1
    print(count)

#exercise, extract the number at the end of the string and convert to a float
str = 'X-DSPAM-Confidence:0.8475'
pos=str.find(":")
num=float(str[pos+1:])
#or single line
num=float(str[str.find(":")+1:])

#taking file input
fname=input("what is the file name?")
try:
    fhand=open(fname)
except:
    print("file does not exist")
    exit() #this seems to break the kernel but I can't work out why.....

#file exercise set up as a function with a fuck you easter egg
#you could put an else statement into the first try block to prevent subsequent code running if an exception is raised, i did it below somewhere
def spam_confidence():
    fname=input("what is the file name? ")
    if fname=="fuck you":
        print("fuck you too")
    else:
        try:
            fhand=open(fname)
        except:
            print("file does not exist") #else: etc etc
    count=0
    num=[]
    print("calculating the average spam confidence...")
    try:
        for line in fhand:
            if line.startswith("X-DSPAM-Confidence:"):
                count=count+1
                num.append(float(line[line.find(":")+1:])) #append the list 'num' with anything after the :
        print("average spam confidence = ",sum(num)/len(num))
    except:
        print("process failed")

        

#romeo exercise take 2.......
#reason it wasnt working was becuase I hadn't stated to look at each element after I'd split the line, I was just looking at the whole line        
list=[]
with open("romeo.txt") as fhand:
    for line in fhand:
        wrd=line.split() #split each line into a list of words
        for word in wrd:#look at each word of the list of words
            if word not in list:
                list.append(word)
            else:
                continue
      
#another list thingy    
str="dinosaurs are cool"
list1=[]
#wrd=str.split()
for i in str:
    if i not in list1:
        list1.append(i)
    else:
        continue
        
#dictionary exercise, open the email text file, find all lines that start with 'from' then extract the date (third element) and then count the number of days using a dicitonary
days=dict()
with open("mbox-short.txt") as fhand:
    for line in fhand:
        if line.startswith("From "):
            words=line.split()
            if words[2] not in days:
                days[words[2]]=1
            else:
                days[words[2]]+=1

#next dictionary exercise
emails=dict()
domain=dict()
with open("mbox-short.txt") as fhand:
    for line in fhand:
        if line.startswith("From "):
            words=line.split()
            if words[1] not in emails:
                emails[words[1]]=1
            else:
                emails[words[1]]+=1
            pos=words[1].find("@") #find the position of the @ in the first element of words (the email address)
            dom1=words[1] #extract just the email addresses otherwise the next bit doesnt work hah
            dom=dom1[pos+1:] #extract everything after the @
            if dom not in domain:
                domain[dom]=1 #create dictionary entry
            else:
                domain[dom]+=1 #update dictionary entry

#dictionary work, with tuples, which I still absolutely do not understand                
counts=dict()
with open("romeo.txt") as fhand: #open file
    for line in fhand: #loop through each line in the file
        word=line.split() #split lines so we can look at words
        for wrd in word: #access each element of each line
            #print(wrd) #guardian
            if wrd not in counts:
                counts[wrd]=1 #set up the dictionary with each word
            else:
                counts[wrd]+=1 #add number of occurances
lst=[]
for key,val in list(counts.items()): #to sort we have to convert to list, something to do with tuples
    lst.append((key,val))
lst.sort() #sort


#exercise, look for user with the most commits and print their email address. lotsof try except blocks for good measure
def most_commits():
    fname=input("What is the file name? ")
    emails=dict()
    domain=dict()
    try:
        with open(fname) as fhand:
            for line in fhand:
                if line.startswith("From "):
                    words=line.split()
                    if words[1] not in emails:
                        emails[words[1]]=1
                    else:
                        emails[words[1]]+=1
                    pos=words[1].find("@") #find the position of the @ in the first element of words (the email address)
                    dom1=words[1] #extract just the email addresses otherwise the next bit doesnt work hah
                    dom=dom1[pos+1:] #extract everything after the @
                    if dom not in domain:
                        domain[dom]=1 #create dictionary entry
                    else:
                        domain[dom]+=1 #update dictionary entry
    except FileNotFoundError:
        print("file not found")
    else: #if an exception isn't made (i.e. file exists) then continue with the code below
        try: #if you get rid of the else above it still tries to run the code and prints the error below
            top_emails=[]
            for key,val in list(emails.items()):
                    top_emails.append((val,key))
            top_emails.sort(reverse=True)
            print("user with most commits is",top_emails[0])
        except:
            print("something went wrong, check format?")
            

#read a file and prints letters in decreasing order of frequency
letters={}
count=0
with open("romeo.txt") as fh:
    for line in fh:
        line=line.lower() #all lowercase othewise it'll count them as different characters
        split=line.split() #split the lines
        for word in split: #access each word of the line
            for char in word: #access each character of the word
                if char not in letters: #building the dictionary
                    letters[char]=1
                else:
                    letters[char]+=1
    top_letters=[]
    for key,val in list(letters.items()): #converting from dictionary to list so we can find the highest
        top_letters.append((val,key))
    top_letters.sort(reverse=True) #sort by ascending value
    

#regular expressions are basically wildcards on steroids and can be used to make partial matches
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #if re.search('From:', line):
        #print(line)
        
#if re.search('F..m ', line): #match anything what starts with F then has two characters and ends with m
#if re.search('From:.+@', line): #match anyrhing that starts with From: then has one or more character (.+) and also contains an @ sign

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s) #finds substrings where there is a non-whitespace character (\S) that contains an @ somewhere (+@). the second \S+ prints the rest of the substring after @ until a whitespace is found
print(lst)

#find substring that starts with an upper or lower case letter or a number (a-zA-Z0-9), followed by zero or more characters (\S*) followed by an @ and ending with an upper or lower care letter (\S*[a-zA-Z])
lst1 = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', s) 
print(lst1)

#page 137 I'm trying to extract the whole date, failing spectacularly
with open("mbox-short.txt") as fh:
    for line in fh:
        line=line.rstrip()
        x=re.findall('From.*(\s.*[0-9].*)', line) #[0-9][0-9] looking for a two digit number on a line starting with From with an unknown amount of characters in between
        if len(x) > 0:
            print(x)
            
            
#more regex
#full stops are wildcards here, NOT *
str="in 2009, the quick brown fox jumped over the lazy dog"
re.findall("[0-9]",str)     #find a number, any number, and just one of them - they're all therefore printed as seperate strings
re.findall("[0-9]*[0-9]",str)   #find any number. literally find a number, then take any characters and end selection when you come across the last number in a string
re.findall("[0-9].[0-9]",str)   #find a string that is three digits long and formed from a number, then any character, then another number
re.findall("[0-9].\s[t]",str)   #find a string that start with a number, then has any character (.), then has a whitespace (\s), then has a t.
re.findall("[0-9].*[b]",str)    #find a string starting with a number, then has any number (*) of any characters (.) and then stop when you find a b
                                #output for this one is ['2009, the quick b']
re.findall("^[a-z].*",str)      #this actually just prints the whole line: print line that starts with (^) a letter, then has any number (*) of any character (.)
re.findall("^[a-z].",str)       #print line if it starts with a letter, then print the next character, regardless of what it is
re.findall("^[a-z]...",str)     #same as above but print the next three characters (...)

#trying to extract just email addressed
with open("mbox-short.txt") as fh:
    for line in fh:
        line=line.rstrip()
        x=re.findall('\s[a-z].*[@].*\s', line)
        if len(x)>0:
            print(x)

##back to regex exercises. this one replicates what grep does - give it a search term and it'll tell you how many times it appears in the file
count=0
regex=input("enter search term: ")
with open("mbox-short.txt") as fh:
    for line in fh:
        line=line.rstrip()
        if re.search(regex,line):
            count=count+1
        else:
            continue
    print("The term",regex,"appears",count,"times in the file")
    
#search for the number in the sub-string "New Revision: 39772"
#this isnt perfect, the data has to be converted between formats, but it works in the end
total=[]
count=0
with open("mbox-short.txt") as fh:
    for line in fh:
        x=re.findall("New Revision: [0-9]...",line)
        if len(x)>0:
            for i in x:
                num=re.findall("[0-9]+",i)
                num=[int(z) for z in num]
                total=total+num
    print("Average =",sum(total)/len(total))




