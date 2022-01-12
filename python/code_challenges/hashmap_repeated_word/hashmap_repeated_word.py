import re

def check_each_word(string,definition):
    regex = r"\W+"
    split_into_words = re.sub(regex,' ',string).lower().split()

    if len(split_into_words) < 2:
        if definition == "first":
            return "String not long enough"
        if definition == "total":
            if len(split_into_words) == 0:
                return "No checkable words"
            else:
                return f"1 of {split_into_words[0]}"

    first_word = split_into_words.pop(0)

    string_dict = {first_word: 1}

    for word in split_into_words:
        if word in string_dict.keys():
            if definition == "first":
                return word
            if definition == "total":
                value = string_dict[word]
                print(value)
                value += 1
                string_dict[word] = value
        else:
            string_dict[word] = 1
    if definition == "first":
        return "There are no repeated words"
    if definition == "total":
        return string_dict

def word_count(string):
    return check_each_word(string,"total")

def repeated_word(string):
    return check_each_word(string,"first")

if __name__ == "__main__":
    test_string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    wordcount = word_count(test_string)
    print(wordcount)
