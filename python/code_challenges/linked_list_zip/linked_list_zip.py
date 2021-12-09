from linked_list.linked_list import LinkedList

# def zip_lists(linked_list_one,linked_list_two):
#     # entry back into list one
#     previous_next_list_one = linked_list_one.head.next

#     #connecting to the head of list two
#     linked_list_one.head.next = linked_list_two.head

#     #entry back into list two
#     previous_next_list_two = linked_list_two.head.next

#     #connecting list two to the entry point on list one
#     linked_list_two.head.next = previous_next_list_one

#     #connecting back list one to entry back into list two
#     previous_next_list_one.next = previous_next_list_two
#     return linked_list_one

def zip_lists(linked_list_one,linked_list_two):

    if not linked_list_one.head:
        raise IndexError(" list one does not exist")
    if not linked_list_two.head:
        raise IndexError(" list two does not exist")

    current = linked_list_one.head
    target = linked_list_two.head

    while current:

        if target is None:
            return linked_list_one
        else:
            current_next = current.next
            current.next = target
            target = current_next
            current = current.next

    return linked_list_one

if __name__ == "__main__":
    print("Hello")

    a = LinkedList()
    a.insert("1")
    a.insert("2")
    b = LinkedList()
    b.insert("One")
    b.insert("Two")
    print(a)
    print(b)
    marco = zip_lists(a,b)
    print(marco)


