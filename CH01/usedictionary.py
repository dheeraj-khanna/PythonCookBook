from collections import defaultdict
from collections import OrderedDict
import json


def using_dictionary_by_mapping_keys():
    """
    1.6. Mapping Keys to Multiple Values in a Dictionary

    This function is showing how to create dictionary object using defaultdict of collections.keys
    More importantly it demonstrate when to use list [list] and when to use set {tuple}
    :return: None
    
    """
    # The choice of whether or not to use lists or sets depends on intended use. Use a list if
    # you want to preserve the insertion order of the items. Use a set if you want to eliminate
    # duplicates (and don’t care about the order).

    # Standard dict objects preserve order in the reference (CPython) implementations of Python
    # 3.5 and 3.6, and this order-preserving property is becoming a language feature in Python 3.7.
    # https://gandenberger.org/2018/03/10/ordered-dicts-vs-ordereddict/

    # Example creating dictionary using list

    # Normal dictionary were not ordered before 3.5

    normal_dict = {}

    normal_dict['3'] = "three"
    normal_dict['4'] = "four"
    normal_dict['5'] = "five"
    normal_dict['1'] = "one"
    normal_dict['2'] = "two"

    print("Printing normal Dictionary : ")

    for key, value in normal_dict.items():
        print("key : {0},value : {1}".format(key, value))

    d = defaultdict(list)
    d['a'].append("1")
    d['b'].append("2")
    d['c'].append("3")
    # notice this 3 will be added twice in the dictionary since this is list.
    d['c'].append("3")
    print(d)
    print("Printing list Dictionary : ")
    for key, value in d.items():
        print("key : {0},value : {1}".format(key, value))

    # Example : creating dictionary using set
    d = defaultdict(set)
    d['b'].add("2")
    d['c'].add("3")
    d['a'].add("1")
    # notice this 3 will be added only once in the dictionary since this is set.
    d['c'].add("3")
    print(d)

    print("Printing set Dictionary : ")
    for key, value in d.items():
        print("key : {0},value : {1}".format(key, value))


def using_dictionary_in_order():
    """
    You want to create a dictionary, and you also want to control the order of items when
    iterating or serializing.

    To control the order of items in a dictionary, you can use an OrderedDict from the
    collections module.
    :return: None

    """

    d = OrderedDict()

    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    print(d)
    print("Printing ordered Dictionary : ")
    for key in d:
        print(key, d[key])

    print(json.dumps(d))


def calculate_dictionary():
    """
    1.8. Calculating with Dictionaries
    You want to perform various calculations (e.g., minimum value, maximum value, sorting, etc.)
    on a dictionary of data.

    :return: None

    """

    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    print("Here is the prices dictionary ")
    print(prices)

    # Notice the out put of these function. This will give output based on
    # minimum key or values respectively not the same key-value pair
    print("Using normal minimum function ", min(prices.keys()))
    print("Using normal minimum function ", min(prices.values()))

    # correct way of getting the minimum based on values
    min_price = min(zip(prices.values(), prices.keys()))
    print("The minimum prices of the dictionary = ", min_price)

    # correct way of getting the maximum based on values
    max_price = max(zip(prices.values(), prices.keys()))
    print("The maximum prices of the dictionary = ", max_price)

    # sorting using zip
    prices_sorted = sorted(zip(prices.values(),prices.keys()))
    print("The sorted dictionary looks like = ", prices_sorted)


def find_common_in_dict():
    """
    1.9. Finding Commonalities in Two Dictionaries

    You have two dictionaries and want to find out what they might have in common (same
    keys, same values, etc.).

    :return:
    """
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    print("Common keys having in dictionary a and b =", a.keys() & b.keys())
    print("Common keys present in a but not in b dictionary  =", a.keys() - b.keys())
    print("Common keys present in b but not in a dictionary  =", b.keys() - a.keys())
    print("Common values present in a and  b dictionary  =", a.items() & b.items())

    # Make a new dictionary with certain keys removed
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c)
    # c is {'x': 1, 'y': 2}

    d = {key: b[key] for key in b.keys() - {'x', 'w'}}
    print(d)


def finding_duplicate(items, key=None):
    """
    1.10. Removing Duplicates from a Sequence while Maintaining Order

    You want to eliminate the duplicate values in a sequence, but preserve the order of the
    remaining items.

    :return:
    """

    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# calling functions
#
# using_dictionary_by_mapping_keys()
#
# using_dictionary_in_order()

# calculate_dictionary()

# find_common_in_dict()

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print(list(finding_duplicate(items=a, key=lambda d: (d['x'], d['y']))))

print(list(finding_duplicate(items=a, key=lambda d: (d['x']))))

