from hash_table.hash_table import HashTable

def tree_intersection(tree_one, tree_two):
    tree_one_values = tree_one.pre_order()
    tree_two_values = tree_two.pre_order()
    tree_one_hashmap = HashTable(len(tree_one_values))
    for value in tree_one_values:
        tree_one_hashmap.add(value,value)

    output = set()
    for value in tree_two_values:
        if tree_one_hashmap.contains(value):
            output.add(value)

    return output

def tree_intersection_no_hash(tree_one, tree_two):
    tree_one_values = tree_one.pre_order()
    tree_two_values = tree_two.pre_order()

    output = set()
    for value in tree_two_values:
        if value in tree_one_values:
            output.add(value)

    return output
