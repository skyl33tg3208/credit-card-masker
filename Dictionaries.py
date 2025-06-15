fruit_basket = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
}

#How would you print the color of the banana?
print(fruit_basket["banana"])
#How would you print the entire dictionary?
print(fruit_basket)
#What happens if you try to access a key that isn't in the dictionary, like fruit_basket["orange"]?
print(fruit_basket["orange"])
#how would you add a new fruit, "kiwi" with the color "green" to the fruit_basket?
fruit_basket["kiwi"] = "green"
#remove the "apple" from the fruit_basket
del fruit_basket["apple"]


#Real world examples
#Contact List where you store peoples name and their phone numbers
contacts = {
    "Kenny": "305-906-2960",
    "Kenny": "786-123-5543",
}

#Product Inventory where you might have a dictionary to keep track of products and their prices
inventory = {
    "shoes": "Nike",
    "shirts": "Jordan",
}

# Let's say we want to find out Bob's phone number from our contact list
print(contacts["Bob"])  # This will print: 987-654-3210

# If we want to update Sarah's grade
grades["Sarah"] = 95  # Now Sarah has a new grade

# If we want to check the price of a smartphone
print(inventory["smartphone"])  # This will print: 699.99