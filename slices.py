list1 = [1, 2, 3, 4, 5]
list2 = list1[0:3]  # [:3]
print(list2)
list3 = list1[3:len(list1)]  # [3:]
print(list3)
print(list2 + list3)

strHi = "Hello, world!"
substr = strHi[0:5]
print(substr)
print(strHi[-1])
print(strHi[-6:-1])
print(strHi[::-1])
print(strHi == strHi[::-1])
