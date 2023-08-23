in_put = "yasodha bharath 123 98761132"

x=[]
s=set(in_put)
sum_duplicates=0
d={}
for i in s:

    if in_put.count(i)>1:
        c=in_put.count(i)
        sum_duplicates +=c
        d[i]=c




s="hi is is are"
s1=s.split()
s2=set(s1)
for i in s2:
    if s1.count(i)>1:
        print(i)






#############################################################################

import sys

def main():
    # Read a String statement from the command line
    input_statement = input("Enter a statement: ")

    # Find total number of characters present in the statement
    total_chars = len(input_statement)

    # Find total number of duplicate characters in the statement
    char_count = {}
    for char in input_statement:
        char_count[char] = char_count.get(char, 0) + 1
    total_duplicate_chars = sum(count > 1 for count in char_count.values())

    # Find total number of words present in the statement
    words = input_statement.split()
    total_words = len(words)

    # Find total number of duplicate words in the statement
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    total_duplicate_words = sum(count > 1 for count in word_count.values())

    # Reverse the characters present in the statement
    reversed_chars = input_statement[::-1]

    # Reverse the words present in the statement
    #reversed_words = ' '.join(reversed(word) for word in words)

    # Form a new statement from the reversed words
    #new_statement = reversed_words

    # Remove duplicate characters from the latest statement
    new_statement = ''.join(char for char in new_statement if new_statement.count(char) == 1)

    # Print final latest String statement
    print(f"Total characters: {total_chars}")
    print(f"Total duplicate characters: {total_duplicate_chars}")
    print(f"Total words: {total_words}")
    print(f"Total duplicate words: {total_duplicate_words}")
    print(f"Reversed characters: {reversed_chars}")
    print(f"Reversed words: {reversed_words}")
    print(f"Final statement without duplicate characters: {new_statement}")

if __name__ == "__main__":
    main()

###############################################################################

# Function to find total number of characters
def count_characters(statement):
    return len(statement)

# Function to find total number of duplicate characters
def count_duplicate_characters(statement):
    char_count = {}
    for char in statement:
        char_count[char] = char_count.get(char, 0) + 1
    return sum(count > 1 for count in char_count.values())

# Function to find total number of words
def count_words(statement):
    words = statement.split()
    return len(words)

# Function to find total number of duplicate words
def count_duplicate_words(statement):
    word_count = {}
    for word in statement.split():
        word_count[word] = word_count.get(word, 0) + 1
    return sum(count > 1 for count in word_count.values())

# Function to reverse characters in the statement
def reverse_characters(statement):
    return statement[::-1]

# Function to reverse words in the statement
def reverse_words(statement):
    words = statement.split()
    reversed_words = ' '.join(reversed(word) for word in words)
    return reversed_words

# Function to form a new statement from reversed words
def form_new_statement(statement):
    return reverse_words(statement)

# Function to remove duplicate characters from a statement
def remove_duplicate_characters(statement):
    return ''.join(char for char in statement if statement.count(char) == 1)

# Read a String statement from the command line
input_statement = input("Enter a statement: ")

# Calculate and display results
total_chars = count_characters(input_statement)
total_duplicate_chars = count_duplicate_characters(input_statement)
total_words = count_words(input_statement)
total_duplicate_words = count_duplicate_words(input_statement)
# reversed_chars = reverse_characters(input_statement)
# reversed_words = reverse_words(input_statement)
# new_statement = form_new_statement(input_statement)
# final_statement = remove_duplicate_characters(new_statement)

print(f"Total characters: {total_chars}")
print(f"Total duplicate characters: {total_duplicate_chars}")
print(f"Total words: {total_words}")
print(f"Total duplicate words: {total_duplicate_words}")
print(f"Reversed characters: {reversed_chars}")
print(f"Reversed words: {reversed_words}")
print(f"Final statement without duplicate characters: {final_statement}")
