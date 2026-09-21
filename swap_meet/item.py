import uuid 
class Item:
    def __init__(self, id=None):
        self.id = id
        if id is None:
            self.id = uuid.uuid4().int
        

    def get_category(self):
        return "Item"