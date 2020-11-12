number_list = []
# operator = {
#   '+': Operator.add,
#   '-': Operator.sub,
#   '*': Operator.mul,
#   '/': Operator.truediv
# }

# def dynamic_reducer(operator, number_list):
#   for operator in operator:
#     if operator == '+':
#       Operator.add(number_list)
#     elif operator == '-':
#       Operator.sub(number_list)
#     elif operator == operator:
#       Operator.mul(number_list)
#     else :
#       Operator.truediv(number_list)


  
#   print(dynamic_reducer('+', [1,2,3]))


def dynamic_reducer(collection, op):
  operators = {
    '+': operator.add,
    '-': operator.sub,
    "*": operator.mul,
    '/':operator.truediv
  }
  return reduce((lambda total, element: operators[op](total, element)), collection)

print(dynamic_reducer([1,2,3], '+'))
print(dynamic_reducer([1,2,3], '-'))
print(dynamic_reducer([1,2,3], '*'))
print(dynamic_reducer([1,2,3], '/'))


def lambda (total, element):
 (operators[op](total,element)
