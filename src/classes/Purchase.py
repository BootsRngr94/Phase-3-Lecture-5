class Purchase():

# TODO: make list of all purchases ✅
    all = []

    def __init__(self, person, makeup_item, date = "03/04/2020"):
        self._person = person
        self._makeup_item = makeup_item
        self._date = date

        Purchase.all.append(self)

        # TODO: construct purchase object as SSOT ✅
        self.person.makeup_items.append(self.makeup_item) # person.makeup_items.append(makeup_item)
        self.person.purchases.append(self) # person.purchases.append(self)

        self.makeup_item.owners.append(self.person) # makeup_item.owners.append(person)
        self.makeup_item.purchases.append(self) # makeup_item.purchases.append(self)

    # TODO: make property for person (must be instance of People class) ✅
    # TODO: make property for makeup_item (must be instance of Makeup class) ✅

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