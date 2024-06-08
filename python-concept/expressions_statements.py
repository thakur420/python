'''
Item1: Slicing
    somelist[start:end]
    start : inclusive
    end : exclusive
    stride : index interval(step)
    works with built-in types: list,tuple,str,bytes
    works with any class that defines __getitem__
'''
l = ['a','b','c','d','e','f','g','h']
print(l[:4])
print(l[-4:])
print(l[3:-3])

assert l[3:] == l[3:len(l)], "LHS should be equal to RHS"

# slicing create new list(deep copy)
l_slice = l[:4]
l_slice[2] = 99
print(l)
print(l_slice)

#tuple assignment
b,c = l[2:4]
print(b,c)
#x,y = l[3:7] #ValueError: too many values to unpack (expected 2)
#print(x,y)

#slice assignment
print("slice assignment",l)
l[2:7] = [99,22,33] # truncate the list if rhs size < lhs size
l[2:7] = [99,22,33,1,2,3,4,5,6,7,8,9,10] # extend the list if rhs size > lhs size
print(l)

#deep copy list using slicing
l_copy = l[:]
print(l," | ",id(l))
print(l_copy," | ",id(l_copy))


'''
Item2: Slicing with stride
    somelist[start:end]
    start : inclusive
    end : exclusive
    stride : index interval(step)
'''
a = ['a','b','c','d','e','f','g','h']
b = a[::2]
print(b)
c = a[::-1]
print(c)
d = a[-2:2:-2]
print(d)

'''
Item3 : Prefer enumerate over range
'''
fruit_list = ['apple', 'banana','mango','grape','kiwi']
for i in range(len(fruit_list)):
    print(f'{i+1} :{fruit_list[i]}')

#use of enumrate
for i,fruit in enumerate(fruit_list,1):
    print(f'{i} : {fruit}')




