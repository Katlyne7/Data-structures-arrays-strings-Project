class Node:
    """Represents a single node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list with common operations.

    Maintains an internal size counter so size() runs in O(1)
    instead of traversing the whole list every time.
    """

    def __init__(self):
        self.head = None
        self._size = 0  #Tracks size to avoid O(n) traversal

    # Basic info 

    def is_empty(self):
        """Returns True if the list has no elements. O(1)"""
        return self.head is None

    def size(self):
        """Returns the number of nodes. O(1)"""
        return self._size

    # Insertion

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self._size += 1

    def insert_at_position(self, data, pos):

        if pos < 0 or pos > self._size:
            raise IndexError(
                f"Position {pos} is out of range for a list of size {self._size}."
            )

        if pos == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(pos - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1

    # Deletion

    def delete_by_value(self, value):
        """
        Deletes the first node containing value. O(n)

        Returns True if deleted, False if value wasn't found.
        """
        if self.head is None:
            print(f"Cannot delete {value}: list is empty.")
            return False

        # Head is the target
        if self.head.data == value:
            self.head = self.head.next
            self._size -= 1
            return True

        # Search the rest of the list
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next

        print(f"Value {value} not found.")
        return False

    # Search 

    def search(self, value):
        """
        Returns the 0-based index of the first occurrence of value,
        or -1 if not found. O(n)
        """
        current = self.head
        for index in range(self._size):
            if current.data == value:
                return index
            current = current.next
        return -1

    # Display

    def display(self):
        """Prints all elements as a chain ending in None."""
        if self.head is None:
            print("None")
            return

        parts = []
        current = self.head
        while current is not None:
            parts.append(str(current.data))
            current = current.next

        print(" -> ".join(parts) + " -> None")


# Tests 

if __name__ == "__main__":

    def header(title):
        print(f"\n--- {title} ---")

    print("=" * 50)
    print("        LINKED LIST TESTS")
    print("=" * 50)

    # Test 1: Empty list
    header("Test 1: Empty list")
    ll = LinkedList()
    print(f"Empty: {ll.is_empty()} | Size: {ll.size()}")
    ll.display()

    # Test 2: Prepend & Append
    header("Test 2: Prepend & Append")
    ll.prepend(20)
    ll.prepend(10)
    ll.append(30)
    ll.append(40)
    ll.display()                          # 10 -> 20 -> 30 -> 40 -> None
    print(f"Size: {ll.size()}")

    # Test 3: Insert at position
    header("Test 3: Insert at position")
    ll.insert_at_position(15, 1)
    ll.display()                          # 10 -> 15 -> 20 -> 30 -> 40 -> None
    ll.insert_at_position(0, 0)
    ll.display()                          # 0 -> 10 -> 15 -> 20 -> 30 -> 40 -> None

    # Test 4: Search
    header("Test 4: Search")
    print(f"Search 20: index {ll.search(20)}")
    print(f"Search 99: index {ll.search(99)}")

    # Test 5: Delete by value
    header("Test 5: Delete by value")
    ll.delete_by_value(15)                # middle node
    ll.delete_by_value(0)                 # head node
    ll.delete_by_value(40)                # tail node
    ll.display()                          # 10 -> 20 -> 30 -> None

    # Test 6: Edge cases
    header("Test 6: Edge cases")
    empty = LinkedList()
    empty.delete_by_value(5)              # delete from empty list
    print(f"Search in empty list: {empty.search(1)}")

    try:
        ll.insert_at_position(99, 100)    # out-of-range position
    except IndexError as e:
        print(f"Caught: {e}")

    try:
        ll.insert_at_position(99, -1)     # negative position
    except IndexError as e:
        print(f"Caught: {e}")

    # Test 7: Single-element list
    header("Test 7: Single element")
    solo = LinkedList()
    solo.append(42)
    solo.display()
    solo.delete_by_value(42)
    solo.display()
    print(f"Empty after deletion? {solo.is_empty()}")

    print("\n" + "=" * 50)
    print("  ALL TESTS COMPLETE")
    print("=" * 50)