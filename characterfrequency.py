# Name: Katlyne Kaziga
# Reg number: AIIM/01432/2024

#Character frequency counting

#Method 1: Using a dictionary
def char_frequency_dict(s):
    freq = {}
    for char in s :
        if char in freq:
            freq[char] +=1
        else:
            freq[char] = 1
    return freq
text = "structures"
frequency_dict = char_frequency_dict(text)
print(frequency_dict)

#Method 2: Using dict.get()
def char_frequency_dict_get(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        return freq
    text = "structures"
frequency_dict_get = char_frequency_dict_get(text)
print(frequency_dict_get)

#Method 3: Using collections.Counter
from collections import Counter
def char_frequency_counter(s):
    return dict(Counter(s))
text = "structures"
frequency_counter = char_frequency_counter(text)
print(frequency_counter)

#Method 4: Using str.count() method
def char_frequency_count_method(s):
    freq = {}
    for char in s:
        freq[char] = s.count(char)
        return freq 
    text = "structures"
    print(char_frequency_count(text))
    