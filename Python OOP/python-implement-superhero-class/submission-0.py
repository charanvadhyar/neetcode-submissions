class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        self.name=name
        self.power=power
        self.health=health



# TODO: Create Superhero instances

super_hero1=SuperHero("Batman","Intelligence",100)
super_hero2=SuperHero("Superman","Strength",150)



# TODO: Print out the attributes of each superhero

print(super_hero1.name)
print(super_hero1.power)
print(super_hero1.health)
print(super_hero2.name)
print(super_hero2.power)
print(super_hero2.health)
