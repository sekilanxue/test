from hero_timo import Timo
from hero_police import Police


class HeroFactory:
    def creat_hero(self, name):
        if name == "timo":
            return Timo()
        elif name == "police":
            return Police()
        else:
            raise Exception("工厂很快就会有这个英雄了，尽请期待")

a = HeroFactory()
timo_fight = a.creat_hero("timo")
police_fight = a.creat_hero("police")
print("女警挑起的战争")
police_fight.speak_lines()
police_fight.fight(timo_fight.hp,timo_fight.power)
print("放学后，提莫伏击了女警")
timo_fight.speak_lines()
timo_fight.fight(police_fight.hp,police_fight.power)