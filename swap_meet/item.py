import uuid 
class Item:
    def __init__(self, id=None):      
        if id is None:
            id = uuid.uuid4().int
        self.id = id

    # stringify an number to a string using dunder method 
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def get_category(self):
        return "Item"

    