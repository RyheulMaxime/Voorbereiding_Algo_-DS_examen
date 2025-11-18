

class LinkedListNode:
    def __init__(self, task_name, duration, priority, next = None):
        # task_name(string): the name of the task.
        self.task_name = task_name
        # duration(int): the duration of the task in minutes.
        self.duration = duration
        # priority(int): the priority of the task(1 is highest priority, higher numbers are lower priority).
        self.priority = priority
        # next(pointer): a reference to the next node in the linked list.
        self.next = next


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    # add_task(task_name, duration, priority): Adds a new task to the end of the list.
    def add_task(self, task_name, duration, priority):
        last_node = self.__tail
        new_node = LinkedListNode(task_name, duration, priority)

        if last_node is None:
            self.__head = new_node
        else:
            last_node.next = new_node
            # print(self.__tail.task_name)

        self.__tail = new_node

    def add_tasks_index(self, index, task_name, duration, priority):
        selected_index = 1
        selected_task = self.__head
        if index == 0:
            new_node = LinkedListNode(task_name, duration, priority, selected_task)
            self.__head = new_node
            return None

        while selected_index < index and selected_task.next is not None:
            selected_index += 1
            selected_task = selected_task.next

        new_node = LinkedListNode(task_name, duration, priority, selected_task.next)
        if selected_task.next is None:
            self.__tail = new_node

        selected_task.next = new_node
        return None

    # remove_task(task_name): Removes a task with the given name from the list.
    # 1: remove task
    # 2: adjust next parameters
    def remove_task(self, task_name):
        start = self.__head
        previous_node = None
        while start.task_name != task_name:
            previous_node = start
            start = start.next

        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None

        if previous_node is None:
            self.__head = start.next
        else:
            next_node = start.next
            previous_node.next = next_node
            if next_node is None:
                self.__tail = previous_node


    # display_tasks(): Prints all tasks in the linked list in the order they appear.
    def display_tasks(self):
        current = self.__head

        while current is not None:
            print(current.task_name)
            current = current.next

    # find_task(task_name): Searches for a task by name and returns its details.
    def find_task(self, task_name):
        start = self.__head

        while start is not None and start.task_name != task_name:
            start = start.next

        if start is None or start.task_name != task_name:
            print("no task found")
            return None

        # print(start)
        print("***************** Task found **********************")
        print(f"Name: {start.task_name}")
        print(f"Duration: {start.duration}")
        print(f"Priority: {start.priority}")
        if start.next is not None:
            print(f"Next task: {start.next.task_name}")
        else:
            print("Is last task")
        print("***************************************************")
        return None

    # calculate_total_duration(): Calculates the total duration of all tasks in the current order.
    def calculate_task_duration(self):
        duration = 0
        current_node = self.__head
        while current_node is not None:
            duration += current_node.duration
            current_node = current_node.next

        return duration

    # read_tasks_from_csv(file_path): Reads tasks from a CSV file and adds them to the linked list.
    def read_tasks_from_csv(self, file_path):
        file = open(file_path, 'r')
        # index = 0
        has_header = True
        for line in file:
            line = line.strip("\n")
            info = line.split(',')
            if has_header:
                has_header = False
            else:
                self.add_task(info[0], int(info[1]), int(info[2]))
        file.close()

    def get_lowest_priority(self):
        lowest_priority_node = self.__head
        current_node = self.__head
        while current_node is not None:
            if current_node.priority < lowest_priority_node.priority:
                lowest_priority_node = current_node
            # elif current_node.priority == lowest_priority_node.priority:
            #     pass

            current_node = current_node.next
        return lowest_priority_node

    def get_lowest_priority_duration(self):
        lowest_node = self.__head
        current_node = self.__head
        while current_node is not None:
            if current_node.priority < lowest_node.priority:
                lowest_node = current_node
            elif current_node.priority == lowest_node.priority:
                if lowest_node.duration > current_node.duration:
                    lowest_node = current_node

            current_node = current_node.next
        return lowest_node

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    # reorder_tasks_by_priority(): Reorders the tasks in the linked list based on priority. (lowest priority number comes first).
    def reorder_tasks_by_priority(self):
        new_list = LinkedList()
        curr = self.__head

        while curr:
            new_list.head = sorted_insert_by_priority(new_list, LinkedListNode(curr.task_name, curr.duration, curr.priority)).get_head()
            curr = curr.next

        self.__head = new_list.get_head()
        self.__tail = new_list.get_tail()


    def reorder_tasks_by_priority_duration(self):
        new_list = LinkedList()
        curr = self.__head

        while curr:
            new_list.head = sorted_insert_by_priority_duration(new_list, LinkedListNode(curr.task_name, curr.duration, curr.priority)).get_head()
            curr = curr.next

        self.__head = new_list.get_head()
        self.__tail = new_list.get_tail()


# sorted_insert_by_priority: This method has input a head (i.a linked list) and a node. The method adds the node
#  to linked list by looking at the duration. Nodes with the lowest duration are added in the beginning of the LinkedList.
def sorted_insert_by_priority(linked_list: LinkedList, node: LinkedListNode):
    """
    Insert node into a list sorted by PRIORITY ASC.
    """
    head = linked_list.get_head()

    # Insert at head
    if head is None or node.priority < head.priority:
        node.next = head
        linked_list._LinkedList__head = node
        if linked_list.get_tail() is None:
            linked_list._LinkedList__tail = node
        return linked_list

    curr = head
    while curr.next is not None and curr.next.priority <= node.priority:
        curr = curr.next

    node.next = curr.next
    curr.next = node

    if node.next is None:
        linked_list._LinkedList__tail = node

    return linked_list



# sorted_insert_by_priority_duration: This method has input a head (i.a linked list) and a node. The method adds the node to
# linked list by looking first at the priority and next at duration. Nodes with the lowest priority and then duration
# are added in the beginning of the LinkedList.
def sorted_insert_by_priority_duration(linked_list: LinkedList, node: LinkedListNode):
    """
    Insert node sorted by PRIORITY first, then DURATION.
    """
    head = linked_list.get_head()

    if (
        head is None
        or node.priority < head.priority
        or (node.priority == head.priority and node.duration < head.duration)
    ):
        node.next = head
        linked_list._LinkedList__head = node
        if linked_list.get_tail() is None:
            linked_list._LinkedList__tail = node
        return linked_list

    curr = head
    while curr.next is not None:
        nxt = curr.next
        if (node.priority < nxt.priority) or (
            node.priority == nxt.priority and node.duration < nxt.duration
        ):
            break
        curr = curr.next

    node.next = curr.next
    curr.next = node

    if node.next is None:
        linked_list._LinkedList__tail = node

    return linked_list

if __name__ == '__main__':
    list1 = LinkedList()
    list1.add_task('Task 1', 1, 2)
    list1.add_task('Task 2', 2, 3)
    list1.add_task('Task 3', 1, 3)
    list1.add_task('Task 4', 5, 3)
    list1.remove_task('Task 4')
    # print(list)
    list1.display_tasks()
    list1.find_task('Task 2')

    print(f"total duration: {list1.calculate_task_duration()}")

    print("***************** List 2 **********************")
    list2 = LinkedList()
    list2.read_tasks_from_csv('tasks.csv')
    list2.display_tasks()
    print(f"total duration 2: {list2.calculate_task_duration()}")

    print("***************** functions **********************")
    list2.add_tasks_index(6,'Task 1', 35, 2)
    # print(list2.get_lowest_priority().task_name)
    list2.reorder_tasks_by_priority_duration()
    list2.display_tasks()
    # print(f"total duration 3: {list2.calculate_task_duration()}")

    print("********************** Nodes sorted function ********************")
    node1 = LinkedListNode('Task 2', 17, 2)
    print(sorted_insert_by_priority(list2, node1).display_tasks())
