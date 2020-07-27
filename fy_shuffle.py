'''
Copyright(c) 2014 YSUV - Fisher yates shuffle

MIT Licence
'''
import random


def shuffle(arr):
    for index, val in enumerate(arr):
        no = random.randrange(0, len(arr) - 1)
        arr[index], arr[no] = arr[no], arr[index]

    return arr

if __name__ == '__main__':
    print shuffle([1, 2, 3, 4, 5])
