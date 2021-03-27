class Hero():
    hp = 0
    power = 0
    name = ""

    def fight(self, enemy_hp, enemy_power):
        my_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if my_hp > enemy_final_hp:
            print(f"这次是我{self.name}的胜利，哈哈")
        elif my_hp <enemy_final_hp:
            print("怎么可能，是我输了吗？")
        else:
            print("这次算你好运，我们放学后见。")

    def speak_lines(self):
        if self.name == "提莫":
            print("提莫队长正在待命")
        elif self.name == "女警":
            print("见识一下法律的子弹")
