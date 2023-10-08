class Makeup():
    # !This is built similarly to People.py, for more in depth notes refer to that class section!
    def __init__(self, brand, type):
        #Lines 4 & 5 refer to the notes on People.py
        self._brand = brand
        self._type = type

        #Initializes owners as an empty list
        self.owners = []
        #Initializes purchases as an empty list
        self.purchases = []

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    # checks that attribute has not already been set
    def brand(self, brand): 
        #takes a brand parameter and checks if the brand attribute has already been set (using hasattr).
        if not hasattr(self, "brand"): 
            self._brand = brand
        else:
            raise Exception("Brand can be set only once!")
        
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        #checks whether the value provided for the type property is of type str( short for string). The type() function is used to determine the type of an object
        if type(type) == str:
            self._type = type
        else:
            raise Exception("Type must be a string!")
        
    def __repr__(self):
        return f"Brand: {self.brand}\nMakeup Type: {self.type}"