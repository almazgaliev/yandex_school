from typing import List


def foo(arr: List[int], s: int) -> int:
    le = -1
    if(any(map(lambda x: x > s, arr))):
        return le
    left = arr.index(max(arr))
    right = left+1

    while(sum(arr[left:right]) < s):
        left_safe = 0 if(left - 1 < 0) else left - 1
        right_safe = len(arr) if(right + 1 > len(arr)) else right + 1

        if(arr[left_safe] > arr[right_safe]):
            left -= 1
        else:
            right += 1
    le = right-left
    return le, arr[left:right]


def bar(arr: List[int], s: int) -> int:
    pass


l, su = map(int, input('len, sum:').split())

arr = [int(input()) for _ in range(l)]
print(foo(arr,su))
