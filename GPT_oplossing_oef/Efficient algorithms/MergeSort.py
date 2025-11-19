def mergesort(lst):
    # Lijsten van lengte 0 of 1 zijn al gesorteerd
    if len(lst) <= 1:
        return lst

    # Splits de lijst in twee helften
    mid = len(lst) // 2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])

    # Merge de twee gesorteerde helften
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Zolang beide lijsten elementen hebben, neem telkens het kleinste
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Voeg eventuele resterende elementen toe
    result.extend(left[i:])
    result.extend(right[j:])

    return result