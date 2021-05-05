class fruit(object):
    def __init__(self,name,color,flavor, poisonous):
        self.name=name
        self.color=color
        self.flavor=flavor
        self.poisonous=poisonous
    def description(self):
        print("I'm a %s %s and I taste %s."%(self.color, self.name, self.flavor))
    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible.")
        else:
            print("Don't eat me! I am super poisonous.")

lemon=fruit("lemon","yellow","sour",False)
lemon.description()
lemon.is_edible()

strawberry=fruit("sugar cane","green","sweet",True)
strawberry.description()
strawberry.is_edible()
