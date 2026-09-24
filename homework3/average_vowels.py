# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()
def counting_vowels_and_consonants(s):
    v = 0
    c = 0
    s = s.lower()
    for i in s:
        if i.isalpha():
            if i in 'aeiou':
                v += 1
            else:
                c += 1
    return (v, c)


# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()
def average_vowels_and_consonants(i):
    i = i.replace("?", ".").replace("!", ".")
    s = i.split('.')
    n, v, c = -1, 0, 0
    for a in s:
        temp = counting_vowels_and_consonants(a)
        n += 1
        v += temp[0]
        c += temp[1]
    return (n, v/n, c/n)

    

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
ans = average_vowels_and_consonants(paragraph)
print(f"This paragraph has {ans[0]} sentences, {ans[1]} vowels per sentence, and {ans[2]} consonants per sentence")
