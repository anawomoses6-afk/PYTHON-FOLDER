# number one
def length_of_string(input_string):
    return len(input_string)

sample_string = 'semicolon'
print(length_of_string(sample_string))

# nomber two
def collect_string(enter_string):
    if len(input_string) < 2:
        return ""
    return enter_string[:2] + enter_string[-2:]

print(collect_string('semicolon')) 
print(collect_string('on'))        
print(collect_string('o'))         


#number three
def add(enter_string):
    if len(enter_string) < 3:
        return enter_string
    elif enter_string.endswith('ing'):
        return enter_string + ('ly'
    else:
        return enter_string + 'ing'

print(add('abc'))    
print(add('string')) 
print(add('on'))     

#number four
def search_word(word_list):
    if not word_list:
        return None, 0
    
    longest_word = max(word_list, key=len)
    return longest_word, len(longest_word)

sample_data = ['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey']
word, length = search_word(sample_data)
print(f"{word}, {length}")


#number five
def remove_odd(enter_string):
    return enter_string[0::2]

sample_data = "semicolon"
print(remove_odd(sample_data))


#number six
def minimum_return_number(numbers):
    minimum_number= number[0]
    for number in numbers:
        if number < minimum_number
            minimum_number = number
    return minimum
print(minimum_return_number(8,4,9,2,5,7,3))


# number seven
def squared_list(numbers):
    return (number * number of number in numbers)
        Sample_data: [2, 3, 4, 5, 7]
print(squared_list(sample_data))


#number Eight
def list_return_sum(numbers):
    sum = 0
    for number in numbers:
    sum = sum + (number * number)
    return sum
    
sample_data: [2, 3, 4, 5, 7]
print(list_return_sum(sample_data))








