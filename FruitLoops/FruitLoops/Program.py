colors = ["red", "green", "blue"]
print(colors)
print(colors[1])

fruits = ["apple", "banana", "orange", "kiwi", "mango"]
# For-each loop
for item in fruits:
	print(item)

print()
# For loop
for index in range(len(fruits)):
	print(fruits[index])

# lastfruit = fruits[len(fruits)-1]
lastfruit = fruits[-1]
print(lastfruit)
input()