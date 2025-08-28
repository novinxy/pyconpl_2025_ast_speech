def append_to(element, collection=[]):
    collection.append(element)
    return collection


print(append_to(12))  # [12]
print(append_to(42))  # [12, 42]
