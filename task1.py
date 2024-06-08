class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def sorted_insert(self, sorted_list, new_node):
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            sorted_list = new_node
        else:
            current = sorted_list
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return sorted_list

    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy

        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


llist1 = LinkedList()
llist1.insert_at_end(3)
llist1.insert_at_end(1)
llist1.insert_at_end(2)
print("Перший список до сортування:")
llist1.print_list()

llist1.insertion_sort()
print("Перший список після сортування:")
llist1.print_list()

llist1.reverse_list()
print("Перший список після реверсування:")
llist1.print_list()


llist2 = LinkedList()
llist2.insert_at_end(6)
llist2.insert_at_end(5)
llist2.insert_at_end(4)
print("Другий список до сортування:")
llist2.print_list()

llist2.insertion_sort()
print("Другий список після сортування:")
llist2.print_list()


merged_list_head = LinkedList.merge_sorted_lists(llist1.head, llist2.head)
merged_list = LinkedList()
merged_list.head = merged_list_head
print("Об'єднаний відсортований список:")
merged_list.print_list()


