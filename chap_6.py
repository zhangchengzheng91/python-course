def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result

# print(fibs(3))
# print(fibs(10))
# print(fibs(20))

def square(x):
    'Calculates the square of the number x'
    return x ** x
# print('square.__doc__=', square.__doc__)

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

storage = {}
init(storage)

def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = ['first', 'middle', 'last']

    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

Mynames = {}
init(Mynames)
store(Mynames, 'Magnus Lie Hetland')
print(lookup(Mynames, 'middle', 'Lie'))
store(Mynames, 'Robin Hood')
store(Mynames, 'Robin Locksley')
print(lookup(Mynames, 'first', 'Robin'))
print(Mynames)