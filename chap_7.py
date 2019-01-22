class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm {}".format(self.name))


# foo = Person()
# bar = Person()
# foo.set_name('Luke Sky')
# bar.set_name('Andkin')
# foo.greet()
# bar.greet()
# print(foo.name)

class Secretive:

    def __inaccessible(self):
        print("Bet you can't ses me ...")

    def accessible(self):
        print('The secret message is:')
        self.__inaccessible()

# s = Secretive()
# s.accessible()
# s._Secretive__inaccessible()

class MemberCount():
    members = 0
    def init(self):
        MemberCount.members += 1

# m1 = MemberCount()
# m1.init()
# print(MemberCount.members)
# m2 = MemberCount()
# m2.init()
# print(MemberCount.members)
# m3 = MemberCount()
# print(MemberCount.members)
# print(m1.members)

class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

# f = Filter()
# f.init()
# fr = f.filter([1, 2, 3])
# print(fr)
# s = SPAMFilter()
# s.init()
# sr = s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])
# print(sr)

class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is ', self.value)

class TalkingCalculator(Calculator, Talker):
    pass

# tc = TalkingCalculator()
# tc.calculate('1 + 2 * 3')
# tc.talk()
# print(hasattr(tc, 'talk'))
# print(hasattr(tc, 'frond'))

from abc import ABC, abstractclassmethod

class Talk(ABC):
    @abstractclassmethod
    def talk(self):
        pass

# talk = Talk()

class Knight(Talk):
    def talk(self):
        print('Hi')

# knight = Knight()

class Herring:
    def talk(self):
        print('Blub')

# h = Herring()

# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the second number: '))
#     print(x / y)
# except (ZeroDivisionError, TypeError, NameError, ValueError) as e:
#     print(e)
#     print('The second number can not be zero')

class MuffledCalculator:
    muffled = True
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise

# calculator = MuffledCalculator()
# calculator.calc('10 / 2')
# calculator.calc('10 / 0')

# try:
#     1/0
# except ZeroDivisionError:
#     raise ValueError from None

# try:
#     print('A simple task')
# except:
#     print('What? Something went wrong')
# else:
#     print('Ah ... It went as planned')

try:
    1 / 0
except Exception as e:
    print(e)
else:
    print('That went well')
finally:
    print('Cleaning up')
