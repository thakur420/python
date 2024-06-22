def hash(s:str):
    return sum(ord(x) for x  in s) % 100

print(hash("hello"))
print(hash("abc"))