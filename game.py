import numpy as np
from model import *
from menu import *
from button import *
from parameter import *

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.checkpoint = 1  #关卡
        self.member = []
        self.run = [1]#是否再进行，暂停为0，
        self.normal_run_frame = 24
        #self.run_frame = self.normal_run_frame
        #self.group_attack_status = 0 #群攻状态

    def game_load(self):
        self.l = 0  # 加载进度条
        while True:
            self.clock.tick(24)
            if self.l >= screen_size[0]:
                self.game_slect()
                return
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(im_load, ((screen_size[0] - im_load.get_width()) // 2, 0))
            pygame.draw.rect(screen, (0, 255, 0), (0, 550, self.l, 5), 0)
            r = random.randint(1, 500)
            self.l += r
            pygame.display.update()

    def game_slect(self):
        self.l = 0
        if self.checkpoint == 1:
            self.bg_map = bg_map1_1
        elif self.checkpoint == 2:
            self.bg_map = bg_map1_2
        else:
            m = (self.checkpoint - 1) // 12 + 1
            if m == 1:
                self.bg_map = bg_map1_3
            elif m == 2:
                self.bg_map = bg_map2
        while True:
            self.clock.tick(200)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(self.bg_map, pos_bg_map, (self.l, 0, screen_size[0], screen_size[1]))
            if self.l < map_size[0] - screen_size[0]:
                self.l += 1
            else:
                break
            pygame.display.update()
        self.button0 = Button0(self)
        while True:
            self.clock.tick(24)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(self.bg_map, pos_bg_map, (self.l, 0, screen_size[0], screen_size[1]))
            screen.blit(im_warehouse, pos_sun_warehouse)#显示太阳仓库
            screen.blit(bg_shovel, pos_bg_shovel)  # 显示铲子
            screen.blit(bg_level, pos_bg_level)  # 显示关卡
            surface = font3.render("关卡：" + str(self.checkpoint), False, font_color[3])
            screen.blit(surface, (pos_bg_level[0] + 10, pos_bg_level[1] + 8))
            screen.blit(im_button, pos_button_menu)#显示菜单按钮
            surface = font3.render("菜单", False, font_color[2])
            screen.blit(surface, (pos_button_menu[0] + 30, pos_button_menu[1] + 8))
            #pygame.draw.rect(screen, (0, 255, 0), (19, 9, 102, 482), 1)#区域0
            for i in range(len(self.member)):
                surface0 = font2.render(str(price[self.member[i]]), False, font_color[1])
                screen.blit(card[self.member[i]][1], (pos_card_member[0], pos_card_member[1] + card_size[1] * i))
                screen.blit(surface0, (pos_card_member[0] + 60, pos_card_member[1] + 40 + card_size[1] * i))
            #pygame.draw.rect(screen, (0, 255, 0), (399, 99, 402, 302), 1)#区域1
            screen.blit(bg_card, pos_bg_card)
            for i in range(species):
                m = i // 4
                n = i % 4
                if i in self.member or i + 1 > self.checkpoint:
                    screen.blit(card[i][0], (pos_card_select[0] + card_size[0] * n,
                                                       pos_card_select[1] + card_size[1] * m))
                else:
                    screen.blit(card[i][1], (pos_card_select[0] + card_size[0] * n,
                                                       pos_card_select[1] + card_size[1] * m))
                surface0 = font2.render(str(price[i]), False, font_color[1])
                screen.blit(surface0, (pos_card_select[0] + 60 + card_size[0] * n,
                                            pos_card_select[1] + 40 + card_size[1] * m))
            #pygame.draw.rect(screen, (0, 255, 0), (500, 432, 202, 69), 1)  # 区域3
            screen.blit(button_start, pos_button_start)
            if self.button0.action(events) == 1:
                self.game_ready()
                return
            if self.run[0] == 0:
                self.time_out()
            pygame.display.update()

    def game_ready(self):
        while self.l > 0:
            self.clock.tick(200)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(self.bg_map, pos_bg_map, (self.l, 0, screen_size[0], screen_size[1]))
            screen.blit(im_warehouse, pos_sun_warehouse)
            screen.blit(im_button, pos_button_menu)
            surface = font3.render("菜单", False, font_color[2])
            screen.blit(surface, (pos_button_menu[0] + 30, pos_button_menu[1] + 8))
            for i in range(len(self.member)):
                surface0 = font2.render(str(price[self.member[i]]), False, font_color[1])
                screen.blit(card[self.member[i]][1], (pos_card_member[0], pos_card_member[1] + card_size[1] * i))
                screen.blit(surface0, (pos_card_member[0] + 60, pos_card_member[1] + 40 + card_size[1] * i))
            pygame.display.update()
            self.l -= 1
        self.time = 0
        while self.time < len(im_start) * 16:
            self.clock.tick(24)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(self.bg_map, pos_bg_map, (0, 0, screen_size[0], screen_size[1]))
            screen.blit(im_warehouse, pos_sun_warehouse)
            screen.blit(im_button, pos_button_menu)
            surface = font3.render("菜单", False, font_color[2])
            screen.blit(surface, (pos_button_menu[0] + 30, pos_button_menu[1] + 8))
            for i in range(len(self.member)):
                surface0 = font2.render(str(price[self.member[i]]), False, font_color[1])
                screen.blit(card[self.member[i]][1], (pos_card_member[0], pos_card_member[1] + card_size[1] * i))
                screen.blit(surface0, (pos_card_member[0] + 60, pos_card_member[1] + 40 + card_size[1] * i))
            screen.blit(im_start[self.time // 16], pos_im_start)
            pygame.display.update()
            self.time += 1
        self.game_start()

    def game_start(self):
        self.menu = Menu(self.member)
        self.model = Model(self)
        self.square = np.zeros((5, 9))
        """[[0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0]]"""
        self.max_speed = 3
        self.speed = [1]
        self.button1 = Button1(self)
        while True:
            self.clock.tick(self.normal_run_frame * self.speed[0])
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.load_background()
            self.load_battlefield()
            self.model.action()
            self.button1.action(events)
            if self.model.win[0] != -1:
                self.game_over()
                break
            if self.run[0] == 0:
                self.time_out()
            pygame.display.update()

    def time_out(self):
        self.button3 = Button3(self)
        while True:
            self.clock.tick(24)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(bg_timeout, pos_bg_timeout) #菜单界面背景图
            screen.blit(im_button, pos_im_menu_button0)  # 选择按钮0
            surface = font3.render("重新开始", False, font_color[2])
            screen.blit(surface, (pos_im_menu_button0[0] + 10, pos_im_menu_button0[1] + 8))
            screen.blit(im_button, pos_im_menu_button1)  # 选择按钮1
            surface = font3.render("继续游戏", False, font_color[2])
            screen.blit(surface, (pos_im_menu_button1[0] + 10, pos_im_menu_button1[1] + 8))
            screen.blit(im_button, pos_im_menu_button2)  # 选择按钮2
            surface = font3.render("退出游戏", False, font_color[2])
            screen.blit(surface, (pos_im_menu_button2[0] + 10, pos_im_menu_button2[1] + 8))
            screen.blit(im_button, pos_im_menu_button3)  # 选择按钮3
            surface = font3.render("选择关卡", False, font_color[2])
            screen.blit(surface, (pos_im_menu_button3[0] + 10, pos_im_menu_button3[1] + 8))

            if self.button3.action(events) == 1:
                break
            pygame.display.update()

    def game_over(self):
        self.button2 = Button2(self)
        self.member = []
        if self.model.win[0] == 0:
            while True:
                self.clock.tick(24)
                events = pygame.event.get()
                for event in events:
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                self.load_lose()
                n = self.button2.action(events)
                if n == 0:
                    self.game_slect()
                elif n == 1:
                    pygame.quit()
                    sys.exit()
                pygame.display.update()
        else:
            while True:
                self.clock.tick(24)
                events = pygame.event.get()
                for event in events:
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                self.load_background()
                self.load_battlefield()
                self.model.action()
                self.load_win()
                n = self.button2.action(events)
                if n == 0:
                    self.game_slect()
                elif n == 1:
                    self.checkpoint += 1
                    self.game_slect()
                pygame.display.update()

    def choose_level(self):
        self.button4 = Button4(self)
        #pos0 = [480, 140, 720, 300]#关卡选择区域
        #pos1 = [548, 320, 660, 360]#返回按钮
        while True:
            self.clock.tick(24)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(bg_card, pos_bg_card)
            for i in range(24):
                m = i // 6
                n = i % 6
                screen.blit(im_button0, (pos_level_choose[0] + n * button0_size[0],
                                                   pos_level_choose[1] + m * button0_size[1]))
                surface = font3.render(str(i + 1), False, font_color[2])
                screen.blit(surface, (pos_level_choose[0] + 10 + n * button0_size[0],
                                           pos_level_choose[1] + 5 + m * button0_size[1]))
            screen.blit(im_button, pos_button_return)
            surface = font3.render("返回游戏", False, font_color[2])
            screen.blit(surface, (pos_button_return[0] + 10, pos_button_return[1] + 8))
            if self.button4.action(events) == 1:
                break
            pygame.display.update()
        pass

    def load_background(self):
        screen.blit(self.bg_map, pos_bg_map)#显示地图
        screen.blit(im_warehouse, pos_sun_warehouse)#显示阳光仓库
        surface = font1.render(str(self.menu.sunlight), False, font_color[1])
        screen.blit(surface, (pos_sun_warehouse[0] + 50, pos_sun_warehouse[1] + 8))  # 显示阳光数量
        screen.blit(bg_shovel, pos_bg_shovel)#显示铲子
        screen.blit(bg_level, pos_bg_level)#显示关卡
        surface = font3.render("关卡：" + str(self.checkpoint), False, font_color[3])
        screen.blit(surface, (pos_bg_level[0] + 10, pos_bg_level[1] + 8))
        if self.speed[0] == 1:#显示加速按钮
            screen.blit(im_speed_up0, (pos_im_speed_up[0], pos_im_speed_up[1]))
        else:
            screen.blit(im_speed_up1, (pos_im_speed_up[0], pos_im_speed_up[1]))
        surface = font3.render("X" + str(self.speed[0]), False, font_color[2])
        screen.blit(surface, (pos_im_speed_up[0] + im_speed_up0.get_size()[0] + 2, pos_im_speed_up[1] + 5))#显示加速倍数
        screen.blit(im_button, pos_button_menu)#显示菜单按钮
        surface = font3.render("菜单", False, font_color[2])
        screen.blit(surface, (pos_button_menu[0] + 30, pos_button_menu[1] + 8))
        for i in range(len(self.member)):#显示卡片信息
            if self.menu.now_cd[self.member[i]] >= max_cd[self.member[i]] and\
                    self.menu.sunlight >= price[self.member[i]]:
                im = card[self.member[i]][1]
            else:
                im = card[self.member[i]][0]
            surface0 = font2.render(str(price[self.member[i]]), False, font_color[1])
            screen.blit(im, (pos_card_member[0], pos_card_member[1] + card_size[1] * i))
            screen.blit(surface0, (pos_card_member[0] + 60, pos_card_member[1] + 40 + card_size[1] * i))
            pygame.draw.rect(screen, (0, 255, 0), (pos_card_member[0] - 5, i * card_size[1] + pos_card_member[1] + 5, 4, 50), 0)
            persentage = self.menu.now_cd[self.member[i]] / max_cd[self.member[i]]
            if persentage < 1:
                pygame.draw.rect(screen, (255, 0, 0), (pos_card_member[0] - 5, i * card_size[1] + pos_card_member[1] + 5, 4, 50 * (1 - persentage)), 0)

    def load_battlefield(self):
        for i in self.model.plants:#显示植物
            screen.blit(i.image, i.pos0)
        for i in self.model.zombies:#显示僵尸
            screen.blit(i.image, i.pos0)
            if i.max_HP > i.HP > 0:
                pygame.draw.rect(screen, (0, 255, 0), (i.pos[0] - i.w // 2, i.pos0[1] + 10, i.w, 4), 1)
                persentage = i.HP / i.max_HP
                if persentage > 0:
                    pygame.draw.rect(screen, (255, 0, 0), (i.pos[0] - i.w // 2, i.pos0[1] + 10, i.w * persentage, 4), 0)
            if i.ice_time > 0 and i.HP > 0:
                screen.blit(im_ice, (i.pos[0] - i.w // 2 + 5, i.pos0[1] + 15))
        for i in self.model.bullets:#显示子弹
            screen.blit(i.image, i.pos0)

    def load_lose(self):
        screen.blit(im_lose, pos_im_over)#失败图标
        screen.blit(im_button, pos_im_over_button0)#选择按钮1
        surface = font3.render("重新开始", False, self.model.menu.font_color[2])
        screen.blit(surface, (pos_im_over_button0[0] + 10, pos_im_over_button0[1] + 8))
        screen.blit(im_button, pos_im_over_button1)  # 选择按钮1
        surface = font3.render("退出游戏", False, self.model.menu.font_color[2])
        screen.blit(surface, (pos_im_over_button1[0] + 10, pos_im_over_button1[1] + 8))

    def load_win(self):
        screen.blit(im_win, pos_im_over)#胜利图标
        screen.blit(im_button, pos_im_over_button0)#选择按钮1
        surface = font3.render("重新开始", False, self.model.menu.font_color[2])
        screen.blit(surface, (pos_im_over_button0[0] + 10, pos_im_over_button0[1] + 8))
        screen.blit(im_button, pos_im_over_button1)  # 选择按钮1
        surface = font3.render("下一关卡", False, self.model.menu.font_color[2])
        screen.blit(surface, (pos_im_over_button1[0] + 10, pos_im_over_button1[1] + 8))



if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.game_load()