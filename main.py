import pygame
import random

def main():
    # declare the size of the canvas
    width = 900
    height = 900
    blue_color = (97, 159, 182)
    play_area_width = 850
    play_area_height = 850
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Treat Hunting')
    
    #Game initialization
    background_image = pygame.transform.scale(pygame.image.load('images/background.png').convert_alpha(),(900,900))
    cat_image = pygame.transform.scale(pygame.image.load('images/orange_cat.png').convert_alpha(),(80,70))
    treats_image = pygame.transform.scale(pygame.image.load('images/treat_trophy.png').convert_alpha(),(70,80))
    clock = pygame.time.Clock()
    
    class Treats(object):
        def __init__(self,name, x, y, screen_width, screen_height):
            self.name = name
            self.x = x
            self.y = y
            self.screen_width = screen_width
            self.screen_height = screen_height
        def move_east(self, icon, speed):
            self.x += speed
            screen.blit(icon, (self.x, self.y))
            if self.x >= self.screen_width:
                self.x = 0
        def move_west(self, icon, speed):
            self.x -= speed
            screen.blit(icon, (self.x, self.y))
            if self.x <= 0:
                self.x = self.screen_width
        def move_south(self, icon, speed):
            self.y += speed
            screen.blit(icon, (self.x, self.y))
            if self.y >= self.screen_height:
                self.y = 0
        def move_north(self, icon, speed):
            self.y -= speed
            screen.blit(icon, (self.x, self.y))
            if self.y <= 0:
                self.y = self.screen_height
        def move_se(self, icon, speed):
            self.x += speed
            self.y += speed
            screen.blit(icon, (self.x, self.y))
            if self.x >= self.screen_width or self.y >= self.screen_height:
                self.x = 0
                self.y = 0
        def move_sw(self, icon, speed):
            self.x -= speed
            self.y += speed
            screen.blit(icon, (self.x, self.y))
            if self.x <= 0 or self.y >= self.screen_height:
                self.x = self.screen_width
                self.y = 0
        def move_ne(self, icon, speed):
            self.x += speed
            self.y -= speed
            screen.blit(icon, (self.x, self.y))
            if self.x >= self.screen_width or self.y <= 0:
                self.x = 0
                self.y = self.screen_height
        def move_nw(self, icon, speed):
            self.x -= speed
            self.y -= speed   
            screen.blit(icon, (self.x, self.y))     
            if self.x <= 0 or self.y >= self.y <= 0:
                self.x = self.screen_width
                self.y = self.screen_height
    
    class Cat(object):
        def __init__(self,name, x, y, play_area_width, play_area_height):
            self.name = name
            self.x = x
            self.y = y
            self.play_area_width = play_area_width
            self.play_area_height = play_area_height
            self.speed_x = 0
            self.speed_y = 0
        def update(self):
            self.x += self.speed_x
            self.y += self.speed_y    
        def render(self, screen):
            screen.blit(cat_image,(self.x, self.y))

    KEY_UP = 273
    KEY_DOWN = 274
    KEY_LEFT = 276
    KEY_RIGHT = 275

    #initialize treats
    treats_x = 50
    treats_y = 50
    treats = Treats("Treat Trophy", treats_x, treats_y, width, height)
    treats_speed = 4
    random_num = 3
    change_dir_countdown = 120
    
    #initialize cat
    cat_x = 350
    cat_y = 350
    cat_speed = 5
    cat = Cat("Garfiekins", cat_x, cat_y, play_area_width, play_area_height)


    stop_game = False
    while not stop_game:
        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image,(0,0))

        #move the treats random directions
        if change_dir_countdown == 0:
            change_dir_countdown = 120
            random_num = random.randint(1,8)

        if random_num == 1:     
            treats.move_east(treats_image, treats_speed)
        elif random_num == 2:
            treats.move_west(treats_image, treats_speed)
        elif random_num == 3:
            treats.move_north(treats_image, treats_speed)          
        elif random_num == 4:
            treats.move_south(treats_image, treats_speed)
        elif random_num == 5:
            treats.move_ne(treats_image, treats_speed)
        elif random_num == 6:
            treats.move_nw(treats_image, treats_speed)
        elif random_num == 7:
            treats.move_se(treats_image, treats_speed)   
        elif random_num == 8:
            treats.move_sw(treats_image, treats_speed)                   

        change_dir_countdown -= 1 

        for event in pygame.event.get():
            # Event handling
            #cat movement
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    cat.speed_y = cat_speed
                elif event.key == KEY_UP:
                    cat.speed_y = -cat_speed
                elif event.key == KEY_LEFT:
                    cat.speed_x = -cat_speed
                elif event.key == KEY_RIGHT:
                    cat.speed_x = cat_speed
            
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    cat.speed_y = 0
                elif event.key == KEY_UP:
                    cat.speed_y = 0
                elif event.key == KEY_LEFT:
                    cat.speed_x = 0
                elif event.key == KEY_RIGHT:
                    cat.speed_x = 0    
            if event.type == pygame.QUIT:
                stop_game = True  
    
        # Game logic
        cat.update()

        # Game display
        cat.render(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
