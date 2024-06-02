import random

class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Previews node is None")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None
  
  def revers(self):
    """ Reversed list """
    if not self.head:
        return self# linked list is empty
    stack = []
    current = self.head
    while current:
      stack.append(current)
      current = current.next
    self.head = stack.pop()
    self.head.next = None;
    current = self.head
    while len(stack) > 0:
      current.next = stack.pop()
      current = current.next
      current.next = None
    return self

  def pop(self, node = None) -> int | None:
    """ Pop the node or last node in list """
    if not node: # find the tail
      curr = self.head
      while curr:
        node = curr
        curr = curr.next
    if not node:
      return None
    if node == self.head:
      self.head = node.next
      node.next = None
      return node.data
    prev = self.head
    while prev.next:
      if prev.next == node:
        prev.next = node.next
        node.next = None
        return node.data
      prev = prev.next
    return None # node is not presend in list

  def sort(self):
    """ Sortings list by insertion """
    if not self.head or not self.head.next:
      return self # empty or one element list
    curr = self.head.next
    while curr:
        next = curr.next
        current = self.pop(curr)
        if current < self.head.data:
          self.insert_at_beginning(current)
        else:
          curr = self.head
          while curr.next != next:
            if current < curr.next.data:
              break
            curr = curr.next
          self.insert_after(curr, current)
        curr = next
    return self

  def merge_with(self, list):
    """ Merge current linked list with another one (both lists must be sorted lists) """
    if not list or not list.head:
      return self # Empty list for merge - do nothing
    if not self.head:
      self.head = list.head
      return self 
    new = None
    if self.head.data < list.head.data:
      new = self.head
      l1 = new.next
      l2 = list.head
    else:
      new = list.head
      l1 = self.head
      l2 = new.next
    curr = new
    while l1 and l2:
      if l1.data < l2.data:
        curr.next = l1
        curr = l1
        l1 = l1.next
      else:
        curr.next = l2
        curr = l2
        l2 = l2.next
    while l1:
      curr.next = l1
      curr = l1
      l1 = l1.next
    while l2:
      curr.next = l2
      curr = l2
      l2 = l2.next
    self.head = new
    return self

  def __str__(self):
    res = ""
    current = self.head
    is_first = True
    while current:
      if is_first:
        is_first = False
      else:
        res += " -> "
      res += f"{current.data}"
      current = current.next
    return res

if __name__ == "__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Linked list:")
    print(llist)

    print("Reversed linked list:")
    print(llist.revers())

    print("Sorted linked list:")
    print(llist.sort())

    llist2 = LinkedList()
    for _ in range(5):
        llist2.insert_at_end(random.randint(1, 25))
    print(f"Merge with random sorted list: {llist2.sort()}")
    print(llist.merge_with(llist2))
