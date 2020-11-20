# write a program that prints the numbers from 1 thru 100 but for 
# multiples of 3 print 'fizz', instead of the number and for the multiples of five print 
# 'buzz'. for numbers which are muliples of both three and five print 'FizzBuzz'

def fizz_buzz(max_value): 
        
    for max in range(0, max_value + 1):        
        if (max % 3 == 0) and (max % 5 == 0):
            print("FizzBuzz")
        elif(max % 5) == 0:
            print('Buzz') 
        elif(max %  3) == 0:
            print('Fizz')
        else:
            print(max)
      
print(fizz_buzz(100))
