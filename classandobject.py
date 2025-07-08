class avenger:
    def __init__(self, name, age, gender, superpower, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.superpower = superpower
        self.weapon = weapon
    def get_info(self):
        print("name:", self.name)
        print("age:", self.age)
        print("gender:", self.gender)
        print("power:", self.superpower)
        print("weapon:", self.weapon)
    def is_leader(self):
        if self.name == "iron man":
            print("leader: yes")
        else:
            print("leader: no")

hero1 = avenger("captain america", 35, "male", "super strength", "shield")
hero2 = avenger("iron man", 46, "male", "technology", "armor")
hero3 = avenger("black widow", 30, "female", "superhuman", "batons")
hero4 = avenger("hulk", 41, "male", "unlimited strength", "no weapon")
hero5 = avenger("thor", 45, "male", "super energy", "mjolnir")
hero6 = avenger("hawkeye", 38, "male", "fighting skills", "bow and arrows")

heroes = [hero1, hero2, hero3, hero4, hero5, hero6]

for hero in heroes:
    hero.get_info()
    hero.is_leader()
    print()
