########################################### 1: Merge sort #############################################################
from grah_library import DirectedGraph


def mergesort(list):
    sortedList = list
    if len(list) > 1:
        # Merge sort the first half
        firstHalf = list[ : len(list) // 2]
        mergesort(firstHalf)

        # Merge sort the second half
        secondHalf = list[len(list) // 2 : ]
        mergesort(secondHalf)
        
        # Merge firstHalf with secondHalf into list
        sortedList = merge(firstHalf, secondHalf, list)

    return sortedList

# Merge two sorted lists */
def merge(list1, list2, temp):
    current1 = 0  # Current index in list1
    current2 = 0  # Current index in list2
    current3 = 0  # Current index in temp

    while current1 < len(list1) and current2 < len(list2):
        if list1[current1] < list2[current2]:
            temp[current3] = list1[current1]
            current1 += 1
            current3 += 1
        else:
            temp[current3] = list2[current2]
            current2 += 1
            current3 += 1

    while current1 < len(list1):
        temp[current3] = list1[current1]
        current1 += 1
        current3 += 1

    while current2 < len(list2):
        temp[current3] = list2[current2]
        current2 += 1
        current3 += 1
    # print(temp)
    return temp

# print(mergesort([45, 12, 23, 47, 72, 49, 18, 78]))

############################################## 2: MergeSort non-recursive ############################################
def sorteer(rij: list):
    n = len(rij)
    stap = 1  # begin met sublijsten van grootte 1

    # Blijf doorgaan tot de stapgrootte groter is dan de lijst
    while stap < n:
        for start in range(0, n, 2 * stap):
            midden = start + stap
            einde = min(start + 2 * stap, n)
            
            # splits in twee gesorteerde sublijsten
            links = rij[start:midden]
            rechts = rij[midden:einde]
            
            # merge ze terug in rij[start:einde]
            i = j = 0
            k = start
            while i < len(links) and j < len(rechts):
                if links[i] <= rechts[j]:
                    rij[k] = links[i]
                    i += 1
                else:
                    rij[k] = rechts[j]
                    j += 1
                k += 1

            # eventuele restjes van links of rechts toevoegen
            while i < len(links):
                rij[k] = links[i]
                i += 1
                k += 1
            while j < len(rechts):
                rij[k] = rechts[j]
                j += 1
                k += 1

        stap *= 2  # verdubbel de grootte van de blokken


# Voorbeeld:
# lijst = [5, 2, 9, 1, 5, 6]
# sorteer(lijst)
# print(lijst)


##################################################### 3: Quicksort ###################################################
def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1)

def quickSortHelper(lst, first, last):
    if last > first:
        pivotIndex = partition(lst, first, last)
        quickSortHelper(lst, first, pivotIndex - 1)
        quickSortHelper(lst, pivotIndex + 1, last)

# Partition lst[first.last]
def partition(lst, first, last):
    pivot = lst[first]  # Choose the first element as the pivot
    low = first + 1  # Index for forward search
    high = last  # Index for backward search

    while high > low:
        # Search forward from left
        while low <= high and lst[low] <= pivot:
            low += 1

        # Search backward from right
        while low <= high and lst[high] > pivot:
            high -= 1

        # Swap two elements in the list
        if high > low:
            lst[high], lst[low] = lst[low], lst[high]

    while high > first and lst[high] >= pivot:
        high -= 1

    # Swap pivot with lst[high]
    if pivot > lst[high]:
        lst[first] = lst[high]
        lst[high] = pivot
        return high
    else:
        return first

# A test function 
# def main():
#     lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
#     quickSort(lst)
#     for v in lst:
#         print(v, end = " ")

# main()


######################################## 4: Dijkstra shortest path  #############################################
# import heapq
# from functools import total_ordering
from grah_library import *

def shortest_path(graph, src, dest):
    # nodes = {}
    nodes = {node: (float('inf'), None) for node in graph.get_all_nodes()}
    # for node in graph.get_all_nodes():
    #     nodes[node] = (float('inf'), None)
    # print(nodes)

    nodes[src] = (0, "Source")

    permanent_nodes = set()

    while src != dest:
        # current_node = min(nodes, key=lambda k: nodes[k][0])
        current_node = min((n for n in nodes if n not in permanent_nodes), key=lambda k: nodes[k][0])
        # print(current_node, nodes[current_node])

        current_dist = nodes[current_node][0]

        # graph.get_outgoing_edges(current_node)
        for edge in graph.get_outgoing_edges(current_node):
            edge.get_destination()
            # print(edge.weight, type(edge.weight), edge.get_destination())
            if current_dist + int(edge.weight) < nodes[edge.get_destination()][0]:
                nodes[edge.get_destination()] = (current_dist + edge.weight, current_node)
                # print(nodes)

        permanent_nodes.add(current_node)
        src = current_node

    # print(nodes)


    # Determine path to dest
    path = []
    node = dest
    if nodes[dest][0] == float('inf'):
        return None  # No path exists

    while node is not None:
        path.append(node)
        if nodes[node][1] == 'Source':
            break
        node = nodes[node][1]

    path.reverse()

    # return path, nodes[dest][0]
    return path


graph = directed_graph_from_dict({'Alice': ['Bob'], 'Bob': [], 'Carol': ['Alice', 'Bob']}, weights = {('Alice', 'Bob'): 5, ('Carol', 'Bob'): 4, ('Carol', 'Alice'): 5})
src = graph.get_node_from_name('Carol')
dest = graph.get_node_from_name('Alice')

# print(shortest_path(graph, src, dest))

# plan:
# 1: Select current node
# 2: determine

# [Node('Carol'), Node('Alice')]


############################################# 5: Parking simulator ####################################################
import heapq


class PriorityQueue:
    def __init__(self):
        self.content = []

    def add(self, item):
        heapq.heappush(self.content, item)

    def peek(self):
        return self.content[0]

    def poll(self):
        return heapq.heappop(self.content) if len(self.content) > 0 else None

    def is_empty(self):
        return len(self.content) == 0

    def __str__(self):
        return str(heapq.nsmallest(len(self.content), self.content))



def simuleer_parking(aantaParkeerplaatsen:int, blokTijd:int, klanten:list):

    parkeer_plaatsen = []

    while len(parkeer_plaatsen) < aantaParkeerplaatsen:
        parkeer_plaats = PriorityQueue()
        parkeer_plaatsen.append(parkeer_plaats)

    print(parkeer_plaatsen)

    klanten_gesorteerd = sorted(klanten)

    verlopen_tijd = 0

    while len(klanten_gesorteerd) > 0:
        aankomst_klant = klanten_gesorteerd[0][0]
        # print(aankomst_klant)
        print(verlopen_tijd)
        if aankomst_klant <= verlopen_tijd:
            print(klanten_gesorteerd)
            added_to_queue = False
            for queue in parkeer_plaatsen:
                if (queue.is_empty() or queue.peek() <= verlopen_tijd) and added_to_queue == False :
                    queue.poll()
                    queue.add(klanten_gesorteerd[0][1] + verlopen_tijd)
                    klanten_gesorteerd.pop(0)
                    added_to_queue = True
                    print(queue.peek())
            if added_to_queue == False:
                klanten_gesorteerd[0] = (aankomst_klant + blokTijd, klanten_gesorteerd[0][1])
                klanten_gesorteerd = sorted(klanten_gesorteerd)
        # print(klanten_gesorteerd[0][0])
        if len(klanten_gesorteerd) != 0 and klanten_gesorteerd[0][0] > verlopen_tijd:
            verlopen_tijd += 1

    max_value = 0
    for queue in parkeer_plaatsen:
        if not queue.is_empty() and queue.peek() > max_value:
            max_value = queue.peek()
    return max_value


# print(simuleer_parking(1, 5, [(0, 5), (4, 5), (5, 3), (10, 10)]))
print(simuleer_parking(10, 4, [(12, 6), (11, 10), (6, 3), (10, 3), (36, 8), (63, 7), (57, 5), (50, 9), (32, 4), (44, 3), (68, 10), (29, 5), (10, 10), (68, 10), (56, 2), (35, 8), (25, 2), (58, 9), (17, 8), (51, 3), (36, 9), (69, 3), (21, 4), (34, 10), (63, 4), (41, 6), (27, 3), (67, 3), (44, 7), (48, 1)]))
# print(simuleer_parking(2, 5, [(0, 5), (4, 8), (4, 5), (4, 4), (8, 9),(10, 3),(10, 10)]))

# queue = PriorityQueue()
# print(queue.is_empty())
# queue.add(3)
# queue.add(2)
# print(queue.peek())
# print(queue.poll())
# print(queue.peek())