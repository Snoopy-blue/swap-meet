from swap_meet.item import Item

class Clothing(Item):
    def __init__ (self, id=None, condition=0, fabric="Unknown"):
        super().__init__(id,condition)
        self.fabric = fabric


    # stringify an number to a string using dunder method
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."    

    def get_category(self):
        return "Clothing"