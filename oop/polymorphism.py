#abstract class that is gonna be used with inheritence and subclasses
#common convention, you dont want anyone to call and instatiate it , but use methods out of it 
class Html:
    def __init__(self, content):
        self.content = content
  # the render method raise error is there so that all the subclasses use it 
    def render(self):
        raise NotImplementedError('Subclass must implement render method')
    
# class Heading(Html):
#     def render(self):
#         return f'<h1>{self.content}>/h1>'
#     # we have two classes that use the method from html , and each child class has different ways of using it 
#     #and we leveraged, classes, polymorphism, and inheritence to make a custom html generator
# class Div(Html):
#     def render(self):
#         return f'<div>{self.content}</div>'
    
# tags = [
#     Div('some content'),
#     Heading('Some big heading'),
#     Div('Another Div')
# ]

# for tag in tags :
#     print(tag.render()) #were using polymorphism poly means many and morphism means changes, means one item
    # can have many forms 
#polymorphic functions 
class Heading:
    def __init__(self, content):
        self.content = content
    def render(self):
        return f'<h1>{self.content}>/h1>'
    # we have two classes that use the method from html , and each child class has different ways of using it 
    #and we leveraged, classes, polymorphism, and inheritence to make a custom html generator
class Div:
    def __init__(self, content):
        self.content = content
    def render(self):
        return f'<div>{self.content}</div>'
    

div_one = Div('some content')
heading = Heading('Some big heading')
div_two =   Div('Another Div')

def html_render(tag_object):
    print(tag_object.render())
    
html_render(div_one)
html_render(div_two)
html_render(heading)

#Parent class 
class Fish:
    def  __init__(self, first_name, last_name='Fish', skeleton='Bone', eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
        
    def swim(self):
        return 'Swim Forwards'
    
    def swim_backwards(self):
        return "Swim backwards"
    
    #Inherietance 
    
class Trout(Fish):
        pass
    
bob = Trout('Bob', 'Fishers') 
print(bob.first_name + ' ' + bob.last_name)   
print(bob.eyelids)   
print(bob.swim())   
print(bob.swim_backwards())  

#subclass with its own class methood
class Clownfish(Fish):
    def live_with_anemone(self):
        return 'The clownfish is coexisting with sea anemome'
    

casey = Clownfish('Casey')
print(casey.first_name + ' ' + casey.last_name) 
print(casey.swim()) 
print(casey.live_with_anemone()) 

class Shark(Fish):
    #override constructor and swimbackwards methods, but inherits the swim method
    def __init__(self, first_name, last_name='Shark', skeleton='cartilage', eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
        
    #polymorphism
    def swim_backwards(self):
        return 'The shark cannot swim backwards, but can sink backwards'
    
sammy = Shark('Sammy')
print(sammy.first_name + ' ' + sammy.last_name) 
print(sammy.swim()) 
print(sammy.swim_backwards()) 

# multiple inheritence 
class Coral:
    def community(self):
        return 'Coral lives in a community'
    
class Anemome:
    def protect_clownfish(self):
        return 'The anemome is protecting the clownfish'
class CoralReef(Coral, Anemome):
    pass 

great_barrier = CoralReef
print(great_barrier.community())
print(great_barrier.protect_clownfish())


