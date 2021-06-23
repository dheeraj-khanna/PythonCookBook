from collections import deque
import heapq


def dqexample():
    """

    Using deque(maxlen=N) creates a fixed-sized queue. When new items are added and
    the queue is full, the oldest item is automatically removed. For example:

    # =====================================Keeping the Last N Items===
    :return:

    """

    # let us heapify

    print("# ==================================================================================== #")
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print("Original list number ", nums)
    heapList = list(nums)
    print("Before heapify the heapifyList looks like this ", heapList)
    heapq.heapify(heapList)
    print("After heapify the numbers looks like this ", heapList)

    print("After heapify the numbers the popping of items comes out like this ")
    poppedListnum = []
    for index in range(len(nums)):
        poppedListnum.append(heapq.heappop(heapList))

    print(poppedListnum)

# ===================================Calling Functions====
dqexample()