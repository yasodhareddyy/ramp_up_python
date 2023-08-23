#  Read a String statement from the command line

in_put=input("Enter statement : ")
input_1=input("Enter new input : ")
#in_put = "yasodha bharath 123 98761132 yasodha yash"

# Find out total number of characters present in the statement.
len_input_str = (len(in_put+input_1))

# Find out total number of duplicate Characters in the statementH
duplicate_cont = 0
for i in set(in_put):
    if in_put.count(i) > 1:
        duplicate_cont += in_put.count(i)

# Find out total number of words present in the statement
splt=in_put.split(" ")

# Function to find total number of duplicate words
duplicate_words=0
for i in set(splt):
    if splt.count(i)>1:
        duplicate_words+=splt.count(i)

# Reverse the characters present in the statement.
reverse_str=in_put[::-1]

# Reverse the words present in the statement.
reverse_words=""
for i in splt:
    reverse_words+=i[::-1]+" "

#Form a new statement from the reversed words.
new_statement = reverse_words

# Remove the duplicate characters from the latest statement.
remove_duplicates=""
for i in new_statement:
    if i not in remove_duplicates:
        remove_duplicates+=i
#print(remove_duplicates)



print(in_put)
print(f"Total number of characters present in the statement : {len_input_str}")
print(f"Total number of duplicate Characters in the statement : {duplicate_cont}")
print(f"Total number of words present in the statement : {len(splt)}")
print(f"Total number of duplicate words : {duplicate_words} ")
print(f"Reverse the characters : {reverse_str}")
print(f"Reverse the words : {reverse_words}")
print(f"Final statement without duplicate characters: {remove_duplicates}")




