# the dunder int function builder snytax 
class Invoice:
     def __init__(self, client, total): 
         #This is a special reserved word and constructor method this is gonna run when the class is instantiated  self is always first argument 
         self._client = client #this instance self.client is equal to client
         self._total = total # this instance self.total is equal to total and is bound to this class object   
         
     def formatter(self):
         return f'{self._client} owes:  ${self._total}'
    #  getters 
     @property
     def client(self):
         return self._client
     @property
     def total(self):
         return self._total
     #setters 
     @client.setter
     def client(self, client):
         self._client = client
         
         
     
google = Invoice('Google', 100)
snapchat = Invoice('Snapchat', 200)

print(google.formatter())
print(snapchat.formatter())
# get and set in python 
# print(google.client)
 # this is how you set google.client to yahoo this way 
# its rare to have easy acess to get totals or clients , and in other languages you would have to set and get in the class
print(google._total)
print(google._client)
google.client = 'Yahoo'
print(google._client)
