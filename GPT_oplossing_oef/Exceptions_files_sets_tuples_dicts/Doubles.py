def double(lst):
    seen = set()
    for num in lst:
        if num in seen:
            print(num)
            return
        seen.add(num)
    print(None)

def doubles(lst):
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1

    once = {num for num, c in counts.items() if c == 1}
    multiple = {num for num, c in counts.items() if c > 1}

    print(once, multiple)