#heading_generator(title, heading_type)
# heading_generator('Greeting', '1')  
# <h1> Greeting </h1> 

def heading_generator(title, h_number):
    h_num = h_number
    for heading_num in range(1,7):  
      if h_num == heading_num:   
       return f'<h{heading_num}>{title}</h{heading_num}>'
      
    
        
print(heading_generator('Greeting', 1))
print(heading_generator('Hey There', 0))
print(heading_generator('Yo Ryan', 2))
print(heading_generator('Yo Cian', 3))
print(heading_generator('My Day', 4))
        