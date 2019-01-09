import sys
from nose.tools import *
from random import randint
sys.path.append("C:/Users/xiao0/projects_pro")
from ex16.ex16.ex16 import *
from ex14.ex14.ex14 import DLList


max_numbers = 5

def random_list(count):
    numbers = DLList()
    for i in range(count, 0, -1):
        # numbers.shift(i)
        numbers.shift(randint(0, 10))
    return numbers

def is_sorted(numbers):
    node = numbers.begin
    while node and node.next:
        if node.value > node.next.value:
            return False
        else:
            node = node.next
            
    return True

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_bubble_sort():
    numbers = random_list(max_numbers)
    bubble_sort(numbers)
    assert is_sorted(numbers)

def test_merge_sort():
    numbers = random_list(max_numbers)
    merge_sort(numbers)
    assert is_sorted(numbers)

def test_quick_sort():
    numbers = random_list(max_numbers)
    print_all(numbers.begin)
    quick_sort(numbers)
    assert is_sorted(numbers)