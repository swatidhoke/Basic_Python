# Commonly Used String Functions in Python:
# 1. len() - Returns the length of the string.
#    Example: len("hello") returns 5.
#
# 2. str.upper() - Converts all characters in the string to uppercase.
#    Example: "hello".upper() returns "HELLO".
#
# 3. str.lower() - Converts all characters in the string to lowercase.
#    Example: "HELLO".lower() returns "hello".
#
# 4. str.strip() - Removes leading and trailing whitespace from the string.
#    Example: "  hello  ".strip() returns "hello".
#
# 5. str.replace(old, new) - Replaces occurrences of a substring with a new substring.
#    Example: "hello world".replace("world", "Python") returns "hello Python".
#
# 6. str.split(separator) - Splits the string into a list of substrings based on the separator.
#    Example: "hello world".split(" ") returns ["hello", "world"].
#
# 7. str.join(iterable) - Joins elements of an iterable into a single string with a separator.
#    Example: ", ".join(["apple", "banana", "cherry"]) returns "apple, banana, cherry".
#
# 8. str.find(substring) - Finds the index of the first occurrence of a substring. Returns -1 if not found.
#    Example: "hello world".find("world") returns 6.
#
# 9. str.startswith(prefix) - Checks if the string starts with the specified prefix.
#    Example: "hello world".startswith("hello") returns True.
#
# 10. str.endswith(suffix) - Checks if the string ends with the specified suffix.
#     Example: "hello world".endswith("world") returns True.

# Convert each token to lowercase and remove non-alphabetic characters
#clean_word = ''.join(ch.lower() for ch in word if 'a' <= ch.lower() <= 'z')

#str.count(substring) - this will return the count of a word in a given string
# text = "hello world, hello universe"
# count_hello = text.count("hello")
# print(count_hello)  # Output: 2
class StringLearningPython:
    '''
    Some basic usage of String data structure in Python
    '''

    def __init__(self):
        pass

    # 1. Check if a String is a Palindrome
    def is_palindrome(self, s):
        return s == s[::-1]

    # 2. Count the Number of Vowels in a String
    def count_vowels(self, s):
        vowels = "aeiouAEIOU"
        vowel_count = 0
        for char in s:
            if char in vowels:
                vowel_count += 1
        return vowel_count

    # 3. Find the Most Frequent Character in a String
    def most_frequent_char(self, s):
        max_count = 0
        most_frequent = ''
        for char in s:
            count = s.count(char)
            if count > max_count:
                max_count = count
                most_frequent = char
        return most_frequent

    # 4. Remove Duplicates from a String
    def remove_duplicates(self, s):
        seen = set()
        result = []
        for char in s:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)


if __name__ == '__main__': 
    string_learner = StringLearningPython()

    s = "racecar"
    print("is_palindrome:", string_learner.is_palindrome(s))  # Output: True

    s = "Hello World"
    print("count_vowels:", string_learner.count_vowels(s))  # Output: 3

    s = "hello"
    print("most_frequent_char:", string_learner.most_frequent_char(s))  # Output: 'l'

    s = "banana"
    print("remove_duplicates:", string_learner.remove_duplicates(s))  # Output: "ban"

