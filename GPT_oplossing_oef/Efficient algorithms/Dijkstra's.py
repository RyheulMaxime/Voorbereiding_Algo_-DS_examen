def shortest_path(graph, src, dest):
    # from priority_queue import PriorityQueue

    # Distance dictionary: kortste bekende afstanden vanaf src
    dist = {node: float('inf') for node in graph.get_nodes()}
    dist[src] = 0

    # Voor reconstructie van het pad
    prev = {}

    # PriorityQueue op basis van afstand
    pq = PriorityQueue(sortkey=lambda node: dist[node])
    pq.push(src)

    visited = set()

    while not pq.is_empty():
        u = pq.pop()

        # Als we dest bereikt hebben met minimale afstand → klaar
        if u == dest:
            break

        if u in visited:
            continue
        visited.add(u)

        # Voor elke uitgaande edge
        for edge in graph.get_out_edges(u):
            w = edge.get_end()           # buur
            weight = edge.get_weight()   # positief gewogen

            # Relaxatiestap
            new_dist = dist[u] + weight
            if new_dist < dist[w]:
                dist[w] = new_dist
                prev[w] = u
                pq.push(w)

    # Is dest onbereikbaar?
    if dist[dest] == float('inf'):
        return []   # of None, maar lijst is gevraagd

    # Reconstructie van het pad (achterwaarts)
    path = []
    cur = dest
    while cur != src:
        path.append(cur)
        cur = prev[cur]
    path.append(src)

    path.reverse()
    return path



import heapq
from functools import total_ordering

@total_ordering
class SpecialSorted:

    def __init__(self, element, value):
        self.element = element
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

class PriorityQueue:

    def __init__(self, sortkey = lambda x : x):
        self.content = []
        self.sortkey = sortkey

    def add(self, item):
        heapq.heappush(self.content, SpecialSorted(item, self.sortkey(item)))

    def peek(self):
        return self.content[0].element if self.content else None

    def poll(self):
        return heapq.heappop(self.content).element if len(self.content) > 0 else None

    def is_empty(self):
        return len(self.content) == 0

    def __str__(self):
        return str(heapq.nsmallest(len(self.content), [item.element for item in self.content]))