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
