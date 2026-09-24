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
        
        return self.swap_items(other_vendor, my_giveaway, friend_giveaway)

    def get_by_category(self, category):
        list_with_category = []
        for item in self.inventory:
            if item.get_category() == category:
                list_with_category.append(item)

        return list_with_category

    def get_best_by_category(self, category):
        list_with_category = self.get_by_category(category)
        if not list_with_category: 
            return None
        
        best_condition_item = list_with_category[0]
        for item in list_with_category:
            if item.condition > best_condition_item.condition:
                best_condition_item = item

        return best_condition_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # my_priority = category I want
        # their_priority = category friend wants

        mybest_friend_want = self.get_best_by_category(their_priority)
        friendbest_I_want = other_vendor.get_best_by_category(my_priority)

        if not mybest_friend_want or not friendbest_I_want:
            return False

        return self.swap_items(other_vendor, mybest_friend_want, friendbest_I_want)
        
        
