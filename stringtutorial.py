'''''
sample_string = "I love New York City"

# Print the first character
print("1: ", sample_string[0])

# Print the last character
print("2: ", sample_string[-1])

# Print the length
print("3: ", len(sample_string))

# Slice: where to star and where to end
print("4: ", sample_string[0:4])
print("5: ", sample_string[8:])

# Join and concatenate strings
print("New York " + "Yankees")

# String: Multiply
print("Time Square, " * 4)

# Convert string into an integer and integer into string
string_num = int("4")
print(type(string_num))

num_string = str(4)
print(type(num_string))

# Print string one by one
team = "Boston Red Sox"
for i in team:
    print(i)
    '''''

team = "New York Yankees"

for i in range(0, len(team)-1, 2):
    print(team[i] + team[i+1])






