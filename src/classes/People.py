class People():

    def __init__(self, name, age):
        #Lines 6 & 7 These lines assign the values of name and age passed as parameters to attributes _name and _age respectively. 
        #Note: the _(underscores) convention in Python to indicate that these attributes are intended to be "protected" or "private"
        self._name = name
        self._age = age

        # Initializes makeup_items as an empty list
        self.makeup_items = []
        # Initializes purchase as an empty list
        self.purchase = []

    #decorator that allows you to define a method as a "getter" for a class attribute.
    @property
    #creates a property called name
    def name(self):
        return self._name
    #decorator used to define a method as a "setter" for a class attribute. It allows you to set a new value for the name property.
    @name.setter
    def name(self, name):
        #Lines 20-28: This is the setter method for the name property. 
        # It takes a name parameter, and if the provided name is a string with more than 3 characters, 
        # it updates the _name attribute. Otherwise, it raises an exception.
        if type(name) == str and len(name) > 3:
            self._name = name
        else:
            raise Exception("Name must be a string of more than 3 characters!")
    # second decorator pair. 
    @property
    #Similar to name, there are age and age.setter methods defined for the age property.
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if type(age) == int and age > 12:
            self._age = age
        else:
            raise Exception("Age must be an integer greater than 12!")
    
    # This method is used to define the string representation(or repr) of an instance of the People class. 
    def __repr__(self):
    #returns a formatted string containing the person's name and age.    
        return f"Name: {self.name}\nAge: {self.age}"