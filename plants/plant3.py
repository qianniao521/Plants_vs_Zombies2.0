
from parameter import *


#土豆地雷
class Plant3:
    def __init__(self, ranks):
        self.id = 3           #植物编号 土豆地雷
        self.exist = 1  # 是否存在
        self.max_HP = 50
        self.HP = self.max_HP           #植物血量
        self.hurt = 500
        self.time = 0   #计时
        self.frame = 0          #帧
        self.actions = 0        #动作状态0-11
        self.normal_fs = 3  # 正常每张图片播放几帧
        self.fs = self.normal_fs  # 每张图片播放几帧
        self.status = 0         #行为状态：0-生长，1-成熟，3-攻击
        self.ranks = ranks          #位置行列
        self.r = ranks[0]
        self.im0 = load_image("game_picture/plants/plant3/0")
        self.im1 = load_image("game_picture/plants/plant3/1")
        self.im2 = load_image("game_picture/plants/plant3/2")
        self.im = [self.im0, self.im1, self.im2]
        self.image = self.im[self.status][self.actions]
        self.size = []  # 不同状态下的大小
        for i in self.im:
            self.size.append(i[0].get_size())
        self.pos = [(self.ranks[1] + 0.5) * lawn_cube_size[0] + pos_lawn[0],
                    (self.ranks[0] + 1) * lawn_cube_size[1] + pos_lawn[1] - plant_offset_up]  # 实际位置
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])# 图片显示位置
        self.attack_distance = 80  # 攻击触发距离
        self.attack_range = [self.ranks[1] * lawn_cube_size[0] + pos_lawn[0],
                             (self.ranks[1] + 1.1) * lawn_cube_size[0] + pos_lawn[0]]  # 攻击触发范围
        self.hurt_range = [self.ranks[1] * lawn_cube_size[0] + pos_lawn[0],
                             (self.ranks[1] + 2) * lawn_cube_size[0] + pos_lawn[0]]  # 攻击范围

    def action(self, model):
        if self.status == 0:
            if self.HP <= 0:
                self.exist = 0
                return
            self.time += 1
            if self.time >= 240:
                self.status = 1
        elif self.status == 1:
            if self.HP <= 0:
                self.exist = 0
                return
            for i in model.zombies:
                if self.r == i.r and i.HP > 0:
                    if self.attack_range[0] < i.pos[0] < self.attack_range[1]:
                        self.status = 2
                        self.time = 0
                        self.actions = 0
                        break
        else:
            self.attack(model.zombies)
        if self.frame == 0:
            self.actions = (self.actions + 1) % len(self.im[self.status])
        self.frame = (self.frame + 1) % self.fs
        self.image = self.im[self.status][self.actions]
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置

    def attack(self, zombies):
        self.time += 1
        if self.time == (len(self.im[2]) * self.fs - 1) // 2:
            for i in range(len(zombies)):
                if self.r == zombies[i].r and zombies[i].HP > 0:
                    if self.hurt_range[0] < zombies[i].pos[0] < self.hurt_range[1]:
                        zombies[i].HP -= self.hurt
                        if zombies[i].HP <= 0:
                            zombies[i].status = 0
                            zombies[i].actions = 0
                            zombies[i].r = -9
        elif self.time == len(self.im[2]) * self.fs - 1:
            self.exist = 0



Plant3((1, 1))