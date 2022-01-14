def add_left(hash_left, hash_right):
    left_key_list = hash_left.keys()
    output = []
    for key in hash_left:
        key_output = []
        key_output.append(key)
        key_output.append(hash_left[key])
        if key in hash_right.keys():
            key_output.append(hash_right[key])
        else:
            key_output.append(None)
        output.append(key_output)

    return output
