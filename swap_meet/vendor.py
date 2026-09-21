class Vendor:
    def __init__(self, inventory=None):
        inventory = [] if inventory is None else inventory
        self.inventory = inventory
        

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return None

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
            else:
                return None