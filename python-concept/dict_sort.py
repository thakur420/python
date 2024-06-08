l = [{'name':'ram','age':20},{'name':'sita','age':18},{'name':'sam','age':10}]

l.sort(key=lambda x:x['name'])
print(l)

l.sort(key=lambda x:x['age'])
print(l)