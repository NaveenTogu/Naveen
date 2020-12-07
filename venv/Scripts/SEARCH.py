pos = -1
def search(lst, a):

    l = 0
    u = len(lst)-1
    while l<=u:
        mid = (l+u)//2
        if lst[mid] == a:
            globals()['pos'] = mid+1
            return True
        else:
            if lst[mid] < a:
                l = mid+1
            else:
                u = mid-1

    return False



list = [1, 3, 5, 6, 48, 45]
list.sort()
n = int(input('FIND NUMBER '))


if search(list, n):
    print('Found at', pos, end = "")
    if pos>=4:
        print("'th position!!!")
    else:
        if pos==1:
            print("'st position!!!")
        if pos==2:
            print("'nd position!!!")
        if pos==3:
            print("'rd position!!!")
else:
    print('Not Found   ', ':-( :-( :-( :-(')
