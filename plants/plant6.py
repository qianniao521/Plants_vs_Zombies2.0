from bullets.bullet6 import *
from parameter import *


#寒冰射手
class Plant6:
    def __init__(self, ranks):
        self.id = 6           #植物编号 豌豆射手
        self.HP = 100           #植物血量
        self.exist = 1  # 是否存在
        self.frame = 0          #帧
        self.actions = 0        #动作状态0-11
        self.normal_fs = 2  # 正常每张图片播放几帧
        self.fs = self.normal_fs  # 每张图片播放几帧
        self.status = 0         #行为状态：0-等待，2-攻击
        self.ranks = ranks          #位置行列
        self.r = ranks[0]
        self.im0 = load_image("game_picture/plants/plant6/0")
        self.im1 = load_image("game_picture/plants/plant6/0")
        self.im = [self.im0, self.im1]
        self.image = self.im[self.status][self.actions]
        self.attack_interval = 30  # 攻速,最大攻击间隔
        self.now_interval = 0  # 当前攻击间隔
        self.size = []  # 不同状态下的大小
        for i in self.im:
            self.size.append(i[0].get_size())
        self.pos = [(self.ranks[1] + 0.5) * lawn_cube_size[0] + pos_lawn[0],
                    (self.ranks[0] + 1) * lawn_cube_size[1] + pos_lawn[1] - plant_offset_up]  # 实际位置
        self.h = 20  # 图片显示向上偏移量
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])

    def action(self, model):
        if self.HP <= 0:
            self.exist = 0
            return
        if self.status == 0:
            for i in model.zombies:
                if self.r == i.r and i.HP >0:
                    self.status = 1
                    self.actions = 0
                    self.target = i
                    break
        elif self.status == 1:
            if self.target.HP > 0:
                self.attack(model.bullets)
            else:
                n = 0
                for i in model.zombies:
                    if self.r == i.r and i.HP > 0:
                        self.status = 1
                        self.actions = 0
                        self.target = i
                        n = 1
                        break
                if n == 0:
                    self.status = 0
        if self.frame == 0:
            self.actions = (self.actions + 1) % len(self.im[self.status])
        self.frame = (self.frame + 1) % self.fs
        self.image = self.im[self.status][self.actions]
        self.pos0 = pos_conversion_p(self.pos, self.size[self.status])

    def attack(self, bullets):
        if self.now_interval <= 0:
            self.add_bullet(bullets)
            self.now_interval = self.attack_interval
            self.now_interval = self.attack_interval
            self.actions = self.fs * len(self.im[1]) % self.attack_interval
            self.frame = 0
        else:
            self.now_interval -= 1

    def add_bullet(self, bullets):
        bullets.append(Bullet6(self.ranks))


Plant6((1, 1))