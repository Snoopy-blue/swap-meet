import uuid 
class Item:
    def __init__(self, id=None, condition=0.0):      
        if id is None:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition

    def condition_description(self):
        if 0.0 <= self.condition <= 1.0:
            return f"Fair"
        elif 1.0 < self.condition <= 2.0: 
            return f"Good"
        elif 3.0 < self.condition <= 4.0: 
            return f"Excellent"
        elif 4.0 < self.condition <= 5.0: 
            return f"Brand-new"

    # stringify an number to a string using dunder method 
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def get_category(self):
        return "Item"

    

