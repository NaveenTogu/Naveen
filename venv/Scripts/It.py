class Top():

    def __init__(self):
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.x <= a:
            val = self.x
            self.x += 1

            return val
        else:
            raise StopIteration

a = int(input('Top '))
values = Top()

print(next(values))
for i in values:
    print(i)
