# remove_first_and_last(list_to_clean) 
# html = ['<h1>', 'Some content', '</h1>']

html = ['<h1>', 'Some content', '</h1>']
def remove_first_and_last(list_to_clean):
    li = list_to_clean             
    if len(li)< 3:
        return "Error Error Will Robinson, your list only has 2 items"
    else:
        li.pop()
        li.pop(0)
        return li
    
print(remove_first_and_last(html))

#globbing 
def remove_first_and_last(list_to_clean):
    _, *content, _ = list_to_clean
    if content > 3:
      return content
    else:
        return 'Error error will robinson'
