from collections import deque

def dequeExample():
    """
    Using deque(maxlen=N) creates a fixed-sized queue. When new items are added and
    the queue is full, the oldest item is automatically removed. For example:

    # =====================================Keeping the Last N Items===
    :return:

    """

    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)

    print("Queue values =", q)
    print("# ==================================================================================== #")
    q.append(4)
    print("After adding 4 queue values =", q)
    print("# ==================================================================================== #")

    # ==================Finding the Largest or Smallest N Items===
    # =====Problem: You want to make a list of the largest or smallest N items in a collection.
    import heapq
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print("Original list number = ", nums)
    print("Three largest number = ", heapq.nlargest(3, nums))
    print("Three largest number = ", heapq.nsmallest(3, nums))

    print("# ==================================================================================== #")

    letters = ['z', 'x', 'y', 'a', 'b', 'c', 'u', 'v']
    print("Original list letters = ", letters)
    print("Three largest letters = ", heapq.nlargest(3, letters))
    print("Three largest letters = ", heapq.nsmallest(3, letters))


# ===================================Calling Functions====
dequeExample()