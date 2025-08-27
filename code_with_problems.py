def append_to(element, to=[]):
    to.append(element)
    return to


print(append_to(12))  # [12]
print(append_to(42))  # [12, 42]
