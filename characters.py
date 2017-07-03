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
        #self.rect = self.image.get_rect() 

    def update(self, speed):
        self.x += self.speed_x
        self.y += self.speed_y 
        
    def render(self, screen, icon):
        screen.blit(icon,(self.x, self.y))


class Treats(Characters):
    def update(self, speed):
        super(Treats, self).update(speed) 
        if self.x >= self.play_area_width:
            self.x = 0
        if self.x <= 0:
            self.x = self.play_area_width
        if self.y >= self.play_area_height:
            self.y = 0
        if self.y <= 0:
            self.y = self.play_area_height
        if self.x >= self.play_area_width or self.y >= self.play_area_height:
            self.x = 0
            self.y = 0
        if self.x <= 0 or self.y >= self.play_area_height:
            self.x = self.play_area_width
            self.y = 0
        if self.x >= self.play_area_width or self.y <= 0:
            self.x = 0
            self.y = self.play_area_height
        if self.x <= 0 or self.y >= self.y <= 0:
            self.x = self.play_area_width
            self.y = self.play_area_height
    

        if random_num == 1: #move N     
            treats.speed_y = -treats_speed
        elif random_num == 2: #move S
            treats.speed_y = treats_speed
        elif random_num == 3: #move E
            treats.speed_x = treats_speed
        elif random_num == 4: #move W
            treats.speed_x = -treats_speed
        elif random_num == 5: #move NE
            treats.speed_x = treats_speed
            treats.speed_y = -treats_speed
        elif random_num == 6: #move NW
            treats.speed_x = -treats_speed
            treats.speed_y = -treats_speed  
        elif random_num == 7: #move SE
            treats.speed_x = treats_speed
            treats.speed_y = treats_speed
        elif random_num == 8: #move SW
            treats.speed_x = -treats_speed
            treats.speed_y = treats_speed 



class Cat(Characters):
    def update(self, speed):
        super(Cat, self).update(speed) 
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


class Dodgees(Characters): #plastic bag and vacuum (and potentially the other 2 cats)
    pass        