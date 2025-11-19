class TaskNode:
    def __init__(self, task_name, duration, priority):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = None

    def __repr__(self):
        return f"({self.task_name}, dur={self.duration}, prio={self.priority})"
    
import csv

class TaskLinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, task_name, duration, priority):
        new_node = TaskNode(task_name, duration, priority)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node
    
    def remove_task(self, task_name):
        cur = self.head
        prev = None

        while cur:
            if cur.task_name == task_name:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next

        return False
    
    def display_tasks(self):
        cur = self.head
        while cur:
            print(f"Task: {cur.task_name}, Duration: {cur.duration}, Priority: {cur.priority}")
            cur = cur.next

    def find_task(self, task_name):
        cur = self.head
        while cur:
            if cur.task_name == task_name:
                return cur
            cur = cur.next
        return None
    
    def calculate_total_duration(self):
        total = 0
        cur = self.head
        while cur:
            total += cur.duration
            cur = cur.next
        return total

    def read_tasks_from_csv(self, file_path):
        with open(file_path, newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header

            for name, duration, priority in reader:
                self.add_task(name, int(duration), int(priority))


    def reorder_tasks_by_priority(self):
        new_head = None
        cur = self.head

        while cur:
            next_node = cur.next
            cur.next = None
            new_head = self.sorted_insert_by_priority(new_head, cur)
            cur = next_node

        self.head = new_head

    def reorder_tasks_by_priority_duration(self):
        new_head = None
        cur = self.head

        while cur:
            next_node = cur.next
            cur.next = None
            new_head = self.sorted_insert_by_priority_duration(new_head, cur)
            cur = next_node

        self.head = new_head


        
    def sorted_insert_by_priority(self, head, node):
            if head is None or node.priority < head.priority:
                node.next = head
                return node

            cur = head
            while cur.next and cur.next.priority <= node.priority:
                cur = cur.next

            node.next = cur.next
            cur.next = node
            return head

    def sorted_insert_by_priority_duration(self, head, node):
            if (head is None or 
                node.priority < head.priority or
                (node.priority == head.priority and node.duration < head.duration)):
                node.next = head
                return node

            cur = head
            while (cur.next and 
                (cur.next.priority < node.priority or
                    (cur.next.priority == node.priority and cur.next.duration <= node.duration))):
                cur = cur.next

            node.next = cur.next
            cur.next = node
            return head



tasks = TaskLinkedList()
tasks.add_task("Assemble", 20, 2)
tasks.add_task("Paint", 30, 3)
tasks.add_task("Quality Check", 10, 1)

print("Before sort:")
tasks.display_tasks()

tasks.reorder_tasks_by_priority_duration()

print("\nAfter sort:")
tasks.display_tasks()

print("\nTotal duration:", tasks.calculate_total_duration())