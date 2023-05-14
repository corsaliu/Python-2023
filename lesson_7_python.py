"""
Count the occurrences of the word "ReDI" in the phrase: “ReDI school is awesome! Yes ReDI is really cool."
"""

input_str = "ReDI school is awesome! Yes ReDI is really cool."
word = "ReDI"

print(input_str.count(word))


# Another method using function
def count_word_occurences (input_str, word):
    return input_str.count(word)

print(count_word_occurences("ReDI school is awesome! Yes ReDI is really cool.", "ReDI"))
