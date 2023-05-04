my_string = raw_input("Type in numbers: ")
my_string = my_string.split()
my_numbers = []
for item in my_string:
    my_numbers.append(int(item)) # Convert to int and append to my_numbers.
result = add(my_numbers) # add it all up and assign to result.