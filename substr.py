sentence = 'The quick brown fox jumped over the lazy dog.'

# query = sentence.find('oops')
# query_two = sentence.index('oops')
# # new_query = sentence.find(input("enter search term")) you can have a user input what they are looking for in your list or dict
# print(query)
# print(query_two)

query = 'oops' in sentence
print(query)
