import random
import math
from threading import Thread
scratch = None


def merge_sort(start, end, input):
    global scratch

    if start == end:
        return

    mid = start + math.floor((end - start) / 2)

    # sort first half
    worker1 = Thread(target=merge_sort, args=(start, mid, input))

    # sort second half
    worker2 = Thread(target=merge_sort, args=(mid + 1, end, input))

    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()

    # merge the two sorted arrays
    i = start
    j = mid + 1

    for k in range(start, end + 1):
        scratch[k] = input[k]

    k = start
    while k <= end:

        if i <= mid and j <= end:
            input[k] = min(scratch[i], scratch[j])

            if input[k] == scratch[i]:
                i += 1
            else:
                j += 1

        elif i <= mid and j > end:
            input[k] = scratch[i]
            i += 1
        else:
            input[k] = scratch[j]
            j += 1

        k += 1


def create_data(size):
    unsorted_list = [None] * size
    random.seed()

    for i in range(0, size):
        unsorted_list[i] = random.randint(0, 1000)

    return unsorted_list


def print_list(lst):
    end = len(lst)
    for i in range(0, end):
        print(lst[i], end=" ")


if __name__ == "__main__":
    size = 12
    scratch = [None] * size
    unsorted_list = create_data(size)

    print_list(unsorted_list)
    merge_sort(0, size - 1, unsorted_list)
    print("\n\n")
    print_list(unsorted_list)
