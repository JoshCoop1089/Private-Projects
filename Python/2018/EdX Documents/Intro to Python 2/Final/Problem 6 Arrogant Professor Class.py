# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:32:46 2018

@author: joshc
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: It is obvious that ' + self.name + ' says: ' + stuff
    def lecture(self, stuff):         
        return 'It is obvious that ' +Person.say(self, stuff) 
    
    
e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

stuff = [e.say('the sky is blue'),
         le.say('the sky is blue'),
         le.lecture('the sky is blue'),
         pe.say('the sky is blue'),
         pe.lecture('the sky is blue'),
         ae.say('the sky is blue'),
         ae.lecture('the sky is blue')]

for i in stuff:
    output = i
    print(output)
