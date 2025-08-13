# data_structure_conversions.py
# Python Data Types — Definitions, Comparisons, and Conversions

print("\n=== PYTHON DATA TYPES DEFINITIONS ===")

# String
print("STRING: Ordered, immutable sequence of characters.")
print("Example: 'hello'")

# List
print("LIST: Ordered, mutable collection of items, allows duplicates.")
print("Example: [1, 2, 3]")

# Tuple
print("TUPLE: Ordered, immutable collection of items, allows duplicates.")
print("Example: (1, 2, 3)")

# Set
print("SET: Unordered, mutable collection of unique items (no duplicates).")
print("Example: {1, 2, 3}")

# Dictionary
print("DICTIONARY: Unordered, mutable collection of key-value pairs.")
print("Example: {'a': 1, 'b': 2}")

print("\n=== COMPARISON TABLE ===")
comparison_table = """
+-------------+-----------+----------+-----------+-------------+
| Data Type   | Ordered?  | Mutable? | Duplicates| Indexed?    |
+-------------+-----------+----------+-----------+-------------+
| String      | Yes       | No       | Yes       | Yes         |
| List        | Yes       | Yes      | Yes       | Yes         |
| Tuple       | Yes       | No       | Yes       | Yes         |
| Set         | No        | Yes      | No        | No          |
| Dictionary  | No*       | Yes      | Keys No** | Keys by Key |
+-------------+-----------+----------+-----------+-------------+
* From Python 3.7+, dictionaries maintain insertion order but are still conceptually unordered.
** Keys must be unique, values can be duplicated.
"""
print(comparison_table)

print("\n=== STRING ↔ LIST ===")
string_text = "hello"
print("String to list:", list(string_text))
sentence_text = "Python is fun"
print("Sentence to list of words:", sentence_text.split())
word_list = ['Python', 'is', 'fun']
print("List to string:", ' '.join(word_list))

print("\n=== STRING ↔ TUPLE ===")
tuple_chars = tuple("abc")
print("String to tuple:", tuple_chars)
print("Tuple to string:", ''.join(tuple_chars))

print("\n=== STRING ↔ SET ===")
fruit_name = "banana"
print("String to set:", set(fruit_name))
unique_letters_set = {'a', 'b', 'c'}
print("Set to string:", ''.join(unique_letters_set))

print("\n=== LIST ↔ TUPLE ===")
number_list = [1, 2, 3]
print("List to tuple:", tuple(number_list))
number_tuple = (1, 2, 3)
print("Tuple to list:", list(number_tuple))

print("\n=== LIST ↔ SET ===")
duplicate_number_list = [1, 2, 2, 3]
print("List to set:", set(duplicate_number_list))
number_set = {1, 2, 3}
print("Set to list:", list(number_set))

print("\n=== TUPLE ↔ SET ===")
tuple_with_duplicates = (1, 2, 3, 2)
print("Tuple to set:", set(tuple_with_duplicates))
set_numbers = {1, 2, 3}
print("Set to tuple:", tuple(set_numbers))

print("\n=== LIST/TUPLE/SET → DICTIONARY ===")
pair_list = [('a', 1), ('b', 2)]
print("List of tuples to dict:", dict(pair_list))
pair_tuple = (('x', 10), ('y', 20))
print("Tuple of tuples to dict:", dict(pair_tuple))
pair_set = {('m', 100), ('n', 200)}
print("Set of tuples to dict:", dict(pair_set))

print("\n=== DICTIONARY → LIST/TUPLE/SET ===")
sample_dict = {'a': 1, 'b': 2}
print("Dict keys to list:", list(sample_dict.keys()))
print("Dict keys to tuple:", tuple(sample_dict.keys()))
print("Dict keys to set:", set(sample_dict.keys()))
print("Dict values to list:", list(sample_dict.values()))
print("Dict items to list:", list(sample_dict.items()))
print("Dict items to tuple:", tuple(sample_dict.items()))
print("Dict items to set:", set(sample_dict.items()))

print("\n=== TUPLE vs SET DEMONSTRATION ===")
example_tuple = (1, 2, 2, 3)
print("Tuple:", example_tuple)
print("First element of tuple:", example_tuple[0])
example_set = {1, 2, 2, 3}
print("Set (duplicates removed):", example_set)
example_set.add(4)
print("Set after adding 4:", example_set)

try:
    example_tuple[0] = 10
except TypeError as e:
    print("Tuple modification error:", e)

try:
    print(example_set[0])
except TypeError as e:
    print("Set indexing error:", e)
