import sys
sys.path.append("C:/Users/xiao0/projects_pro")
from ex14.ex14.ex14 import DLList


def bubble_sort(numbers):
    """Sorts a list of numbers using bubble sort."""
    while True:
        # 最开始假设它是有序的
        is_sorted = True
        # 一次比较两个，跳过头部
        node = numbers.begin.next
        while node:
            # 遍历并将当前节点与上一个比较
            if node.prev.value > node.value:
                # 如果上一个更大，我们需要交换
                node.prev.value, node.value = node.value, node.prev.value
                # 这表示我们需要再次扫描
                is_sorted = False
            node = node.next

        # 它在顶部重置过，但是如果我们没有交换，那么它是有序的
        if is_sorted: break

def merge_sort(numbers):
    length = numbers.count()
    if length <= 1:
        return numbers

    left = DLList()
    right = DLList()
    count = 0
    node = numbers.begin
    
    while count < length / 2:
        count += 1
        node = node.next

    left.begin = numbers.begin
    node.prev.next = None
    left.end = node.prev

    right.end = numbers.end
    node.prev = None
    right.begin = node

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left ,right):
    result = DLList()
    
    while left.begin and right.begin:
        if left.begin.value < right.begin.value:
            item = left.unshift()
            result.push(item)
        else:
            item = right.unshift()
            result.push(item)

    if left.begin:
        node = left.begin
        node.prev = result.end
        result.end.next = node
        result.end = left.end
    elif right.begin:
        node = right.begin
        node.prev = result.end
        result.end.next = node
        result.end = right.end
    else:
        print('ERROR!')

    return result

def count(node):
    if node == None:
        return 0

    i = 1
    while node.next:
        i += 1
        node = node.next

    return i

def find_end(node):
    if node == None:
        return None

    while node.next:
        node = node.next

    return node

def find_head(node):
    if node == None:
        return None

    while node.prev:
        node = node.prev

    return node

def quick_sort(numbers):
    numbers.begin = quick_sort_node(numbers.begin)
    numbers.end = find_end(numbers.begin)

def combine_node(node_a, node_b):
    find_end(node_a).next = node_b
    node_b.prev = find_end(node_a)
    return find_head(node_b)

def print_all(node):
    print('='*15)
    if node == None:
        print('None!')
        return None
    else:
        node = find_head(node)
        print(node, end=' | ')
    while node.next:
        node = node.next
        print(node, end=' | ')
    print()

def quick_sort_node(node):
    # print_all(node)
    if count(node) <= 1:
        return node
    pivot = node
    print('============before while=======')
    i = 0
    while node.next and i < 1:
        i += 1
        print('-'*40)
        print_all(node)
        # print_all(node)
        # print('node: ', node)
        # print('node.next: ', node.next)
        if node.next.value < pivot.value:
            nn = node.next
            nnn = node.next.next
            nnp = node.next.prev
            node.next.prev.next = nnn
            if node.next.next:
                node.next.next.prev = nnp
            node.next.next = pivot
            node.next.prev = pivot.prev
            if pivot.prev:
                pivot.prev.next = node.next
            pivot.prev = node.next
            node = nn
            # sys.exit(1)
        else:
            node = node.next
            sys.exit(1)
        print('+'*40)
        print_all(node)
        sys.exit(1)
        # print('node.next111: ', node.next)

    print('============after while=======')
    # print_all(node)
    if pivot.prev == None:
        print('pivot: ', pivot)
        pivot_next = pivot.next
        pivot_next.prev = None
        pivot.next = None
        return combine_node(pivot, quick_sort_node(pivot_next))
    elif pivot.next == None:
        pivot_prev = pivot.prev
        pivot_prev.next = None
        pivot.prev = None
        return combine_node(quick_sort_node(find_head(pivot_prev)), pivot)
    elif pivot.prev and pivot.next:
        print('and pivot: ', pivot)

        pivot_next = pivot.next
        pivot_next.prev = None
        pivot.next = None
        step = combine_node(pivot, quick_sort_node(pivot_next))

        pivot_prev = pivot.prev
        pivot_prev.next = None

        return combine_node(quick_sort_node(find_head(pivot_prev)), step)
    else:
        print('ERROR!!') 
        sys.exit(1)       
    

        

            # pp = pivot.prev
            # pn = pivot.next
            # nnp = node.next.prev
            # nnn = node.next.next
            # if pivot.prev:
            #     pivot.prev.next = node.next
            # pivot.next.prev = node.next
            # node.next.prev.next = pivot
            # if node.next.next:
            #     node.next.next.prev = pivot
            # pivot.prev = nnp
            # pivot.next = nnn
            # node.next.prev = pp
            # node.next.next = pn
