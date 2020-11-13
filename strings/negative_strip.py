sentence = "The quick brown fox jumped over the lazy dog."

print(sentence[-5:])


# strip function python 
url = 'https://google.com'

# print(url.strip('https://'))

# url = url.lstrip('https://') #left strip everything from the left to right with what you want to strip which is taking out https  
# url = url.rstrip('.com') # right strip strips everything from right to left with the .com as what you want to strip
# url = url.capitalize() # captitalize the word
url = url.strip('https://').strip('.com').capitalize()
url2 = (url.strip('https://' '.com')).capitalize()

print ((url.strip('https://' '.com')).capitalize())
print (url2)