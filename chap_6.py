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

# Mynames = {}
# init(Mynames)
# store(Mynames, 'Magnus Lie Hetland')
# print(lookup(Mynames, 'middle', 'Lie'))
# store(Mynames, 'Robin Hood')
# store(Mynames, 'Robin Locksley')
# print(lookup(Mynames, 'first', 'Robin'))
# print(Mynames)

def story(**kwds):
    return 'Once upon a time, there was a '\
            '{job} called {name}.'.format_map(kwds)

def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0, start
    result = []

    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print(story(job='king', name='Gumby'))
print(story(name='Sor Robin', job='brave knight'))
params={'job': 'language', 'name': 'Python'}
print(story(**params))
del params['job']
print(story(job='stroke of genius', **params))
power(2, 3)
power(3, 2)
print('power------------')
power(y=3, x=2)
params=(5,) * 2
power(*params)
power(3, 3, 'hello world')
print('interval---------')
interval(10)
interval(1,5)
interval(3, 12, 4)
power(*interval(3, 7))
