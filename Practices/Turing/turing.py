""" list1 = [1, 2, 6, 12]
list2 = [12, 6, 2, 1]
print(list1 == list2)
print(set(list1) == set(list2)) """

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7]
""" print(l1.append(l2)) """
result1 = l1.extend(l2)
result2 = l1 + l2
""" result3 = extend(l1,l2) """
result4 = l1.append(l2)


print(result1)
print(result2)
""" print(result3) """
print(result4)

skills = ['1', '2', '3', '4']
skills.insert(3, '3.5')
print(skills)

t = '%(a)s %(b)s %(c)s'
print(t % dict(a='Welcome', b='to', c='Turing'))

""" Y = [2, 5J, 6]
Y.sort()
print(Y) """

data = [10, 20, 30, 40, 50]
data.pop()
print(data)
data.pop(2)
print(data)

print([i.lower() for i in "TURING"])

""" try:
    # Do something
except:
    # Do something
finally:
    # Do something """

print("Welcome to TURING".capitalize())

data = ['a', 'b', 'c', 'd']
""" newList =  """
""" copy(data) """
""" data.copy() """
""" newList.copy(data) """
newList = data.copy()
""" list(data) """

print(newList)

""" x = "abcdef"
i = "a"
while i in x[:-1]:
    print(i, end=" ") """

print(2**(3**2), (2**3)**2, (2**3)**3)

""" 'The {} side {1} {2}'.format('bring', 'of', 'life') """

def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
        print(l)

""" f(2)
f(3, [3,2,1])
f(3) """

data=[1, 2 ,3]
def incr(x):
    return x + 1

print(list(map(incr, data)))

import re
result = re.findall('Welcome to Turing', 'Welcome', 1)
print(result)