import re

def validate_brackets(string):
    regex = r"\w*\s*"
    modified_string = re.sub(regex,'',string)
    print(modified_string)

    if not modified_string:
        return True
    if len(modified_string) % 2 != 0:
        return False

    modified_string = list(modified_string)
    dict_of_truth = {'{':'}','[':']','(':')'}
    open_stack = []
    close_stack = []
    index_number = 1

    while modified_string:
        bracket = modified_string.pop()
        if bracket == '{' or bracket =='[' or bracket == '(':
            open_stack.append((bracket,index_number))
        elif bracket == '}' or bracket ==']' or bracket == ')':
            close_stack.append((bracket,index_number))

        index_number += 1

    while open_stack and close_stack:
        if dict_of_truth[open_stack.pop()[0]] != close_stack.pop()[0] or open_stack.pop()[1] < close_stack.pop()[1]:
            return False

    return True



if __name__ == "__main__":
    string = "(()"
    results = validate_brackets(string)
    print(results)
