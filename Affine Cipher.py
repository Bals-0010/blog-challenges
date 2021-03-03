"""
Create a Affine Cipher function which takes input string and encrytes with some criteria

Note: first constraint is the multiplier of the character and second constraint is for addition

Explanation:

Input(s):
HELLO
3
4

Output:
ZQLLU

for H will be 7 so  -> 7  * first_constraint + second_constraint  =  7 * 3 + 4 = 21 + 4 = 25 
so, H will become Z
for E will be 4 so  -> 4  * first_constraint + second_constraint  =  4 * 3 + 4 = 12 + 4 = 16 
so, E will become Q
for L will be 11 so -> 11 * first_constraint + second_constraint  = 11 * 3 + 4 = 33 + 4 = 37
so 37 > 26, hence the number should not be greater than 25
then result = old_result - 26 , i.e: result = 37 - 26 = 11
hence for L it will be 11 and the character will be L

"""

def affine_cipher():
    alphabets         = "abcdefghijklmnopqrstuvwxyz".upper() # Can be done in one liner:  list('str'.upper())
    alphabets_list    = list(alphabets)
    input_string      = input().upper()
    first_constraint  = int(input())
    second_constraint = int(input())
    result = []
    
    for _ in input_string:
        temp = (alphabets_list.index(_) * first_constraint) + second_constraint 
        if temp >= 26:
            temp = temp - 26
        result.append(alphabets_list[temp])

    return "".join(result)
    
print(affine_cipher())