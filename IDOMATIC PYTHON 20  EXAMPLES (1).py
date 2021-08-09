Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> '''
# example(1)-Looping over dictionary keys

a = {'new': 'blue', 'name1': 'green', 'name2': 'red'}

for i in a.keys():
    print(i)
 
a = {'new': 'blue', 'name1l': 'green', 'name2': 'red'}


for i in a.keys():
    if i.startswith('n'):
         print(i)

         
        
# example(2)-looping backwards   
    
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)-1,-1,-1):
    print(colors[i])
    
colors = ['red', 'green', 'blue', 'yellow']
for color in reversed(colors):
    print(color)

names = ['raju' , 'hari' , 'rohith' , 'vamsi']
colors = ['clever','danger','handsome','crazy']
n = min(len(names) , len(colors))
for i in range(n):
    print(names[i] , '->' , colors[i])
   
names = ['raju' , 'hari' , 'rohith' , 'vamsi']
colors = ['clever','danger','handsome','crazy']    
for name, color in zip(names, colors):
    print(name, '->',color)

names = ['raju' , 'hari' , 'rohith' , 'vamsi']
colors = ['clever','danger','handsome','crazy']
for name,color in zip(names, colors):
    print(name,'->',color)

    
  
# example(3)-sorted list
names = ['raju' , 'hari' , 'rohith' , 'vamsi']
for names in sorted(names):
    print(names)
    
names = ['raju' , 'hari' , 'rohith' , 'vamsi']
print(sorted(names, key = len))



# example(4)-Looping over a range of numbers

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
    print(i**3)

for i in range(9):
    print(i**3)


  
# example(5)-Looping over a collection
colors = ['white', 'yellow', 'red', 'black']

for i in range(len(colors)):
    print(colors[i])

colors = ['white', 'yellow', 'red', 'black']

for color in colors:
    print(color) 


# example(6)-using and and or

x = int(input("Please enter a number between 1 and 10: "))

if x > 0 and x < 11:
	print(x)
else:
	print("Invalid selection")


x = int(input("Please enter a number between 1 and 10: "))

if x < 1 or x > 10:
	print("Invalid selection")
else:
	print(x)



# example(7)-using of list in differnt way

student=("chandu","raju","tarak","tejas","ramu")
print(student[0:3])

student=("chandu","raju","tarak","tejas","ramu")
print(student[:3])

# example(8)- using list and editing it.

list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]
  
print(list1)
print(list2)

list1 = [5, 4, 3, 2, 1]
list1 = list1 + [1, 2, 3, 4]
list2 = list1

print(list1)
print(list2)


#example(10)-Using the in keyword.

my_list = ['Larry', 'Moe', 'Curly']
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

my_list = ['Larry', 'Moe', 'Curly']
for element in my_list:
    print(element)


#example(11)- using variables

x = 'foo'
y = 'foo'
z = 'foo'
print(x)
print(y)
print(z)

string = x = y = z = 'foo'

print(string)

#example(12)- Avoid using a temporary variable when performing a swap of two values

foo = 'Foo'
bar = 'Bar'
temp = foo
foo = bar
bar = temp

foo = 'Foo'
bar = 'Bar'
(foo,bar) = (bar,foo)
print(foo,bar)

#example(13)- using negative indexes.

def get_suffix(word):
    word_length = len(word)
    print(word[word_length - 2:])

def get_suffix(word):
    print(word[-2:])


#example(14)- using the built-in function.

the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
the_sum = 0
for element in the_list:
    the_sum += element

the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
the_sum = sum(the_list) 

#example(15)-

my_list = ['Larry', 'Moe', 'Curly']
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

my_list = ['Larry', 'Moe', 'Curly']
for element in my_list:
    print(element)
 
# example(16)-

def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
        L.append(a)
        return L
print(f(1))
print(f(2))
print(f(3))


#example(17)-

def print_list(list_value, sep):
    print('{}'.format(sep).join(list_value))
the_list = ['a', 'b', 'c']
the_other_list = ['Jeff', 'hates', 'Java']
print_list(the_list, ' ')
print_list(the_other_list, ' ')
print_list(the_other_list, ', ')

def print_list(list_value, sep=' '):
    print('{}'.format(sep).join(list_value))
the_list = ['a', 'b', 'c']
the_other_list = ['Jeff', 'hates', 'Java']
print_list(the_list)
print_list(the_other_list)
print_list(the_other_list, ', ')


# example(18)-

def all_equal(a, b, c):
    result = False
    if a == b == c:
        result = False
        if a == b == c:
            result = True
            return result
        
def all_equal(a, b, c):
return a == b == c


# example(19)-

def add(x,y):
    return x+y
x=3
y=4
z = add(x,y)
print(z)

adder = lambda x,y: x+y
print(adder(3,4))



# example(20)-
students = ["raju", "ushodaya", "venkat", "sai", "tom"]
print(students[-1])

students = ["raju", "ushodaya", "venkat", "sai", "tom"]
print(students[-1])