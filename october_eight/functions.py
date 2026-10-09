
def length_of_string(input_string):
    return len(input_string)

sample_string = 'semicolon'
print(length_of_string(sample_string))


def collect_string(enter_string):
    if len(input_string) < 2:
        return ""
    return enter_string[:2] + enter_string[-2:]

print(collect_string('semicolon')) 
print(collect_string('on'))        
print(collect_string('o'))         



def add(nenter_string):
    if len(enter_string) < 3:
        return enter_string
    elif enter_string.endswith('ing'):
        return enter_string + 'ly'
    else:
        return eneter_string + 'ing'

print(add('abc'))    
print(add('string')) 
print(add('on'))     


def search_word(word_list):
    if not word_list:
        return None, 0
    
    longest_word = max(word_list, key=len)
    return longest_word, len(longest_word)

sample_data = ['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey']
word, length = search_word(sample_data)
print(f"{word}, {length}")



def remove_chars(enter_string):
    return enter_string[0::2]

sample_data = "semicolon"
print(remove_chars(sample_data))




