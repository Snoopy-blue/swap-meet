class Vendor:
    def __init__(self, inventory=None):
        inventory = [] if inventory is None else inventory
        self.inventory = inventory
        

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return None

        self.inventory.remove(item)
        return item
        

        self.inventory.remove(item)
        return item
        

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        my_giveaway = self.remove(my_item)
        other_vendor.inventory.append(my_giveaway)

        friend_giveaway = other_vendor.remove(their_item)
        self.inventory.append(friend_giveaway)

        return True

    def swap_first_item(self,other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_giveaway = self.inventory[0]
        friend_giveaway = other_vendor.inventory[0] 
        self.inventory.remove(my_giveaway)
        other_vendor.inventory.remove(friend_giveaway)
        other_vendor.inventory.append(my_giveaway)
        self.inventory.append(friend_giveaway)

        return True

    