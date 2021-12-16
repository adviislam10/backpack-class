class Backpack:
    # Initialize
    def __init__(self, color, size, items, open):

        self.color = color
        self.size = size
        self.items = items
        self.open = open

    # Methods
    def openBag(self):
        self.open = True
        print("Your bag has been opened")

    def closeBag(self):
        self.open = False
        print("Your bag has been closed")

    def putIn(self, item):
        if self.open == True:
            self.items.append(item)
            print(item + " has been added to your bag!")

        else:
            print("Bag is not open")

    def takeout(self, item): 
        if self.open == True:
            for i in range(len(self.items)):
                if self.items[i] == item:
                    del self.items[i]
                    return print(item + " has been removed from your bad.")
            else: 
                print(item + " not found in bag.")
        else:
            print("Bag is not open")

# Create objects
bag1 = Backpack("blue", "small", ["keys", "bottle"], False)
bag2 = Backpack("red", "medium", ["keys", "bottle"], False)
bag3 = Backpack("green", "large", ["keys", "bottle"], False)
        
bag1.openBag()
bag1.putIn("lunch")
bag1.putIn("jacket")
bag1.putIn("binder")
bag1.closeBag()
bag1.openBag()
bag1.takeout("jacket")
bag1.takeout("binder")
bag1.closeBag()