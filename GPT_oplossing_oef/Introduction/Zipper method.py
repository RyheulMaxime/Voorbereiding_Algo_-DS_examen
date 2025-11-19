def merge(seq1, seq2):
    result = []
    n = min(len(seq1), len(seq2))
    for i in range(n):
        result.append(seq1[i])
        result.append(seq2[i])
    return result

def weave(seq1, seq2):
    result = []
    n = max(len(seq1), len(seq2))
    len1, len2 = len(seq1), len(seq2)

    for i in range(n):
        result.append(seq1[i % len1])
        result.append(seq2[i % len2])

    return result

def zipper(seq1, seq2):
    result = []
    len1, len2 = len(seq1), len(seq2)
    n = min(len1, len2)

    # First: alternate until shortest is done
    for i in range(n):
        result.append(seq1[i])
        result.append(seq2[i])

    # Then: append leftovers from the longer sequence
    if len1 > len2:
        result.extend(seq1[n:])
    else:
        result.extend(seq2[n:])

    return result