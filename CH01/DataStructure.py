from collections import deque


def unpack():
    """
    Unpacking a Sequence into Separate Variables

    You have an N-element tuple or sequence that you would like to unpack into a collection
    of N variables

    :param data: any data type
    :return: the same data type as unpacked

    """

    # create and unpack a tuple with numbers
    p = (4, 5)
    x, y = p
    print(x, y)
    print("# ==================================================================================== #")

    # create and unpack a list having mix data
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name, " ", shares, " ", price, " ", date)
    print("# ==================================================================================== #")

    # create and unpack a string

    s = "Hello World !"
    a, b, c, d, e, f, g, h, i, j, k,l, m = s
    print(s)
    print(a,b,c,d,e,f,g,h,i,j,k,l,m)
    print("# ==================================================================================== #")

    # When unpacking, you may sometimes want to discard certain values. Python has no special syntax
    # for this, but you can often just pick a throwaway variable name for it. For example:
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    __, shares,__, date = data
    print(shares, " ", date)
    print("# ==================================================================================== #")


def unpackNelements():
    """
    Unpacking Elements from Iterables of Arbitrary Length

    Problem :
    You need to unpack N elements from an iterable, but the iterable may be longer than N
    elements, causing a “too many values to unpack” exception.

    :return: None

    """

    # assume these are the marks of the student in 10 subject
    # we need to calculate average marks based marks obtained
    # second subject to second last subject
    grades = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # notice star in the second variable. That will create a list of marks from 20 to 90
    first, *second , last = grades
    avgMarks = sum(second) / len(grades)
    print("The avg marks of the student = ", avgMarks)
    print("# ==================================================================================== #")
    # ===============================another example===

    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212','671-923-7508')
    name, email_addr, *phone_numbers = record
    print(name, email_addr, *phone_numbers)
    # ========================using star syntax on list of tupels===

    records = [
        ('Female', 'FLora  ',47, 1974),
        ('Female', 'Linda  ',21, 2000),
        ('Female', 'Melinda',21, 2000),
        ('Male  ', 'Duffin ',47, 1974),
        ('Male  ', 'Markus ',21, 2000),
        ('Male  ', 'Jhon   ',21, 2000),
    ]

    print("# ==================================================================================== #")
    print("Sex   ","Name  ","Age    ", "DOB    ")

    def print_female(x, y, z):
        print('Female', x, y, z)

    def print_male(x, y, z):
        print('Male', x, y, z)

    for tag, *args in records:

        if tag == "Female":
            print_female(*args)

        if tag == "Male":
            print_male(*args)

    print("# ==================================================================================== #")

    # Star unpacking can also be useful when combined with certain kinds of string processing operations,
    # such as splitting for example

    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(":")
    print(uname, " - ", homedir, " - ", sh)
    print("# ==================================================================================== #")

    # =====================================Keeping the Last N Items===

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

# unpack()

unpackNelements()