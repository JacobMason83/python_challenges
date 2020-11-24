#overview of dunder method aka magic methods 
# the double underscore had to do with the private and protected methods, unlike in other languages they have private methods or protected methods
# and they would have limited visability in anything outside of the class itself 
# dunder str 
class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total
        
    def __str__(self): #this is used usally for helping debug the class , helpful way to get information on the class 
        return f'Invoice from {self.client} for {self.total}'
    
#dunder repr is for raw data , to your air log , or logs  repr means representation of the data at that instance 
    def __repr__(self):
        return f'Invoice < value: client: {self.client}, total: {self.total} >'
inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))

