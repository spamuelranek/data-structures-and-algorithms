from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Dog, Cat, Kiwi
import pytest
def test_is_animal_shelter():
    animal_shelter = AnimalShelter
    assert animal_shelter

def test_is_dog():
    doggy = Dog
    assert doggy

def test_is_cat():
    kitty = Cat
    assert kitty

def test_not_a_cat_or_dog():
    animal_shelter = AnimalShelter()
    bird = Kiwi()
    with pytest.raises(ValueError):
        animal_shelter.enqueue(bird)

def test_enqueue_dog():
    animal_shelter = AnimalShelter()
    doggy = Dog("Charlie")
    animal_shelter.enqueue(doggy)
    actual = animal_shelter._enqueue_stack.peek().name
    expected = "Charlie"
    assert actual == expected

def test_enqueue_dog_and_cat():
    animal_shelter = AnimalShelter()
    doggy = Dog("Charlie")
    kitty = Cat("loafen")
    animal_shelter.enqueue(doggy)
    animal_shelter.enqueue(kitty)
    actual = animal_shelter._enqueue_stack.peek().name
    expected = "loafen"
    assert actual == expected

def test_dequeue_an_animal():
    animal_shelter = AnimalShelter()
    doggy = Dog("Charlie")
    animal_shelter.enqueue(doggy)
    actual = animal_shelter.dequeue().name
    expected = "Charlie"
    assert actual == expected

def test_dequeue_a_dog_among_cats():
    animal_shelter = AnimalShelter()
    kitty_cat = Cat("dubious")
    doggy = Dog("Charlie")
    kitty = Cat("loafen")
    animal_shelter.enqueue(kitty_cat)
    animal_shelter.enqueue(doggy)
    animal_shelter.enqueue(kitty)
    actual = animal_shelter.dequeue("dog").name
    expected = "Charlie"
    assert actual == expected

def test_dequeue_a_cat_among_dogs():
    animal_shelter = AnimalShelter()
    doggy = Dog("Charlie")
    kitty = Cat("loafen")
    little_doggy = Dog("werner")
    animal_shelter.enqueue(doggy)
    animal_shelter.enqueue(kitty)
    animal_shelter.enqueue(little_doggy)
    actual = animal_shelter.dequeue("cat").name
    expected = "loafen"
    assert actual == expected

def test_dequeue_longest_held_animal():
    animal_shelter = AnimalShelter()
    doggy = Dog("Charlie")
    kitty = Cat("loafen")
    little_doggy = Dog("werner")
    animal_shelter.enqueue(doggy)
    animal_shelter.enqueue(kitty)
    animal_shelter.enqueue(little_doggy)
    actual = animal_shelter.dequeue().name
    expected = "Charlie"
    assert actual == expected

def test_dequeue_dog_with_no_dogs():
    animal_shelter = AnimalShelter()
    kitty = Cat("loafen")
    animal_shelter.enqueue(kitty)
    actual = animal_shelter.dequeue("dog")
    expected = "There are no dogs in the shelter at the time"
    assert actual == expected

def test_dequeue_with_no_animals():
    animal_shelter = AnimalShelter()
    with pytest.raises(IndexError):
        animal_shelter.dequeue("dog")

def test_dequeue_multiple():
    animal_shelter = AnimalShelter()
    doggy = Dog("Charlie")
    kitty = Cat("loafen")
    little_doggy = Dog("werner")
    animal_shelter.enqueue(doggy)
    animal_shelter.enqueue(kitty)
    animal_shelter.enqueue(little_doggy)
    animal_shelter.dequeue()
    actual = animal_shelter.dequeue("dog").name
    expected = "werner"
    assert actual == expected

