def letter_frequency(string):
    frequency = {}
    for letter in string:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    return frequency

input_string = input("Enter a string: ")
frequency_dict = letter_frequency(input_string)
print("Letter frequency in the given string:", frequency_dict)