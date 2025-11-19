def sorteer(rij):
    n = len(rij)
    size = 1   # start met blokken van grootte 1 (enkel element)

    # Helperfunctie voor het mergen van twee gesorteerde subarrays
    def merge(left, mid, right):
        temp = []
        i, j = left, mid

        while i < mid and j < right:
            if rij[i] <= rij[j]:
                temp.append(rij[i])
                i += 1
            else:
                temp.append(rij[j])
                j += 1

        # Voeg resterende elementen toe
        temp.extend(rij[i:mid])
        temp.extend(rij[j:right])

        # Schrijf terug in de originele lijst
        rij[left:right] = temp

    # Iteratief blokken mergen
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(left + size, n)
            right = min(left + 2*size, n)
            merge(left, mid, right)
        size *= 2
