
f = open('LION.jpg', 'rb')
f1 = open('LEO.jpg', 'wb')
for i in f:
    f1.write(i)

