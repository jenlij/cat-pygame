import pygame

class Characters(pygame.sprite.Sprite):
    def __init__(self,name, x, y, play_area_width, play_area_height):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.play_area_width = play_area_width
        self.play_area_height = play_area_height
        self.rect = self.image.get_rect() 

    def update(self, speed):
        self.x += self.speed_x
        self.y += self.speed_y 

    def render(self, screen, icon):
        screen.blit(icon,(self.x, self.y))


class Treats(Characters):
    pass
        # def __init__(self,name, x, y, screen_width, screen_height):
        #     #pygame.sprite.Sprite.__init__(self)
        #     self.name = name
        #     self.x = x
        #     self.y = y
        #     self.screen_width = screen_width
        #     self.screen_height = screen_height
        #     #self.rect = self.image.get_rect()   
        # def move_east(self, icon, speed):
        #     self.x += speed
        #     #screen.blit(icon, (self.x, self.y))
        #     if self.x >= self.screen_width:
        #         self.x = 0
        # def move_west(self, icon, speed):
        #     self.x -= speed
        #     #screen.blit(icon, (self.x, self.y))
        #     if self.x <= 0:
        #         self.x = self.screen_width
        # def move_south(self, icon, speed):
        #     self.y += speed
        #     #screen.blit(icon, (self.x, self.y))
        #     if self.y >= self.screen_height:
        #         self.y = 0
        # def move_north(self, icon, speed):
        #     self.y -= speed
        #     #screen.blit(icon, (self.x, self.y))
        #     if self.y <= 0:
        #         self.y = self.screen_height
        # def move_se(self, icon, speed):
        #     self.x += speed
        #     self.y += speed
        #     #screen.blit(icon, (self.x, self.y))
        #     if self.x >= self.screen_width or self.y >= self.screen_height:
        #         self.x = 0
        #         self.y = 0
        # def move_sw(self, icon, speed):
        #     self.x -= speed
        #     self.y += speed
        #     #screen.blit(icon, (self.x, self.y))
        #     if self.x <= 0 or self.y >= self.screen_height:
        #         self.x = self.screen_width
        #         self.y = 0
        # def move_ne(self, icon, speed):
        #     self.x += speed
        #     self.y -= speed
        #     #screen.blit(icon, (self.x, self.y))
        #     if self.x >= self.screen_width or self.y <= 0:
        #         self.x = 0
        #         self.y = self.screen_height
        # def move_nw(self, icon, speed):
        #     self.x -= speed
        #     self.y -= speed   
        #     screen.blit(icon, (self.x, self.y))     
        #     if self.x <= 0 or self.y >= self.y <= 0:
        #         self.x = self.screen_width
        #         self.y = self.screen_height
    
class Cat(Characters):
    def __init__(self,name, x, y, play_area_width, play_area_height):
        self.name = name
        self.x = x
        self.y = y
        self.play_area_width = play_area_width
        self.play_area_height = play_area_height
        self.speed_x = 0
        self.speed_y = 0
    def update(self, speed):
        self.x += self.speed_x
        self.y += self.speed_y 
        if self.x >= self.play_area_width - 25:
            self.speed_x = 0
            self.x = self.play_area_width - 25
        if self.y >= self.play_area_height:
            self.speed_y = 0
            self.y = self.play_area_height
        if self.x <= 25:
            self.speed_x = 0
            self.x = 25
        if self.y <= 25:
            self.speed_y = 0
            self.y = 25    
        #self.rect.topleft = self.x, self.y   
    def render(self, screen, icon):
        screen.blit(icon,(self.x, self.y))

class Dodgees(Characters): #plastic bag and vacuum (and potentially the other 2 cats)
    pass        