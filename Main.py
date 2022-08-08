from typing import Optional


class Node:
    """
    Provide necessary documentation
    """
    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """
    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        new = Node(data)
        if self.head == None:
            self.head = new
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new
          

    def status(self):
        """
        It prints all the elements of list.
        """
        curr = self.head
        while curr != None and curr.next != None:
            print(curr.data, end = " ")


def get_num(l: LinkedList):
    num = 0
    curr = l.head
    while curr != None and curr.next != None:
        num = num * 10 + curr.data
        curr = curr.next
    return int(str(num)[::-1])
            
class Solution:
    """
    Provide necessary documentation
    """
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        result = get_num(first_list) + get_num(second_list)
        sum_list = LinkedList()
        for digit in map(int, str(result)[::-1]):
            sum_list.insert_at_end(digit)
        return sum_list
        
        

# Do not edit the following code      
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedListT
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()
