# Name: Katlyne Kaziga
# Reg number: AIIM/01432/2024

#String reversal methods

#Method 1: Using slicing
str = "Data structures and algorythms"
reverse_slicing = str[::-1]
print(reverse_slicing)

#Method 2: Using a loop
def reverse_strings(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
str = "data structures"
reverse_loop = reverse_strings(str)
print(reverse_loop)

#Method 3: Using the reversed() + join()
def reverse_builtin(s):
    return''.join(reversed(s))
str = "data structures"
reverse_builtin = reverse_builtin(str)
print(reverse_builtin)

#Method 4: Using recursion
def reverse_recursive(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_recursive(s[1:]) + s[0]

str = "data structures"
reverse_recursive = reverse_recursive(str)
print(reverse_recursive)
