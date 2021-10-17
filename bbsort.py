import time
import random

def bsort(a):
    n = len(a)

    for i in range(n-1):
        flag = 0

        for j in range(n-1):
            if a[j] >a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
                flag = 1

        if flag == 0:
            break
    return a

def bsort_inv(a):
    n = len(a)

    for i in range(n-1):
        flag = 0

        for j in range(n-1):
            if a[j] <a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
                flag = 1

        if flag == 0:
            break
    return a

print('Welcome to Python Bubblesorter.')
print(    )

i = 0
x = 50
order = 1

while i  == 0:
    option = input('What is bubble sort? or move on: ')
    if option == 'What is bubble sort?' or  option ==  'What is bubble sort':
        print('What is bubblesort you say?. Well bubble sort is a type of sorting algorithm that')
        print('goes through the elements of a/an number list/array, compares them and swaps')
        print('them if the first element is bigger than the second. This algorithm will run through')
        print('the entire list until all elemnts are arranged from smallest to biggest or if you want')
        print('you can change the order from smallest to bigges to biggest to smallest. So lets go!.')

    elif option == 'move on':
        print('Lets go')
        time.sleep(2)
        i = 1

        v = 0
        while v == 0:
            print('pick an option')
            print('1 for create list')
            print('2 for random list')
            print('3 for settings')
            Option = int(input('or 4 for to exit: '))

            if Option == 1:
                time.sleep(2)
                length = int(input('type the length for your list: '))
                leng = range(1, length + 1)
                l = []
                time.sleep(2)

                for i in leng:
                    num = int(input('please type in a number: '))
                    l.append(num)

                print('the given list is:')
                print(l)
                if order == 1:
                    bsort(l)

                elif order == 2:
                    bsort_inv(l)
                    
                print('the sorted list is:')
                print(l)

            elif Option == 2:
                time.sleep(2)
                length = int(input('type the length for your list: '))
                leng = range(1, length + 1)
                l = []
                time.sleep(2)

                for i in leng:
                    num = random.randrange(1,x+1)
                    l.append(num)
                    
                print('the given list is:')
                print(l)
                if order == 1:
                    bsort(l)

                elif order == 2:
                    bsort_inv(l)
                    
                print('the sorted list is:')
                print(l)

            elif Option == 3:
                time.sleep(2)
                print()
                print('\t  Welcome to settings')
                e=0
                while e == 0:
                    print('What would you like to do?: ')
                    print('1 for changing the order of sorting')
                    print('2 for changing random list number range')
                    op = int(input('or 3 to exit settings : '))
                    time.sleep(2)
                    if op == 1:
                        print('pick an option')
                        print()
                        print('1 for ascending order.')
                        odr = int(input('2  for descending order: '))
                        order = odr

                    elif op == 2:
                        x = int(input('please enter number range: '))

                    elif op == 3:
                        e = 1

                    else:
                        print('sorry, that is not an option.')

            elif Option == 4:
                print('Thank you :)')
                v = 1

    else:
        print('sorry that is not an option.')
        



    
