# """
# You have been given a raw data dump that is structured as an array of objects. 
# The object's keys are companies, and the values are arrays of emails followed by a 3 digit department number. 
# I need you to write a program that will go through the data, print the emails for each company and what department number that email belongs to.
#import beautifsoup 4 

data_dump = [
{ "Google": ["test@test.com 123", "test@test.com 321", "test@test.com 451", "test@test.com 123" ]},
{ "Yahoo": ["test@test.com 123", "test@test.com 321", "test@test.com 451", "test@test.com 451" ]},
{ "IBM": ["test@test.com 888", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
{ "GREGS": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
{ "AUTO SHOP": ["test@test.com 888", "test@test.com 555", "test@test.com 555", "test@test.com 123" ]},
{ "PAWN SHOP": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Nike": ["test@test.com 123", "test@test.com 123", "test@test.com 555", "test@test.com 123" ]},
{ "Franks": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]},
{ "Tims": ["test@test.com 123", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
{ "Apple": ["test@test.com 123", "test@test.com 555", "test@test.com 123", "test@test.com 123" ]},
{ "Sony": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Disney": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
{ "Popies": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Sally": ["test@test.com 123", "test@test.com 555", "test@test.com 888", "test@test.com 123" ]},
{ "Henry": ["test@test.com 123", "test@test.com 555", "test@test.com 555", "test@test.com 555" ]},
{ "Dave's": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]}
]

# sort_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

# for i in sort_data:
# 	print(i[0], i[1])

# def data_formatter(data):
#     data_dump = data.split(',')  
#     for data in data_dump.keys():
#      print(data)



# print(data_dump[0])   
# def data_dump_formatter(data):
#     li = data
	
#     index = 0
#     for i in li[index]:
#      for key, value in li[index].items():
#          li.sorted(key=int, )
#       index += 1
# def data_dump_sort_format(data):
#   sorted_dict = {}
#   count = 0

#   for i in sorted_values[count]:
#    sorted_values = sorted(data.values()) # Sort the values
#    for k in data.keys():
#         if data[k] == i:
#             sorted_dict[k] = data[k]
#             count+= 1
#             break

      
# print(data_dump_sort_format(data_dump))  

# def email_printer(data):
#       li = []
#       counter = 0
#  # have to loop thru first list
#       for j in data[counter].items():  
#           count = j       
#           for key, value in data[j].items():
#                 li.append("key")
#                 li.sorted(value)
#                 li.append( value)
#                 counter += 1
#       return "".join(li)
    
# print(email_printer(data_dump))
         
        
 # then loop thru dictionary to get to next list
 #then have to sort thru next list by numbers  
 
# from dump import data 
# def email_sort_formatter(data):
#   company = data  
#   for key in company[counter]:
#     counter = 0 
#     keys = key
#     value = company[counter]        
#     counter += 1
#     values =( f"""
# Here is a list of the compainies and the emails associated with it:
#  The company name is {keys}:
#  and the emails are as follows {value}
#  """)
#     return values

def email_sort_formatter(data):
      count = 0
      li = []
      company = data
      for key in company:
        idx = key
      #   li.append(idx)
        for email in company[count]:         
          count += 1
      #     li.append(email)
#       return f"""
# Here is a list of the companies and the emails asociated with them:
# {idx}: \n {values}
#"""
          li.append( f"""
Company         Email List
{idx}:           {email}
""")
      return li
  
   
          
               
         
          
#     formatted_list.append(i)
#     counter += 1
          
  
#return f" {company_email[:-3]} dept: {company_email[-3:]}"     
    
    
print(email_sort_formatter(data_dump))  


# What is a Class in python? a class is a blueprint for your program , you can put functionality and wrap it all up in one place and allows you to create methods to use across your program
# What is a dunder method in Python? is by putting __init__ the underscores before and after the name to allow to protected or private in python
# What is self in python and how might we use it? self is the class itslef or the variable itself
# How does inheritance work in python? whatever main class you have and you create a subclass you can have it inherit the attributes of the main class
# What is pipenv? a private enviroment for you to run everything in / basically a private server
# What is Polymorphism? allows you to create a method in a class and have it be used in others you can have it inherited into the subclass you can use it in the subclasses as you see fit
# What is the purpose of __init__ in python? it is the constructor value for the class 
# What is a decorator and what is its purpose in python? it allows you to specify and tell people how to use your class, like writing a story, its the @property, or @function name
# What is a Generator in python? it allows you to use it like an iterator value in python 
# How do you declare a new instance of a class?  var_name = ClassName(whatever you want)
