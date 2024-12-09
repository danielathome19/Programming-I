colors = ["red", "green", "blue"]
print(colors)
print(colors[1])  # green

fruits = ["apple", "banana", "orange", "kiwi", "mango"]
# For-each loop
for item in fruits:
    print(item)
print("")

# For loop
for index in range(len(fruits)):  # range(0, len(fruits))
    print(fruits[index])
print("")

# lastfruit = fruits[len(fruits)-1]
lastfruit = fruits[-1]
print(lastfruit)

input()