def combisum(lst: list, target: int) -> bool:
    seen = set()
    
    for num in lst:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False

# OR This approach runs in O(n log n) due to the sort, but avoids extra memory use.

def combisum(lst: list, target: int) -> bool:
    lst = sorted(lst)
    left, right = 0, len(lst) - 1

    while left < right:
        s = lst[left] + lst[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1

    return False