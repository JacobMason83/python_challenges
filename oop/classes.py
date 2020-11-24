#will be building out real world classes
class Invoice:
    #classes are object mappers are bluprints, and can have data , and functions as well
    
    def greeting(self): # self represents the instance itself 
        return "Hi there"
# need to instantiation which is the process of creating the instance which is stored at a  point in memory
inv_one = Invoice()    
print(inv_one.greeting()) # prints <__main__.Invoice object at 0x000001B3BA8C6FD0>
 #prints dunder main dunder which means __main__ which is a pointer to main.invoice
inv_two = Invoice()
#made another instance of the invoice class again 
print(inv_two.greeting()) #prints <__main__.Invoice object at 0x00000255F3566FA0> which is stored at a different point in memory