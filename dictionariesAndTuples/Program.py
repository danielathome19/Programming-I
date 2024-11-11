lst = [1, 2, 3]  # List
tpl = (1, 2, 3)  # Tuple - immutable, allows unpacking
a, b, c = tpl    # Unpack tuple into 3 vars
print(tpl)

dct1 = {1: "apples", 2: "oranges", 3: "pears"}
dct2 = {"name": "John", "color": "red", 0: [1,2,3]}
print(dct1[2])
print(dct2["name"])
print(dct1)
print(dct1.keys())
print(dct1.values())

input()
