"""
Return Kth to Last: Implement an algorithm to find the kth to last element of
a singly linked list.
Hints:#8, #25, #41, #67, #126
"""

import logging
import unittest


class Node:
    #Singly link list
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
    #linkList class
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,data):
        node = Node(data)# create a new node

        if self.head == None: #check to see if the head node is empty
            self.head = node # If its empty add it to the new node
            self.size = 1
            return
        #if the head of the linklist is filled

        current = self.head
        while current.next is not None:#Check the current postion is empty
        #Move to the next line if nothing is there
            current = current.next


        current.next = node #point self.head to a new node
        self.size+=1




    def length(self):
        #note the count doesn't start at zero
        cur = self.head
        counter = 0
        while cur is not None:
            counter+=1
            cur = cur.next
        logging.debug('Linklist len: %d', counter)
        return counter

    def toList(self):
        n = self.head

        result = []
        while(n):
            result.append(n.data)
            n = n.next
        return result

    #1->2->3
    def remove_node(self,data):
        #1->2->3
        curr = self.head
        if curr is not None and curr.data == data:
            self.head = curr.next
            curr = None
        #look for the node that has the data we are looking for
        while curr is not None:
            if curr.data == data:
                break
            prev = curr
            curr = curr.next

        #if data isn't found just reutrn
        if(curr == None):
            return

        #allow us to unlink the nodes
        prev.next = curr.next
        curr = None

    def Kth_to_Last(self,num):
        counter = 1 # We need to keep track where we are
        curr = self.head
        goal = self.size - num# kth to last element
        while curr is not None:
            if goal == counter:
                return curr.data
            counter+=1
            curr = curr.next


class Test(unittest.TestCase):
    def test_kth_to_the_last(self):
        llist = linklist()
        llist.push(1)
        llist.push(2)
        llist.push(3)
        llist.push(4)
        llist.push(5)
        self.assertEqual(llist.toList(), [1, 2, 3, 4, 5])

        self.assertEqual(llist.length(), 5)
        self.assertEqual(llist.Kth_to_Last(1), 4)
        self.assertEqual(llist.Kth_to_Last(2), 3)
        self.assertEqual(llist.Kth_to_Last(3), 2)


if __name__ =='__main__':
    unittest.main()


