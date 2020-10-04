
import random
from zombies.zombies import *


class Model:
    def __init__(self, game):
        self.game = game
        self.time = 0
        self.time_preparation = 20 * 24 #僵尸进攻前准备时间
        self.win = [-1]#输赢判定，-1胜负未分，0失败，1胜利
        self.run = game.run  #游戏运行状态0-暂停，1-进行
        self.checkpoint = (game.checkpoint - 1) % 12 + 1
        self.max_frequency = 15     #僵尸最大进攻间隔
        self.frequency = self.max_frequency     #僵尸进攻间隔
        self.attack_number = 0 #群攻次数
        self.attack_end = 0 #1-攻击结束
        self.max_attack_number = (self.checkpoint - 1) // 2 + 1
        self.attack_status = 1 #进攻状态0进攻方式转换，1个体单独进攻，2群攻
        self.attack_time_interval = 24 * 6
        self.ap_size = im_attack_process_component1.get_size()#攻击进程表大小
        self.pos_ap = (pos_im_attack_process_component1[0] + self.ap_size[0],
                    pos_im_attack_process_component1[1]) #攻击进程僵尸初始坐标
        self.l = 0 #进度条已攻击长度
        if self.game.checkpoint == 1:
            self.attack_road = [2, 2]
        elif self.game.checkpoint == 2:
            self.attack_road = [1, 3]
        else:
            self.attack_road = [0, 4]
        self.menu = game.menu
        self.plants = []
        self.zombies = []
        self.bullets = []
    def action(self):
        if self.run[0] == 0:
            return
        if self.win[0] == 0:
            return
        for i in self.plants:
            i.action(self)
        for i in self.zombies:
            i.action(self)
            if i.pos[0] <= win_distance_zombies:
                self.win[0] = 0
        for i in self.bullets:
            i.action(self)
        self.menu.action()
        self.clear(self.game.square)
        if self.time_preparation > 0:
            self.time_preparation -= 1
        else:
            self.load_attack()
            self.zombies_attack()

    def add_zombie(self, k, r):
        s = "self.zombies.append(Zombie" + str(k) + "(r))"
        eval(s)

    def clear(self, square):#清理战场
        for i in self.plants:
            #i.action(self.zombies, self.bullets)
            if i.exist == 0:
                self.plants.remove(i)
                square[i.ranks[0]][i.ranks[1]] = 0
        for i in self.zombies:
            #i.action(self.plants, self.win)
            if i.exist == 0:
                self.zombies.remove(i)
        for i in self.bullets:
            #i.action(self.zombies, self.menu)
            if i.exist == 0 or i.pos[0] >= 1200:
                self.bullets.remove(i)

    def zombies_attack(self):
        if self.attack_end == 1:
            if len(self.zombies) == 0:
                self.win[0] = 1
            return
        if self.attack_status == 1:     #1个体单独进攻
            self.time += 1
            if self.frequency >= 2:
                if self.time == self.frequency * 24 or len(self.zombies) == 0:
                    #更新进度条
                    l = 1 - (self.frequency - 2) / (self.max_frequency - self.attack_number - 2)
                    self.l = (self.attack_number + l) * ((self.ap_size[0] - 10) // self.max_attack_number)

                    self.time = 0
                    self.frequency -= 1
                    k = random.randint(1, self.attack_number + 1)
                    r = random.randint(self.attack_road[0], self.attack_road[1])
                    if k == self.max_attack_number and k > 1:
                        k0 = k - 1
                    else:
                        k0 = k
                    self.add_zombie(k0, r)
            elif self.time >= 10 or len(self.zombies) == 0:
                self.attack_status = 0
                self.time = -1
                if self.attack_number < self.max_attack_number - 1:
                    self.im_attack_tips = im_group_attack
                else:
                    self.im_attack_tips = im_last_attack
        elif self.attack_status == 0:   #0进攻方式转换
            self.time += 1
            if self.time == 3 * 24:
                self.attack_status = 2
                self.time = 0
                self.attack_number += 1
        else:                           #2群攻
            k = self.time // self.attack_time_interval
            if k > self.attack_number:
                if self.attack_number >= self.max_attack_number:
                    self.attack_end = 1
                else:
                    self.attack_status = 1
                    self.frequency = self.max_frequency - self.attack_number
                    self.time = 0
            elif self.time % self.attack_time_interval == 0:
                if k == self.max_attack_number and k > 1:
                    k0 = k - 1
                else:
                    k0 = k
                for i in range(self.attack_road[0], self.attack_road[1] + 1):
                    self.add_zombie(k0, i)
            elif self.time % self.attack_time_interval == self.attack_time_interval // 2:
                n = self.checkpoint - k * 2 + 1
                if n > 0:
                    if k == self.max_attack_number and k > 1:
                        k0 = k - 1
                    else:
                        k0 = k
                    for i in range(n):
                        r = random.randint(self.attack_road[0], self.attack_road[1])
                        self.add_zombie(k0, r)
            self.time += 1

    def load_attack(self):
        #显示攻击进度条
        screen.blit(im_attack_process_component0, pos_im_attack_process_component0)
        screen.blit(im_attack_process_component1, pos_im_attack_process_component1)
        screen.blit(im_attack_process_component2, (self.pos_ap[0] - self.l - 10, self.pos_ap[1]),
                    (self.ap_size[0] - self.l - 10, 0, self.ap_size[0], self.ap_size[1]))
        for i in range(self.max_attack_number):  # 显示旗子
            if self.attack_number <= i:
                screen.blit(im_attack_process_component3,
                            (self.pos_ap[0] - 10 - (self.ap_size[0] - 10) // self.max_attack_number * (i + 1), self.pos_ap[1] + 3))
            else:
                screen.blit(im_attack_process_component3,
                            (self.pos_ap[0] - 10 - (self.ap_size[0] - 10) // self.max_attack_number * (i + 1), self.pos_ap[1] - 5))
        screen.blit(im_attack_process_component4, (self.pos_ap[0] - self.l - 10, self.pos_ap[1]))

        #显示攻击提示
        if self.attack_status == 0:
            screen.blit(self.im_attack_tips, pos_im_attack_tips)







