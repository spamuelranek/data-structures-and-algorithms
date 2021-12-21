from code_challenges.stack_and_queue.queue import Queue

def tree_breadth_first_list(tree):
    if not tree.root:
        return "Tree is empty"
    first_into_queue = tree.root
    list_q = []
    list_q.append(first_into_queue)
    return_list = []
    increment_index = 0

    while list_q:

        deq_list = list_q.pop()
        return_list.append(deq_list.value)
        print(return_list)


        if deq_list.left:
            list_q.append(deq_list.left)
        if deq_list.right:
            list_q.append(deq_list.right)

        increment_index += 1

    return return_list

def tree_breadth_first(tree):
    if not tree.root:
        return "Tree is empty"
    first_into_queue = tree.root
    q = Queue()
    q.enq(tree.root)
    # q.deq()
    return_list = []
    print(q.front.value.left.value)
    # print(q.front.next.value.left.value)


    while not q.is_empty():
        # print(q.peek().value)
        dequeue = q.deq()
        return_list.append(dequeue.value)
        # print(dequeue.left.value)

        if dequeue.left:
            q.enq(dequeue.left)
        if dequeue.right:
            q.enq(dequeue.right)



    return return_list
