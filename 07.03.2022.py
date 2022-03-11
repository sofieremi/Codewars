class A:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(user.name)


user = A('User')


class B(A):
    def hello(self):
        print('Hi,', user.name)


user = A('User')
