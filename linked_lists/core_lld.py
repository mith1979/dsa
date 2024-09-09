class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        # print(new_node)
        # print(self.tail)
    
    def print_list(self):
        # breakpoint()
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # breakpoint()
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            # self.tail = new_node
        else:
            self.tail.next = new_node
            # Move the tail to new last appended node
            # self.tail = new_node
        
        # Moving the self.tail to a common place
        self.tail = new_node    
        self.length +=1
        return True
    
    def pop(self):
        # This is the part if we have 0 items in LL 
        if self.length == 0:
            return None
        # This is the part where we have 2 or more items in LL
        temp = self.head
        pre = self.head
        # We can have both the while loop statements
        # while temp is not None:
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        # This is the part where we have 1 item in LL 
        if self.length == 0:
            self.tail= None
            self.head = None
            return temp.value
    
    def prepend(self, value):
        new_node = Node(value)
        # This is the part where we have 0 items in LL
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # This is the part where we have 2 or more items in LL
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        # This is the part of if we have 0 items in LLs
        if self.length==0:
            return None
        temp = self.head
        # This is the part if we have a 1 item in LLs
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:
        # This is the part where we have more than 1 or more items in the LLs
            self.head = temp.next
        self.length-=1
        return temp.value 
    
    def    

# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# my_linked_list.print_list()

my_linked_list = LinkedList(2)
my_linked_list.append(3)
# my_linked_list.print_list()

my_linked_list.prepend(1)
my_linked_list.print_list()
# my_linked_list.pop()
# my_linked_list.print_list()
# my_linked_list.pop()
# my_linked_list.print_list()
# my_linked_list.pop()
# my_linked_list.print_list()

my_linked_list.pop_first()
# my_linked_list.pop_first()
# my_linked_list.pop_first()
my_linked_list.print_list()