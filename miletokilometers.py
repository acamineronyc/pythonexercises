# Ask the user to input miles and assign it to the miles variable
print('This application will convert miles into kilometers')

miles = input('Please enter the numbers of miles: ')

# Convert from string to integer
miles = int(miles)

# Convert miles into kilometers

kilometer = miles * 1.60934

# Print the results using format()
print("{0} miles is equal two {1} kilometers".format(miles, kilometer))
