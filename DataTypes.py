print("Hello World")

name=input("Hello, what is your name?")

age=int(input("and what is your age"))

print(type("Hello World"))

firstname="Steven"
lastname="Smith"
print("Hello"+" "+firstname+" "+lastname)

number1=float(input("Please enter the first number:"))
number2=float(input("Please enter the second number:"))
answer=number1+number2
print(number1, "+", number2, "=", answer)

"Hello World".lower()
"Hello World".upper()
"Hello world".replace("world", "UK")
"Hello world".split()
"Squirrel, Guinea Pig, Donkey".split(",")
"".join(["Hello", "world"])
" ".join(["Squirrel", "Guinea Pig", "Donkey"])

"Hello world".count ("o")
"Hello world".isdigit()
"123312213".isdigit()
"Dog"+"Cat"

age = 25
f"Steve is {age} years old"
f"Steve will be {age+10} years old in 10 years

"Hello, they call me \"Jeff\""

print("Person 1: \tHey, How are you?\nPerson 2:\tGood thanks!")
print("Person 1: \tHey, How are you?\nPerson 2:\tGood thanks!\U0001F604")

int(3.6)
float(3)

word1 = "Good"
word2 = "Day"
word3 = "Steven"

sentence = word1 + " " + word2 + " " + word3
print(sentence)

number1 = input("Enter whole number:")
number2 = input("Enter decimal number:")
integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))
print(number1)
print(number2)
print(round_number)

name = "Pep"
age = 3
bark = True
tweet = false
print ("My pet is called", name, ", He is", age, "years old.")
print("Statement:", name, "barks.", bark)

# Collections

cool_cows = ["Wimmie the Moo","Moolan","Milkshake","Mooana"]
cool_cows [0]
cool_cows[-1]
cool_cows[-1]
cool_cows[1:3]
cool_cows[1:]
cool_cows[0] = "Alladin but a cow"
del cool_cows [0]
"Moolan" in cool_cows
"cheesebuger" in cool_cows

cool_cows = ["Wimmie the Moo","Moolan","Milkshake","Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]
cool_animals = [cool_cows, cool_sheep, cool_pigs]
farm = ["Pepperidge Farm", ["Winnie the Moo", "Moolan"], 1850]
farm[0] # Result is a string
farm[1] # Result is a list of strings
farm[2] # Result is a intgeger


list.append()
list.remove()
list.pop()
list.sort()

noises = {"cow" : "moo", "sheep" : "baa"}
noises["cow"]
noises["sheep"]
noises["chicken"] = "cluck"

print(noises)
dict.keys()
dict.values()
"moo" in noises
"moo" in noises.values()

tuple(noises.keys())
tuple(noises.values())
tuple(noises.items())

my_words = {"hello" : "hola","thank you" : "gracias"}
my_words.get("hello")
my_words.pop("hello")
print(my_words)

books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
print(books["The Handmaiden's Tale"])

