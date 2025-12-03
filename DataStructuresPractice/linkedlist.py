class ListItem:
   def __init__(self, data) -> None:
      self._data = data
      self._next = None

class List:
    def __init__(self) -> None:
      self._head = None

    def insert_to_head(self, data):
        newListItem = ListItem(data)
        if self._head is None:
            self._head = newListItem
            return
        
        newListItem._next = self._head
        self._head = newListItem

    def find(self, data) -> ListItem:
        if self._head is None:
          return None
        n = self._head

        while n is not None: 
            if n._data == data:
                return f"{n._data} is found."
            n = n._next
        return None
    
    def print(self):
       n = self._head
       while n is not None:
          print(n._data)
          n = n._next


    def print_reverse(self):
        def _rec_print(node):
            if node is None:     # base case
                return
            _rec_print(node._next)  # recursion
            print(node._data)       # print on the way back

        _rec_print(self._head)      # start the recursion


    def remove(self, data):
        n = self._head

        if self._head._data == data: 
            self._head = self._head._next
            
        while n._next is not None:
             if n._next._data == data:
                n._next = n._next._next
                return
             n = n._next
    


lst = List()
lst.insert_to_head(4)
lst.insert_to_head(7)
lst.insert_to_head(10)

lst.print()
print("---")
lst.print_reverse()
print("---")
print(lst.find(10))
print("---")
lst.remove(10)
lst.print()
print("---")