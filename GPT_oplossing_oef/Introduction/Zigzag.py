def iszigzag(seq):
    n = len(seq)
    for i in range(n):
        if i % 2 == 0:   # even index
            if i > 0 and seq[i] < seq[i-1]:
                return False
            if i+1 < n and seq[i] < seq[i+1]:
                return False
        else:            # odd index
            if seq[i] > seq[i-1]:
                return False
            if i+1 < n and seq[i] > seq[i+1]:
                return False
    return True

def zigzag_slow(lst):
    lst.sort()
    for i in range(0, len(lst)-1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]

def zigzag_fast(lst):
    n = len(lst)
    for i in range(0, n, 2):  # only even positions
        # step 1: compare with previous odd
        if i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
        # step 2: compare with next odd
        if i+1 < n and lst[i] < lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]