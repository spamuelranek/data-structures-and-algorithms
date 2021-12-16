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


    for bracket in modified_string:
        if bracket in dict_of_truth:
            open_stack.append(bracket)
        elif bracket in dict_of_truth.values():
            if not open_stack:
                return False

            if bracket != dict_of_truth[open_stack.pop()]:
                return False

    return True



if __name__ == "__main__":
    string = "(()"
    results = validate_brackets(string)
    print(results)
