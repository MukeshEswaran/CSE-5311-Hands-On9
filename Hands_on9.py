class Node:
    """A Node in the doubly linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """A Doubly Linked List to handle collisions."""
    def __init__(self):
        self.head = None
    
    def insert(self, key, value):
        """Insert a new node at the beginning."""
        new_node = Node(key, value)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
    
    def remove(self, key):
        """Remove a node with the given key."""
        curr = self.head
        while curr:
            if curr.key == key:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return True
            curr = curr.next
        return False
    
    def find(self, key):
        """Find a node by key."""
        curr = self.head
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        return None
    
    def clear(self):
        """Clear the linked list."""
        self.head = None

class HashTable:
    """Hash Table with dynamic resizing, collision resolution via chaining."""
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.table = [DoublyLinkedList() for _ in range(capacity)]
    
    def hash_function(self, key):
        """Hash function using the multiplication method."""
        A = 0.6180339887  # Fractional constant
        return int(self.capacity * ((key * A) % 1))
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        if self.size / self.capacity >= 0.75:
            self._resize(2 * self.capacity)
        
        index = self.hash_function(key)
        self.table[index].insert(key, value)
        self.size += 1
    
    def remove(self, key):
        """Remove a key-value pair from the hash table."""
        index = self.hash_function(key)
        if self.table[index].remove(key):
            self.size -= 1
            if self.size / self.capacity <= 0.25 and self.capacity > 8:
                self._resize(self.capacity // 2)
    
    def search(self, key):
        """Search for a value by key."""
        index = self.hash_function(key)
        node = self.table[index].find(key)
        return node
    
    def _resize(self, new_capacity):
        """Resize the table to a new capacity."""
        old_table = self.table
        self.capacity = new_capacity
        self.table = [DoublyLinkedList() for _ in range(new_capacity)]
        self.size = 0

        for chain in old_table:
            curr = chain.head
            while curr:
                self.insert(curr.key, curr.value)
                curr = curr.next
    
    def print_table(self):
        """Print the hash table for debugging."""
        for i in range(self.capacity):
            print(f"Bucket {i}: ", end="")
            node = self.table[i].head
            while node:
                print(f"({node.key}, {node.value})", end=" -> ")
                node = node.next
            print("None")


# Test the HashTable

if __name__ == "__main__":
    ht = HashTable()

    # Insert some values
    ht.insert(1, 100)
    ht.insert(2, 200)
    ht.insert(3, 300)
    ht.insert(4, 400)
    ht.insert(5, 500)

    # Print the table
    ht.print_table()

    # Search for key 3
    result = ht.search(3)
    if result:
        print(f"Found key 3 with value {result.value}")
    else:
        print("Key 3 not found")

    # Remove key 3
    ht.remove(3)

    # Search for key 3 again
    result = ht.search(3)
    if result:
        print(f"Found key 3 with value {result.value}")
    else:
        print("Key 3 not found")

    # Check the size and capacity
    print(f"Current size: {ht.size}, Capacity: {ht.capacity}")
