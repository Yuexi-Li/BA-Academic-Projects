"""
Write a stack class to implementing basic stack functions.
1. push
2. pop
3. peek
4. size
5. is_empty
"""


class Stack():
  def __init__(self):
    self.item=[] 
    
  def push(self, value):
    """
    push the value into the stack 
    """
    return self.item.append(value)
  
  def pop(self): 
    """
    pop out the last element from a stack 
    """
    while not len(self.item):
      self.item= self.item[:-1] 
      return self.item 

  def peek(self):
    """
    peek the last element of a stack 
    """
    return self.item[-1]

  def is_empty(self):
    """
    check whether the stack is empty. Return True is the stack is empty.
    """

    if len(self.item)==0:
      return 'True'
    else:
      return "False"
  
  def size(self):
    return len(self.item) 

s= Stack()
s.push(4)
s.push('Hello')
s.push('25')
print(s.peek())
