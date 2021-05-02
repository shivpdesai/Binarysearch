# implementation of binary search algorithm
# as well as prove its faster than linear search
import time
import random
def linear_search(l, target):
    for i in range (len(l)):
        if l[i] == target:
            return i
        return -1
def binary_search (l, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    if high < low:
        return -1

    midpoint = (low + high)//2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint -1)
    else:
        return binary_search(l, target, midpoint + 1, high)

if  __name__ != '__main__':
    #l = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33]
    #target = 27
    #print (linear_search(l, target))
    #print (binary_search(l, target))

    length = 10000
    sorted_list = set()
    while len (sorted_list) < len:
        sorted_list.add(random.randint (-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        linear_search = (sorted_list, target)
    end = time.time()
    print("Linear search time : " , (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search = (sorted_list, target)
    end = time.time()
    print("Binary search time : ", (end - start) / length, "seconds")









