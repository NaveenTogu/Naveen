a = int(input("A = "))
b = int(input("B = "))
try:
    print("HELLO")
    print(a/b)



except ZeroDivisionError as e:
    print('HEY, You cannot divide by zero')
    print('Hence the problem is', e)
except ValueError as e:
    print('Invalid Input')
except Exception as e:
    print('SOMETHING WENT WRONG....')

finally:

    try:
        k = int(input('k = '))
        print(k)
    except ValueError as e:
        print('Invalid Input')
    except Exception as e:
        print('SOMETHING WENT WRONG....')
    finally:
        print('BYE')