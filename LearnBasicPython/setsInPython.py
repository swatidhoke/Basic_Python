# set.py
# Basic Python learning file for SET data structure

# -------------------------
# 1. Creating a set
# -------------------------
fruits = {"apple", "banana", "cherry"}
print("Initial set:", fruits)

# -------------------------
# 2. Sets automatically remove duplicates
# -------------------------
numbers = {1, 2, 3, 2, 1}
print("Set with duplicates removed:", numbers)

# -------------------------
# 3. Adding elements
# -------------------------
fruits.add("orange")
print("After adding orange:", fruits)

# -------------------------
# 4. Updating set with multiple elements
# -------------------------
fruits.update(["mango", "grape"])
print("After updating with multiple fruits:", fruits)

# -------------------------
# 5. Removing elements
# -------------------------
fruits.remove("banana")  # Will cause an error if not found
print("After removing banana:", fruits)

fruits.discard("kiwi")  # Won't cause an error if not found
print("After discarding kiwi (safe):", fruits)

# -------------------------
# 6. Set operations
# -------------------------
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)         # {1, 2, 3, 4, 5, 6}
print("Intersection:", set_a & set_b)  # {3, 4}
print("Difference:", set_a - set_b)    # {1, 2}
print("Symmetric Difference:", set_a ^ set_b)  # {1, 2, 5, 6}

# -------------------------
# 7. Checking membership
# -------------------------
print("Is 3 in set_a?", 3 in set_a)
print("Is 7 in set_a?", 7 in set_a)

# -------------------------
# 8. Looping through a set
# -------------------------
print("Looping through set_a:")
for num in set_a:
    print(num)

# -------------------------
# 9. Converting list to set
# -------------------------
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print("List with duplicates removed using set:", unique_set)
