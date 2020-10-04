from parameter import *


#大食花
class Plant4:
    def __init__(self, ranks):
        self.id = 4           #植物编号 大食花
        self.exist = 1  # 是否存在
        self.max_HP = 150
        self.HP = self.max_HP           #植物血量
        self.hp = 0 #吞下的僵尸的血量
        self.hurt = 1000
        self.digest_time = 0  #消化时间
        self.frame = 0          #帧
        self.actions = 0        #动作状态0-11
        self.normal_fs = 3  # 正常每张图片播放几帧
        self.fs = self.normal_fs  # 每张图片播放几帧
        self.status = 0         #行为状态：0-生长，1-成熟，3-攻击
        self.ranks = ranks          #位置行列
        self.r = ranks[0]
        self.im0 = load_image("game_picture/plants/plant4/0")
        self.im1 = load_image("game_picture/plants/plant4/1")
        self.im2 = load_image("game_picture/plants/plant4/2")
        self.im = [self.im0, self.im1, self.im2]
        self.image = self.im[self.status][self.actions]
        self.size = []  # 不同状态下的大小
        for i in self.im:
            self.size.append(i[0].get_size())
        self.pos = [(self.ranks[1] + 0.5) * lawn_cube_size[0] + pos_lawn[0] + 10,
                    (self.ranks[0] + 1) * lawn_cube_size[1] + pos_lawn[1] - plant_offset_up]  # 实际位置
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置
        self.attack_distance = 150  # 攻击触发距离
        self.attack_range = [self.ranks[1] * lawn_cube_size[0] + pos_lawn[0],
                             (self.ranks[1] + 2.1) * lawn_cube_size[0] + pos_lawn[0]]  # 攻击触发范围

    def action(self, model):
        if self.HP <= 0:
            self.exist = 0
            return
        if self.status == 0:
            for i in model.zombies:
                if self.r == i.r:
                    if self.attack_range[0] < i.pos[0] < self.attack_range[1]:
                        self.status = 1
                        self.actions = 0
                        self.time = 0
                        break
        elif self.status == 1:
            self.attack(model.zombies)
        else:
            self.digest()
        if self.frame == 0:
            self.actions = (self.actions + 1) % len(self.im[self.status])
        self.frame = (self.frame + 1) % self.fs
        self.image = self.im[self.status][self.actions]
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])  # 图片显示位置

    def attack(self, zombies):
        self.time += 1
        if self.time == len(self.im[1]) * self.fs * 7 // 9 -1:
            self.x = 0#判断是否能吃到僵尸
            for i in zombies:
                if self.r == i.r and i.HP > 0:
                    if self.attack_range[0] < i.pos[0] < self.attack_range[1]:
                        if self.x == 0:
                            self.target = i
                        elif self.target.pos[0] > i.pos[0]:
                            self.target = i
                        self.x = 1
            if self.x == 1:
                self.hp = self.target.HP
                self.target.HP = 0
                self.target.exist = 0
                if self.hp <= 200:
                    self.digest_time = 10
                elif self.hp <= 400:
                    self.digest_time = 15
                elif self.hp <= 800:
                    self.digest_time = 20
                else:
                    self.digest_time = 30
        elif self.time == len(self.im[1]) * self.fs - 1:
            if self.x == 0:
                self.status = 0
            else:
                self.status = 2
                self.time = 24 * self.digest_time  # 消化时间（帧数）
            self.actions = 0

    def digest(self):
        self.time -= 1
        if self.time <= 0:
            self.status = 0


Plant4((1, 1))