from cs50 import get_string

# Get the text from the user
text = get_string("Text: ")

# Calculate the string stats needed for Coleman-Liau index
character_length = sum(characters.isalpha() for characters in text)
word_count = len(text.split())
sentence_count = text.count('.') + text.count('?') + text.count('!')

# Coleman-Liau index
readability_index = (5.88 * (float(character_length) / float(word_count)) -
                     29.6 * (float(sentence_count) / float(word_count)) - 15.8)

# Print the results
if (readability_index < 1):
    print("Before Grade 1")
elif (readability_index > 16):
    print("Grade 16+")
else:
    print("Grade ", (round(readability_index)))
