# li = create a new list from 0-20 omitting the numbers from the original list 

li1 = [1,3,5]


def omit_list(li1):
   new_li = []
   for num in range(21):
       if num in li1:
           pass 
       else: new_li.append(num)  
 
   return new_li

print(omit_list(li1))

omit = [1,2,3]
num_list = []
for num in range(21):
    if num in omit:
      pass 
    else:
      num_list.append(num)
      
print(num_list)

def omit_list(li1):
    li2 = []
    new_li =[]      
    for num in li1:
     for num in li2.range(21):
       if li2[num] in li1[num]:
            pass 
       else:
        new_li.append(num)
    return new_li
print(omit_list(li1))


