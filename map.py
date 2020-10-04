import pygame
import sys
from model import *
from menu import *
from button import *
from parameter import *




class Map:
    def __init__(self, model, screen):
        self.model=model
        self.screen = screen
        pygame.display.set_caption("植物大战僵尸")
        self.bg_photo = pygame.image.load("game_picture/background/白天正门.png").convert_alpha()     #加载图片
        self.bg_photo = pygame.transform.scale(self.bg_photo, map_size) #改变尺寸
        self.ice = pygame.image.load("game_picture/background/ice0.png").convert_alpha()
        self.ice = pygame.transform.scale(self.ice, (20, 20))  # 改变尺寸
        self.lose = pygame.image.load("game_picture/background/lose.png").convert_alpha()
        self.win = pygame.image.load("game_picture/background/win.png").convert_alpha()
        self.button = pygame.image.load("game_picture/background/button.png").convert_alpha()




    def load_background(self):
        self.screen.blit(self.bg_photo, (0, 0))
        pass

    def load_menu(self, menu):
        surface = menu.font1.render(str(menu.sunlight), False, menu.font_color[1])
        self.screen.blit(surface, menu.sun_pos)    #阳光数量
        for i in range(menu.num):
            if menu.now_cd[menu.member[i]] >= menu.max_cd[menu.member[i]] and menu.sunlight >= menu.price[menu.member[i]]:
                im = menu.card[i][1]
            else:
                im = menu.card[i][0]
            surface0 = menu.font2.render(str(menu.price[menu.member[i]]), False, menu.font_color[1])
            self.screen.blit(im, (20, 10 + 60 * i))
            self.screen.blit(surface0, (80,50 + 60 * i))
            pygame.draw.rect(self.screen, (0, 255, 0), (15, i*60 + 15, 4, 50), 0)
            persentage = menu.now_cd[menu.member[i]] / menu.max_cd[menu.member[i]]
            if persentage < 1:
                pygame.draw.rect(self.screen, (255, 0, 0), (15, i*60 + 15, 4, 50 * (1 - persentage)), 0)

        pass

    def load_plants(self):
        for i in self.model.plants:
            self.screen.blit(i.image, i.pos0)

        pass

    def load_zombies(self):
        for i in self.model.zombies:
            self.screen.blit(i.image, i.pos0)
            if i.max_HP > i.HP > 0:
                pygame.draw.rect(self.screen, (0, 255, 0), (i.pos0[0], i.pos0[1], i.w, 4), 1)
                persentage = i.HP / i.max_HP
                if persentage > 0:
                    pygame.draw.rect(self.screen, (255, 0, 0), (i.pos0[0], i.pos0[1], i.w* persentage, 4), 0)
            if i.ice_time > 0 and i.HP > 0:
                self.screen.blit(self.ice, (i.pos0[0] + 5, i.pos0[1] + 5))

    def load_lose(self):
        self.screen.blit(self.lose, (400, 100))#失败图标
        self.screen.blit(self.button,(900, 200))#选择按钮1
        surface =self.model.menu.font3.render("重新开始", False, self.model.menu.font_color[2])
        self.screen.blit(surface, (910, 208))
        self.screen.blit(self.button, (900, 400))  # 选择按钮1
        surface = self.model.menu.font3.render("退出游戏", False, self.model.menu.font_color[2])
        self.screen.blit(surface, (910, 408))

    def load_win(self):
        self.screen.blit(self.win, (400, 100))#胜利图标
        self.screen.blit(self.button,(900, 200))#选择按钮1
        surface = self.model.menu.font3.render("重新开始", False, self.model.menu.font_color[2])
        self.screen.blit(surface, (910, 208))
        self.screen.blit(self.button, (900, 400))  # 选择按钮1
        surface = self.model.menu.font3.render("下一关卡", False, self.model.menu.font_color[2])
        self.screen.blit(surface, (910, 408))

    def load_bullets(self):
        for i in self.model.bullets:
            self.screen.blit(i.image, i.pos)

        pass


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(map_size)
    pygame.display.set_caption("植物大战僵尸")
    menu = Menu([0, 1, 2, 3, 4, 5, 6, 7])
    model = Model(menu, [1])
    map = Map(model, screen)
    button = Button1(map)
    while True:
        clock.tick(24)
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        map.model.action(button.square)

        map.load_background()
        map.load_menu(menu)
        map.load_plants()
        map.load_zombies()
        map.load_bullets()
        button.action(events)

        if map.model.win[0] == -1:

            map.load_win()
        pygame.display.update()








