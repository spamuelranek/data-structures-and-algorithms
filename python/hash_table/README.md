# Hashtables
- Hashtables are present in many languages already. Dicts in python are a form of hashtables. They are a storage system of keky value pairs with a look up time of O(1)

## Challenge
- Implement a Hash Table that has add, get, contains, and hash

## Approach & Efficiency
- I chose to implement my hash table with linked lists at each index. I did it because the documentation supplied mentioned it. I also created another method on the linked list to move through the linked list in the way that was specific to this implementation.
- add()
    - Big O time = O(1)
        - all actions are independent of the value passed in.
    - Big O space = 0(1)
        - you will at most be creating a node one time for each time you run the function

- get()
    - Big O time = O(N)
        - that is if hash() has an 0(1) everything else is a O(1) excepte if the linked list has more than one value
    - Big O space = 0(N)
        - you will at most be creating a node one time for each time you run the function

- contains()
    - Big O time = O(N)
        - that is if hash() has an 0(1) everything else is a O(1) excepte if the linked list has more than one value
    - Big O space = 0(N)
        - you will at most be creating a node one time for each time you run the function

- hash()
    - Big O time = O(N)
        - that is if hash() has an 0(1) everything else is a O(1) excepte if the linked list has more than one value
    - Big O space = 0(N)
        - you will at most be creating a node one time for each time you run the function



## API
No Api used
