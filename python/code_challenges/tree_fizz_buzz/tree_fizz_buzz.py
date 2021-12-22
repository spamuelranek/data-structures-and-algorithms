from tree.k_tree import Ktree

def fizz_buzz_tree(ktree):
    if ktree.root is None:
        return "Empty Tree"
    breadth_list = ktree.breadth_first()
    type_of_k = ktree.k

    new_ktree = Ktree(type_of_k)

    while breadth_list:
        value_to_check = breadth_list.pop(0)
        if value_to_check % 15 == 0:
            value_to_check = "FizzBuzz"
        elif value_to_check % 5 == 0:
            value_to_check = "Buzz"
        elif value_to_check % 3 == 0:
            value_to_check = "Fizz"
        else:
            value_to_check = str(value_to_check)

        new_ktree.add_node(value_to_check)

    return new_ktree


