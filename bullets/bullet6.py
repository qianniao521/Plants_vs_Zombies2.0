
from parameter import *

class Bullet6:
    def __init__(self, ranks):
        self.id = 1
        self.HP = 6
        self.exist = 1
        self.speed = 10
        self.ice_time = 6
        self.attack_power = 10
        self.attack_distance = 30
        self.status = 0
        self.ranks = ranks  #行列（H，W）高宽
        self.r = ranks[0]
        self.pos = [self.ranks[1] * lawn_cube_size[0] + pos_lawn[0] + 60, (self.ranks[0] + 1) * lawn_cube_size[1] + pos_lawn[1] - 70]
        self.attack_range = [self.pos[0] - self.attack_distance, self.pos[0] + self.attack_distance / 2]  # 攻击范围
        self.im0 = pygame.image.load("game_picture/plants/bullet6/0/0.png")
        #gif0 = pygame.transform.scale(gif0, (46, 28))      #pygame.Rect((22, 4, 20, 20)
        self.im1 = pygame.image.load("game_picture/plants/bullet6/1/1.png")
        self.im = [self.im0, self.im1]
        self.size = []  # 不同状态下的大小
        for i in self.im:
            self.size.append(i.get_size())
        self.image = self.im[self.status]
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置

    def action(self, model):
        if self.status == 1:
            self.attack(model.zombies, -1)
        else:
            self.attack_range = [self.pos[0] - self.attack_distance, self.pos[0] + self.attack_distance / 2]  # 攻击范围
            for i in range(len(model.zombies)):
                if self.r == model.zombies[i].r and model.zombies[i].HP > 0:
                    if self.attack_range[0] < model.zombies[i].pos[0] < self.attack_range[1]:
                        self.status = 1
                        self.time = 4
                        self.attack(model.zombies, i)
                        break
        if self.status == 0:
            self.move()
        self.image = self.im[self.status]
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置

    def move(self):
        self.pos[0] = self.pos[0] + self.speed
    def attack(self, zombies, i):
        if i >= 0:
            zombies[i].HP -= self.attack_power
            zombies[i].ice_time = self.ice_time * 24
            zombies[i].speed = zombies[i].normal_speed / 2
            zombies[i].fs = zombies[i].normal_fs * 1.5 // 1 + 1
        elif self.time == 0:
            self.exist = 0
        self.time -= 1


Bullet6((1, 1))