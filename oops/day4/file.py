# multi-level inheritance 
# multiple inheritance 

class Zepto: # gParent
    def __init__(self):
        self.websiteName="Zepto"
        return self.websiteName 
class Store(Zepto): # parent
    super().__init__()
    def __init__(self):
        self.StoreItems={
            "eggs":40,
            "peanut butter":45,
            "bread":26
        }
    def showItems(self):
        k=super().__init__()
        print(k,"gpraent instance var")
        for i,j in self.StoreItems.items():
            print(f"{i}:{j}","19")                
class orderProduct(Store): # child
    def __init__(self):
        super().__init__()
        super().showItems()
orderProduct()