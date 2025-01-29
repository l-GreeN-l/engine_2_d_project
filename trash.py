from copy import deepcopy, copy

class A:



    def __new__(cls, *args, **kwargs):

        if len(kwargs) > 0 and len(args) > 0:
            if kwargs['x'] > 5:
                return super().__new__(cls)
            else:
                print('Error in arguments')
        else:
            return super().__new__(cls)

    # def __new__(cls, *args, **kwargs):
    #     return cls.__new__(cls)

    def __init__(self, x):
        self.x = x
        print("init")

    def get_x(self):
        print(self.x)
        # print("XX")




a = A(x=10)
a.get_x()

b = deepcopy(a)

b.get_x()

