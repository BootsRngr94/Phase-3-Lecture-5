class Purchase():

    #creates a class-level attribute named all which is a list. This list will be used to keep track of all instances of the Purchase class.
    all = []

    def __init__(self, person, makeup_item, date = "03/04/2020"):
        #These lines assign the values of person, makeup_item, and date passed as parameters to attributes _person, _makeup_item, and _date 
        self._person = person
        self._makeup_item = makeup_item
        self._date = date
        #appends the current instance to the all list. This way, the class keeps track of all instances created.
        Purchase.all.append(self)

        #Lines  Constructing purchase object as SSOT (Single Source Of Truth)

        #Appends the current makeup_item to the list of makeup items owned by the person who made the purchase
        self.person.makeup_items.append(self.makeup_item) #alternate way: person.makeup_items.append(makeup_item)
        #Appends the current instance (the purchase) to the list of purchases made by the person.
        self.person.purchases.append(self) #alternate way: person.purchases.append(self)

        #Appends the person who made the purchase to the list of owners of the makeup item.
        self.makeup_item.owners.append(self.person) #alternate way: makeup_item.owners.append(person)
        #Appends the current instance (the purchase) to the list of purchases made for the makeup item.
        self.makeup_item.purchases.append(self) #alternate way: makeup_item.purchases.append(self)



    @property
    def person(self):
        return self._person
    
    @person.setter
    def person(self, person):
        from People import People
        if isinstance(person, People):
            self._person = person
        else:
            raise Exception("Person must be an instance of People class!")
        
    @property
    def makeup_item(self):
        return self._makeup_item
    
    @makeup_item.setter
    def makeup_item(self, makeup_item):
        from Makeup import Makeup
        if isinstance(makeup_item, Makeup):
            self._makeup_item = makeup_item
        else:
            raise Exception("Makeup item must be an instance of Makeup class!")

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        self._date = date

    # TODO: calculate most popular makeup brand ✅
    @classmethod
    def get_most_popular_brand(cls):
        brand_frequencies = {} # stores brands mapped to number of appearances

        for purchase in cls.all: # iterates over all purchase objects
            makeup = purchase.makeup_item # gets makeup object from purchase object
            brand = makeup.brand # gets brand attribute from makeup object

            # adds key:value pairs or increments existing key:value pair
            if brand in brand_frequencies:
                brand_frequencies[brand] += 1 # brand_frequencies[brand] = brand_frequencies[brand] + 1
            else:
                brand_frequencies[brand] = 1

        # print(brand_frequencies)

        # calculates maximum based on values (dictionary.get retrieves values)
        # and returns associated key value
        return max(brand_frequencies, key = brand_frequencies.get)

    def __repr__(self):
        return f"Purchaser: {self.person}\nMakeup Item: {self.makeup_item}\nDate: {self.date}"