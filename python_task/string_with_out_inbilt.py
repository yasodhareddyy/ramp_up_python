# Read a String statement from the command line
in_put = input("Enter statement: ")
#input_1 = input("Enter new input: ")

# Find out total number of characters present in the statement.
len_input_str = len(in_put)

# Find out total number of duplicate Characters in the statement
char_count = {}  # A dictionary to store character counts
duplicate_cont = 0

for char in in_put:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
for count in char_count.values():
    if count > 1:
        duplicate_cont += count

# Find out total number of words present in the statement
splt = in_put.split(" ")

# Function to find the total number of duplicate words
duplicate_words = 0
word_count = {}  # A dictionary to store word counts

for word in splt:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for count in word_count.values():
    if count > 1:
        duplicate_words += count

# Reverse the characters present in the statement.
reverse_str = ""
for char in in_put:
    reverse_str = char + reverse_str

# Reverse the words present in the statement.
reverse_words = ""
for word in splt:
    reverse_words = word + " " + reverse_words

# Form a new statement from the reversed words.
new_statement = reverse_words

# Remove the duplicate characters from the latest statement.
remove_duplicates = ""
for char in new_statement:
    if char not in remove_duplicates:
        remove_duplicates += char

print(in_put)
print(f"Total number of characters present in the statement: {len_input_str}")
print(f"Total number of duplicate Characters in the statement: {duplicate_cont}")
print(f"Total number of words present in the statement: {len(splt)}")
print(f"Total number of duplicate words: {duplicate_words}")
print(f"Reverse the characters: {reverse_str}")
print(f"Reverse the words: {reverse_words}")
print(f"Final statement without duplicate characters: {remove_duplicates}")
