def sort(lijst):

    def quicksort(a, left, right):
        if left >= right:
            return

        # Hoare partition
        pivot = a[(left + right) // 2]
        i, j = left, right

        while i <= j:
            while a[i] < pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        # Recursively sort partitions
        quicksort(a, left, j)
        quicksort(a, i, right)

    quicksort(lijst, 0, len(lijst) - 1)