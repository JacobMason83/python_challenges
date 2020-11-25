import random 
# make a manual incrementing matrix
# need to have a way to auto create a list 
#need the first list to start at 0 then next list starting at 1 then so on 
# # gotta have rows and columns for the matrix 



# def makeCostMatrix(n,m):
#     return [[random.randint(0,5) for row in range(n)] for column in range(m)]

# print(makeCostMatrix(5,5))

# def manual_incrementing_matrix(num):
#     neo = 0
#     morpheous = 0
#     for row in range(num):
#         new_li = new_li.append(row) 
#         for column in range(num):
#          li = li.append(column)
#     return "join"(new_li * li)


def manual_incrementing_matrix(n):
    #matrix n * n 
    matrix = [ [ None for y in range(n)] for x in range(n)]
    
    counter = 0
    
    for idx, el in enumerate(matrix):
        
        for nested_idx, nested_el in enumerate(el):
            matrix[idx][nested_idx] = counter + nested_idx
            
        counter += 1
    
    
    return matrix
    

print(manual_incrementing_matrix(5))








# manual_incrementing_matrix(5)  #should get a 5 by 5 grid