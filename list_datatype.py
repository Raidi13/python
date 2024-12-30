#list

#  l = [1, 2, 4, "abc", True,[10, 20, 30, "abcd" ,False]]
# print(1,type(1))

# l1 = 1[3]
# print(11)

# l2=l[5][0]
# print(12)

# print(1[len(1) -1][0])

print(dir(l))


"""
'clear', 'copy', 'fromkeys', 'get', 'items', 
'keys', 'pop', 'popitem', 'setdefault', 'update', 
'values'
"""
# append an element to the end of the list
# l.append(True)
# print(l)

# l.append([1, 2, 3, "abc", True])
# print(l)

# l.insert(0, "abc")
# print(l)

# res = l.insert(0, "abc")
# print(res, l)

# l = [10, 20, 30, "abcd", False]
# l.extend([1, 2, 3, "abc", True])
# print(l)

# l = [2, 3, 1]
# l.sort() # inplace
# l1 = sorted(l) # this returns a new list
# print(l, l1)
# txt = "Hello, And Welcome To My World!"
# print(txt.split(" ")

# List is a mutable datatype
l = [10, 20, 30, "abcd", False]
l[0] = 100
print(l)