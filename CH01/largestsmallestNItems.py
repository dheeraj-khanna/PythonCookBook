from collections import deque
import heapq

def findlargestorsmallestnitem():

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

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print("Original list number = ", nums)
    print("Three largest number = ", heapq.nlargest(3, nums))
    print("Three smallest number = ", heapq.nsmallest(3, nums))

    print("# ==================================================================================== #")

    letters = ['z', 'x', 'y', 'a', 'b', 'c', 'u', 'v']
    print("Original list letters = ", letters)
    print("Three largest letters = ", heapq.nlargest(3, letters))
    print("Three smallest letters = ", heapq.nsmallest(3, letters))

    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print("Original shares in portfolio = ", portfolio)
    print("Three high price shares      = ", heapq.nlargest(3, portfolio, key=lambda s: s['price']))
    print("Three lowest price shares    = ", heapq.nsmallest(3, portfolio, key=lambda s: s['price']))

findlargestorsmallestnitem()