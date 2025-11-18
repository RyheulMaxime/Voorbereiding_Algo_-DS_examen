def zoek(gesorteerd: list, x: int):
    low = 0
    high = len(gesorteerd) - 1

    while high >= low:
        mid = (low + high) // 2
        if x < gesorteerd[mid]:
            high = mid - 1
        elif x == gesorteerd[mid]:
            return mid
        else:
            low = mid + 1

    return None
        


# def combisom(geheleLst:list, x:int):
#     for i in range(len(geheleLst)):
#         for y in range(len(geheleLst) - i - 1):
#             print(geheleLst[i],geheleLst[y + i],geheleLst[i] + geheleLst[y + i])
#             if geheleLst[i] + geheleLst[y + i] == x:
#                 return True
#     return False

def combisom(geheleLst:list, x:int):
    newLst = []
    for i in range(len(geheleLst)):
        for y in range(len(geheleLst) - i - 1):
            newLst.append(geheleLst[i] + geheleLst[y + i])
    return x in newLst

# print(combisom([1, 2, 3, 4, 5, 6], 10))
# print(combisom([3, 9, -4, 2, 5], -3))
# print(combisom([-3, 7, 9, 20, 1], 17))

def samenvoegen(geheleLst:list, geheleLst2:list):
    newLst = []
    for i in range(min(len(geheleLst),len(geheleLst2))):
        print(i)
        newLst.append(geheleLst[i])
        newLst.append(geheleLst2[i])
    return newLst

def weven(geheleLst:list, geheleLst2:list):
    newLst = []
    for i in range(max(len(geheleLst),len(geheleLst2))):
        newLst.append(geheleLst[i % len(geheleLst)])
        newLst.append(geheleLst2[i % len(geheleLst2)])
    return newLst

def ritsen(geheleLst:list, geheleLst2:list):
    newLst = []
    for i in range(max(len(geheleLst),len(geheleLst2))):
        if i <= len(geheleLst) - 1:
            newLst.append(geheleLst[i])
        if i <= len(geheleLst2) - 1:
            newLst.append(geheleLst2[i])
    return newLst

# print(samenvoegen(('A', 'B', 'C'),  [1, 2]))
# print(weven(['A', 'B'], [1, 2, 3, 4]))
# print(ritsen(('A', 'B'),  [1, 2, 3]))

def iszigzag(geheleLst:list):
    for i in range(len(geheleLst) - 1):
        if i % 2 == 0 and i != len(geheleLst) - 1:
            if geheleLst[i] < geheleLst[i + 1]:
                return False

        elif i % 2 == 1 and i != len(geheleLst) - 1:
            if geheleLst[i] > geheleLst[i + 1]:
                return False
    return True

def zigzag_traag(geheleLst:list):
    newLst = sorted(geheleLst)
    for i in range((len(newLst) - 1) // 2):
        newLst[2 * i], newLst[2 *i + 1] = newLst[2 *i + 1], newLst[2 * i]
    reeks = newLst
    # return newLst

        
# def zigzag_snel(geheleLst:list):
#     newLst = geheleLst
#     for i in range(len(newLst) - 1):
#         # print(newLst)
#         if newLst.index(newLst[i]) % 2 == 0 and newLst[i] < newLst[i - 1] and i != 0:
#             # print(newLst[i], newLst[i - 1])
#             newLst[i], newLst[i - 1] = newLst[i - 1], newLst[i]
#         if newLst.index(newLst[i]) % 2 == 0 and newLst[i] < newLst[i + 1]:
#             # print(newLst[i], newLst[i + 1], 'even')
#             newLst[i], newLst[i + 1] = newLst[i + 1], newLst[i]
    
#     reeks = newLst

def zigzag_snel(geheleLst:list):
    
    for i in range(len(reeks) - 1):
        # print(newLst)
        if i % 2 == 0 and reeks[i] < reeks[i - 1] and i != 0:
            print(reeks[i], reeks[i - 1])
            reeks[i], reeks[i - 1] = reeks[i - 1], reeks[i]
        if i % 2 == 0 and reeks[i] < reeks[i + 1] and i != len(reeks) - 1:
            print(reeks[i], reeks[i + 1], 'even')
            reeks[i], reeks[i + 1] = reeks[i + 1], reeks[i]
    
    
    # return newLst


print(iszigzag([100, 100, 200, 200, 1000, 0, 0, 0]))
reeks = [79, 68, 73, -27, 16, -3, 45, 62, -12, -13, 35, 49, -31]
# print(zigzag_traag(reeks))
zigzag_snel(reeks)
print(reeks)