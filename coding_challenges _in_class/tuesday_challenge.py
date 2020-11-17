#write a python program that checks whether if a string is a palendrome or not. 
# ie => racecar => racecar, ryan => nayr no
# define a function that takes in a word 
# checks if its the same forwards and backwords 
# if it is print word 
def palendrome(words):
    reverse_word = words[::-1]
    # for i in words:
    if words == reverse_word:
        return f"""
        The word {words} is an Palindrome which 
        is the same forwards and backwards 
        {words}:{reverse_word}
        """.strip()
    else: 
        return "This is not a Palindrome... sorry"

print(palendrome('racecar'))
print(palendrome('ADA'))
print(palendrome('bob'))
print(palendrome('eseese'))


    