from parameter import *
import math


class Bullet1:
    def __init__(self, ranks):
        self.id = 1
        self.exist = 1
        self.speed = 8
        self.actions = 0
        self.attack_power = 25
        self.attack_distance = self.speed           #攻击距离
        self.destination = [pos_sun_warehouse[0] + 10, pos_sun_warehouse[1] + 30]
        self.status = 0
        self.ranks = ranks  #行列（H，W）高宽
        self.pos = [self.ranks[1] * lawn_cube_size[0] + pos_lawn[0] + 40, (self.ranks[0] + 1) * lawn_cube_size[1] + pos_lawn[1] - 60]    #宽
        self.im0 = load_image("game_picture/plants/bullet0/0")
        self.im = [self.im0]
        self.size = []  # 不同状态下的大小
        for i in self.im:
            self.size.append(i[0].get_size())
        self.image = self.im[self.status][self.actions]
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置

    def action(self, model):
        x = self.pos[0] - self.destination[0]
        y = self.pos[1] - self.destination[1]
        c = math.sqrt(x*x + y*y)
        if c < self.attack_distance:
            self.exist = 0
            model.menu.sunlight += self.attack_power
        else:
            self.move(x, y, c)
        self.image = self.im[self.status][self.actions]
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置
        self.actions = (self.actions + 1) % 22

    def move(self, x, y, c):
        self.pos[0] = self.pos[0] - self.speed * x // c
        self.pos[1] = self.pos[1] - self.speed * y // c


Bullet1((1, 1))