import re

# while True:
#     print("print name please")
#     name = input()
#     if name == "shenhaiqi":
#         print("got it ")
#         break
#     print("wrong name")

print("print my name")
for i in range(5):
   print(f'shen 5 time ({i})')
   

import random

for i in range(10):
   print(f"10 number are {random.randint(0,1)}")


# print("enter number")
# spam  = int(input())
# if spam == 1:
#    print("hello")
# elif spam ==2:
#    print("howdy")
# else:
#    print("greeting")

for i in range(1,11):
   print(i)

n=1
while n<=10:
   print(n)
   n=n+1


# def collatz(num):
   
#    if num%2 == 0:
#       result = num//2
#       print(result)
#       return result
#    else:
#       result = 3*num+1
#       print(result)
#       return result
   
   

# print("enter the number")
# try:
#     num = int(input())
# except:
#    print("number only")
# else:
   
#     collatz(num)






# animals = ["cat","dog","monkey"]
# print("check if we have it, what do u have as pet")

# myAnimal = input().strip()
# if not myAnimal.isalpha():
#     print(f"{myAnimal} should not be special charater or number")
# elif myAnimal.lower() not in [k.lower() for k in animals]:
#    print(f"{myAnimal} not in list")

# else:
#     print(f"we got what you got -> {myAnimal}")






test = ["hello its shen","hello its dan","hello its angie"]
print(test[random.randint(0,len(test)-1)])



spam = ["a","b","c","d"]

def STRconvert(li):
   if not li:
      return ''
   elif len(li) == 1:
      return str(li[0])
   
   newStr = ""
   for i in range(len(li)-1):
      newStr = newStr+str(li[i])+", "
   
   newStr=newStr+"and "+str(li[-1])
    
   return newStr
      

print(STRconvert(spam))


count = {}
for words in ["apple", "peach", "apple"]:
   count[words] = count.get(words,0)+1
print(count)

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
 count.setdefault(character, 0)
 count[character] +=1
pprint.pprint(count)

a, *m, b = "hello"
print(a, m, b)
# → h ['e', 'l', 'l'] o

staff = {"rope":1,"torch":6,"gold coin":42,"dagger":1,"arrow":12}

def displayInventary(inventary):
   print("inventary")
   item_total = 0
   for k,v in inventary.items():
      print(f"{k} {v}")
      item_total+=v
   print("total item is "+str(item_total))

displayInventary(staff)
print("----------------------")

def addItem(inventary, add):
   for item in add:
      inventary[item] = inventary.get(item,0)+1
   return inventary
      

inv = {"gold coin":42, "rope":1}
addItem(inv,staff)
displayInventary(inv)



def word_count(text):
   words =text.lower().split()
   dic={}
   for word in words:
      dic.setdefault(word,0)+1
      dic[word]+=1
   return dic
      
      
   
print(word_count("The cat sat on the mat. The cat was happy."))

def letter_count(text):
   dic={}
   for letter in text:
      dic.setdefault(letter,0)+1
      dic[letter]+=1
   
   return dic


print(letter_count("the cat sat on mat"))


def wordCount(text):
   words = text.split()
   dic = {}
   for word in words:
      dic[word] = dic.get(word,0)+1
     
   return dic


print(wordCount("the cat sat on mat"))

print("its \'hello\'s \tme")

"""print("comment")"""

print("hello".isalpha())

print(":".join(["p","p","p"]))


Data = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]
# apples Alice dogs
#  oranges Bob cats
#  cherries Carol moose
#. banana David goose


# def printTable(tableData):
#     num_rows = len(tableData[0])       # 4
#     num_columns = len(tableData)       # 3
    
#     for r in range(num_rows):
#         row_items = []
#         for c in range(num_columns):
#             item = tableData[c][r]     # ← THIS IS THE MAGIC: c then r
#             row_items.append(item)
#         print(" ".join(row_items))
     
     
   
# printTable(Data)


Data = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]


def transform(Data):
   if not Data or not Data[0]:
      return
   
   num_row = len(Data[0])
   num_col = len(Data)

   for r in range(num_row):
      result = []
      for c in range(num_col):
         item = Data[c][r]
         result.append(item)
      print(" ".join(result))

transform(Data)





print("RE match ")
k = "hello"
text = "Contact: john@example.com or support@python.org"
match = re.search(r'\w+@\w+\.\w+', text)

if match:
    print("Found email:", match.group())  #john@example.com
    print("Start index:", match.start())   #9
    print("End index:", match.end())       #25
    print(text[9:25])

emails = re.findall(r'\w+@\w+\.\w+',text)  
print(emails)   #john@example.com or support@python.org



a= re.match(r'hello','hello world') #<re.Match object; span=(0, 5), match='hello'>
b= re.match(r'Hello','hello world') #None
print(a)
print(b)


phone = "call 123-333-3333 or 343-324-3423"
pattern = r'(\d{3})-(\d{3})-(\d{4})' 
print(re.findall(pattern,phone))   #[('123', '333', '3333'), ('343', '324', '3423')]

text = "I love cats. Cats are cute."
result = re.sub(r'cats', 'dogs', text, flags=re.IGNORECASE)  # case-insensitive
print(result) #I love dogs. dogs are cute.


data = "apple, banana; orange   grape  mango"
print(data)
parts = re.split(r'[,\s;]+', data)
print(parts)#['apple', 'banana', 'orange', 'grape', 'mango']




# Compile once, reuse many times — faster than calling re.match() repeatedly!
date_pattern = re.compile(r'^(0[1-9]|1[0-2])/\d{2}/\d{4}$')

# Now use the compiled object's methods:
print(date_pattern.match("07/23/2024"))   #<re.Match object; span=(0, 10), match='07/23/2024'>
print(date_pattern.search("Date: 12/99/2025"))  # None
print(date_pattern.findall("01/23/2024 and 03/24/2025"))  #[]



# .	Any character except newline (\n)
# ^	Start of string (or line with multiline flag)
# $	End of string (or line)
# *	0 or more repetitions of preceding element
# +	1 or more
# ?	0 or 1 (i.e., optional), OR makes quantifiers non-greedy (*?, +?)
# {m}	Exactly m times
# {m,n}	Between m and n times
# []	Character set: [abc], [a-z], [^0-9] (not digits)
# \d	Any digit → [0-9]
# \w	Word char → [a-zA-Z0-9_]
# \s	Whitespace → space, tab, newline (\n, \r)
# ()	Grouping + capture
# \	Escape metacharacters (\., \$)


# r'\d+'	One or more digits
# r'[A-Z][a-z]+'	Capitalized word (e.g., "Python")
# r'\bhello\b'	Word boundary — matches "hello" but not "shells"
# r'https?://\S+'	URLs starting with http or https (non-whitespace after)
# `r'^(0[1-9]	1[0-2])/\d{2}/\d{4}$'`



#它把一个正则字符串（如 r'\d+'）编译成一个 RegexObject（正则对象），
# 之后你可以反复用它调用 .match()、.search()、.findall() 等方法，
# 避免每次重复解析正则表达式。
phoneNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
info = phoneNum.search("my phone number is 860-123-0334")
print(info)  #<re.Match object; span=(19, 31), match='860-123-0334'>
print(info.group()) #860-123-0334

import re

formatDate = re.compile(r"(\d\d\d\d)-(\d\d-\d\d)")
newDate = formatDate.search("my new format date is 1991-02-09")
print(newDate)
print(newDate.group(2))

nameCheck = re.compile(r"shen|dan",re.IGNORECASE)
result = nameCheck.search("Shen or Dan")
print(result.group())


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman') #either batman or batwomen either


batRegex = re.compile(r'Bat(wo)*man') #zero or more with *
mo3 = batRegex.search('The Adventures of Batwowowowoman') #'Batwowowowoman'

batRegex = re.compile(r'Bat(wo)+man') #one or more


print(re.match(r'^\d+$', '12d3')) 


neRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 \d{3} # first 3 digits
 (\s|-|\.) # separator
 \d{4} # last 4 digits
 (\s*(ext|x|ext.)\s*\d{2,5})? # extension
 )''', re.VERBOSE)


print("------------------------------------------------------------------")
print("create a regex for phone number\n")


# a ="abc"
# print(a)
# print(repr(a))
# print(type(a))
# print(type(repr(a)))
# print(type(a)==type(repr(a)))
# print(a==repr(a))

import pyperclip



# 'r'	Read (default). File must exist.
# 'w'	Write. Creates new file or overwrites existing.
# 'a'	Append. Creates file if it doesn’t exist. Writes at end.
# 'x'	Exclusive creation. Fails if file exists (safer than 'w').
# 'r+'	Read and write (file must exist).
# 'w+'	Write & read (truncates file).
# 'a+'	Append & read (writes only at end; reading starts from current position).

from pathlib import Path
myfile = Path('data.txt')

if myfile.exists():
   with open(myfile,'r',encoding='utf-8')as f:
      file = f.read()
      print(file)
else:
   print("no file")

# with open('data.txt','r',encoding="utf-8")as f:
#    for line in f:
#       print(line.strip())

    # line1 = f.readline() 
#--------------------------------------------------------------------------
# with open('data.txt','a',encoding='utf-8') as f:
#    f.write("this is writing file text\n")


# lines = ['a','b','c',]
# with open('data.txt','a')as f:
#    f.writelines(lines)
#    f.writelines("\n")

squares = [i**2+100 for i in range(1,11)]
print(squares)



items = ['a','b','c']



# while True:
#    adding = input("adding letter? \'quit\' to exit\n").lower()
#    if adding == 'quit':
#       print("quiting\n",items)
#       break
   
#    result = adding
#    items.append(result)
#    print(items)
   
   
   
# active = True
# while active:
#    userInput = (input("tell me age to get the price\n"))

#    if userInput == "quit".lower():
#       break
   
#    age = int(userInput)

#    if age<=3:
#       print("free")
      
#    elif(3<age<=12):
#       print("10 dollar")

#    else:
#       print(15)
#    active =False
   

sandwich_order= ['a','b','c']
finish_sandwiches = []

print("b is out of order")

finish_sandwiches = [item for item in sandwich_order if item !='b']
print(finish_sandwiches)

import copy
magic = ['shen','dan','jin']
magic2 = []

def showName(name):
   if not name:
      name = copy.deepcopy(magic)
      for i in name:
         print("just add "+i)
   else:
      for i in name:  
         print("the great "+i)   
  



showName(magic2)

def build_profile(f,l,**info):
   dic ={}
   dic['first name'] =f
   dic['last name'] = l
   for k,v in info.items():
      dic[k] =v
   return dic


result = build_profile("shen",'qi',age = 12,hobby="sleep")
print(result)


def build_file(*name,**info):
   dic = {}
   dic['first name'] = name
   for k,v in info.items():
      dic[k]=v
   return dic

result = build_file('dan dan lin',hobby='playing', hobby2='666')

print(result)



def carInfo(year,color,brand = "toyota", **other):
   info = {'year' :year,'color' :color,'brand' :brand}
   for k,v in other.items():
      info[k]=v
   return info

car1 = carInfo(2001,'white',body='suv',maxspeed=300)
car2 = carInfo(2025,'sliver',brand='BMW',maxspeed='500',price ='call for price')

print(car2)
      
   

class Restaurant():
   def __init__(self,restaurant_name,cuisine_type,serve=0):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
      self.serve = serve
    
   def open_restaurant(self):
      print("it's open now")

   def describe(self):
      print(self.restaurant_name + " in ct")
      print(self.cuisine_type +" traditional ")
      print("there is "+str(self.serve))

   def total_customer(self):
      print("there is "+str(self.serve)+ " customer")
   
   def add_total_customer(self,add):
      self.serve+=add

   def total_customer_reset(self):
      self.serve= 0



class IceCreamStand(Restaurant):
   def __init__(self,restaurant_name,cuisine_type="ice cream"):
      super().__init__(restaurant_name,cuisine_type)
      self.flavors =[]
   
   def describe(self):
      print("from ice cream")
    #   return super().describe(
         
    #   )
      
   


   def displayFalvors(self):
      print(f'wow it is {self.cuisine_type}')
      for f in self.flavors:
         print(f'the flavors are {f}')

restaurant = Restaurant("china house","chinese food",0)
restaurant.open_restaurant()
restaurant.describe()
restaurant.add_total_customer(100)
restaurant.total_customer()
restaurant.total_customer_reset()
restaurant.total_customer()

myIceCream = IceCreamStand("japanese import ice cream")
myIceCream.flavors = ['chocolate','vanilla','milk']
myIceCream.add_total_customer(25)
myIceCream.describe()
myIceCream.displayFalvors()

# class User():
#    def __init__(self,f, l ,login_attemp = 0):
#       self.firstName = f
#       self.lastName = l
#       self.login_attemp = login_attemp

#    def greet_user(self):
#       print(self.firstName+ " "+self.lastName+" saying hello")
#       print(str(self.login_attemp))

#    def increment_login_attemp(self):
#       self.login_attemp+=1

#    def reset_login(self):
#       self.login_attemp= 0
   



      


# # user = User("shen","qi",4)
# # user.greet_user()
# # user.increment_login_attemp()
# # user.greet_user()
# # user.reset_login()
# # user.greet_user()


def F(n: int) -> int:
    if n in (0, 1):
        return 1
    else:
        return F(n-1) + F(n-2)
    
print(F(2))

#0 1 1 2 3 5 8 13 21.  //f(1)+f(0)
#0 1 2 3 4 5 6 7  8

import sys
x =1000
y=x
print(id(x) == id(y))
print(type(id))
print(sys.getrefcount(x))


def add(a,b):
    return a+b



def sub(a:int,b:int)->int:
    return a-b

print(int.__mro__) #method resolution order
      
# x = [42,12]
# print(isinstance(x, int))     
# print(isinstance(x, float))
# print(isinstance(x[1],int))


lst = [1,2,3,4,5,6,7,8,'shenhaiqi']
def has__string(lst):
    for i in lst:
        if isinstance('shenhaiqi',str):
            return True
    return False

# print(has__string(lst))


lst2 = [1,3,5,6,7,8,'hi']

def has_int(lst):
    for i in lst:
        if isinstance(i,int):
            return True
    return False


def has_int2(lst):
    for i in lst:
        if not isinstance(i,int):
            return False
    return True

print(has_int2(lst2))


dict1 = {'a':10,'b':20}

def check_type(data):
   if isinstance(data,list):
      print("this is list")
   elif isinstance(data,dict):
      print("this is dict")

check_type(dict1)

print(any(isinstance(i, int) for i in lst)) ##lazy way must be true for one of them
print(all(isinstance(i, int) for i in lst)) #must be true for all of them


def count_int(lst):
   count = 0
   for i in lst:
      if isinstance(i,int):
         count+=1
   return count

print(count_int(lst))

