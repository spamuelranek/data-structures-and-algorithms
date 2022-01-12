from code_challenges.hashmap_repeated_word.hashmap_repeated_word import repeated_word

def test_is_repeated_word():
   assert repeated_word

def test_marco_expected_repeated_word():
    test_string = "marco polo rounded the world. Marco Polo fought the world!"
    actual = repeated_word(test_string)
    expected = "marco"
    assert actual == expected

def test_marco_with_punctuation_expected_repeated_word():
    test_string = "marco, polo rounded the world. Marco Polo fought the world!"
    actual = repeated_word(test_string)
    expected = "marco"
    assert actual == expected

def test_marco_times_two_repeated_word():
    test_string = "marco';: marco,!"
    actual = repeated_word(test_string)
    expected = "marco"
    assert actual == expected

def test_string_not_lone_enough():
    test_string = "marco';:"
    actual = repeated_word(test_string)
    expected = "String not long enough"
    assert actual == expected

def test_no_repeats_enough():
    test_string = "marco';: darco larco zarco farko"
    actual = repeated_word(test_string)
    expected = "There are no repeated words"
    assert actual == expected

