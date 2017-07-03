import pygame
#MAIN FILE
class Characters(pygame.sprite.Sprite):
    def __init__(self,name, x, y, play_area_width, play_area_height, icon):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.play_area_width = play_area_width
        self.play_area_height = play_area_height
        self.image = icon
        self.rect = self.image.get_rect() 
        self.alive = True

    def update(self, speed):
        self.x += self.speed_x
        self.y += self.speed_y 
        self.rect.topleft = self.x, self.y

    def render(self, screen, icon):
        if self.alive == True:
            screen.blit(icon,(self.x, self.y))

    def check_collision(self, sprite1, sound_effect):
        col = pygame.sprite.collide_rect(self, sprite1)    
        if col == True:
            sprite1.alive = False
            sound_effect.play(loops = 0, maxtime = 2000)
            
        
class Treats(Characters):
    def update(self, speed, random_num):
        if random_num == 1: #move N     
            self.speed_y = -speed
        elif random_num == 2: #move S
            self.speed_y = speed
        elif random_num == 3: #move E
            self.speed_x = speed
        elif random_num == 4: #move W
            self.speed_x = -speed
        elif random_num == 5: #move NE
            self.speed_x = speed
            self.speed_y = -speed
        elif random_num == 6: #move NW
            self.speed_x = -speed
            self.speed_y = -speed  
        elif random_num == 7: #move SE
            self.speed_x = speed
            self.speed_y = speed
        elif random_num == 8: #move SW
            self.speed_x = -speed
            self.speed_y = speed 

        if self.x > self.play_area_width:
            self.x = 0
        if self.x < 0:
            self.x = self.play_area_width
        if self.y > self.play_area_height:
            self.y = 0
        if self.y < 0:
            self.y = self.play_area_height
        super(Treats, self).update(speed)     


class Cat(Characters):
    def update(self, speed):
        super(Cat, self).update(speed) 
        if self.x > self.play_area_width - 25:
            self.speed_x = 0
            self.x = self.play_area_width - 25
        if self.y > self.play_area_height:
            self.speed_y = 0
            self.y = self.play_area_height
        if self.x < 25:
            self.speed_x = 0
            self.x = 25
        if self.y < 25:
            self.speed_y = 0
            self.y = 25      


class Dodgees(Treats): #plastic bag and vacuum (and potentially the other 2 cats)
    def check_collision(self, sprite1, sound_effect, sound_effect2, hits):
        col = pygame.sprite.collide_rect(self, sprite1)  
        if col == True:
            sound_effect.play(loops = 0, maxtime = 2000)
        if hits > 20:
            sound_effect.stop()
            sprite1.alive = False
            sound_effect2.play(loops = 0, maxtime = 4000)
        if hits > 25:
            sound_effect2.stop()    
        return col    