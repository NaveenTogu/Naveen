
def top():
    n = 1
    while n<=a:
        sq = n*n

        yield sq
        n += 1

values = top()

a = int(input('TOP '))
for i in values:
    print(i)