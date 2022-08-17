
#WHILE LOOP AND FOR LOOPS
"""

#While Loop

number = 0

while number < 5:              #Will print +1 upto 5 so 0, 1, 2, 3, 4
    print(number)
    number += 1

#FOR LOOP

my_fruit = ["Apple", "Banana", "Orange"] #Will print APPLE, BANANA, ORANGE

for fruit in my_fruit:
    print(fruit.upper())
    
"""

#LIST COMPREHENSION
"""

result = []
for x in range(5):
    result.append(x ** 2)
"""

#BREAKING LOOPS
""" 

for i in range(10):
    print(i)

    if i == 5:
        break # Break the loop


for i in range(10):
    if i == 5:
        continue    # Will continue until i=5 then break out of current interation and then continue
        print(i)
                    # with the next iteration
"""

#NESTED LOOPS
""" 

for i in range(3):
    for j in range(4):
        print(i, "x", j, "=", i * j)


for i in range(10, 21, 2): #Goes from 10-21 in 2s
    print(i)
"""

#ITERATING DICTIONARIES
""" 

for key in {"key": "value"}:
    print(key)             #will print key

for value in {"key": "value"}.values():
    print(value)              # will print value

for key, value in {"key": "value"}.items():
    print(key, value)         #Will print key and value
"""


#ITERATING STRINGS
"""

for char in "Hello world":
    print(char)

for char in "Hello world":
    print(char)
"""


















