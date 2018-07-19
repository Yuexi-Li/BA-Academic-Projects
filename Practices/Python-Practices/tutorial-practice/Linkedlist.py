"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value."""

import unittest
#Class Node: create a Node object 
class Node(object):
  #Node: Value and pointer inside 
  def __init__(self, value):
    self.value=value #value in node 
    # the pointer of that node since its single nodethe pointer points to next is None 
    self.next= None 

class LinkedList(object):
  #Linkedlist: had a head
  def __init__(self, head=None):
    self.head=head 
  
  def append(self, node):
    current=self.head
    if self.head:
      while current.next:   # while current next is not none 
        current=current.next
      current.next=node
    else:
      self.head= node 
  
  def get_position(self, position):
    """
    Get a node at given position. 
    Assume the first position is '1'.
    Return "None" if position is not in the list.
    """
    if position<=0:
      return None 
    if not self.head:
      return None 
    index=1
    current=self.head
    while current.next!= None:
      if position == index:
        return current 
      current=current.next
      index+=1
    if position==index:
      return current
    return None 

  def insert(self,node,position):
    """
    insert a node in a given position. For example, 
    input position 2 will insert the node between 2nd and 3rd node.
    The position of the linkedlist starts with 1.
    If the position is out of the length of linkedlist, 
    an indexError would be raised.
    """
    if position<=0:
      return None
    current=self.head
    #The position is 1 which insert after the node
    if position==1: 
      node.next= current
      self.head=node
      return 
    index=1
    while current!= None:
      if position==index+1:
          node.next=current.next
          current.next=node 
          return
      current=current.next 
      index+=1
    raise IndexError('{}, Out of range'.format(position))

  def delete(self, value):
    """Delete the first node with a given value."""
    current=self.head
    if current.value==value:
      self.head=current.next 
      return 
    while current.next != None:
      if current.next.value==value:
        current.next=current.next.next 
        return 
      current=current.next 
  
class MyTest(unittest.TestCase):
  def test1(self):
    # Test cases
    # Set up some Nodes
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    # Start setting up a LinkedList
    ll = LinkedList(n1)
    ll.append(n2)
    ll.append(n3)

    # Test get_position
    # Should print 3
    self.assertEqual(ll.head.next.next.value,3)
    # Should also print 3
    self.assertEqual(ll.get_position(3).value,3)

    # Test insert
    ll.insert(n4,3)
    # Should print 4 now
    print(ll.get_position(3).value)
    self.assertEqual(n4.value,4)
    self.assertEqual(ll.get_position(3).value,4)

    # Test delete
    ll.delete(1)
    # Should print 2 now
    self.assertEqual(ll.get_position(1).value,2)
    # Should print 4 now
    self.assertEqual(ll.get_position(2).value,4)
    # Should print 3 now
    self.assertEqual(ll.get_position(3).value,3)

if __name__ == '__main__':
    unittest.main()

