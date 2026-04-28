import random


class Node:
    def __init__(self, data):
        self.data = float(data)
        self.next = None
        self.prev = None

    @staticmethod
    def create_list():
        count = int(input("n : "))
        if count <= 0:
            return None, None

        head = None
        tail = None

        for _ in range(count):
            val = round(random.uniform(8, 10))
            new_node = Node(val)

            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                new_node.prev = tail
                tail = new_node

        return head, tail

    @staticmethod
    def read_list(head):
        if head is None:
            return

        curr = head
        while curr is not None:
            if curr.next is not None:
                print(curr.data, end=" - ")
            else:
                print(curr.data)
            curr = curr.next

    @staticmethod
    def calculate(head, tail):
        if head is None or tail is None:
            return 0

        total_sum = 0
        l = head
        r = tail

        while l is not None:
            total_sum += l.data * r.data
            l = l.next
            r = r.prev
        return total_sum

    @staticmethod
    def clear_memory(head):
        curr = head
        while curr is None:
            next_node = curr.next
            curr.next = None
            curr.prev = None
            curr = next_node
        return None, None


my_head, my_tail = Node.create_list()
Node.read_list(my_head)

res = Node.calculate(my_head, my_tail)
print(f"\n Answer: {round(res, 4)}")

my_head, my_tail = Node.clear_memory(my_head)
