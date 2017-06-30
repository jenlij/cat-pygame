import pygame
import random
from characters import *

def choose_character(icon1, icon2, icon3):
    print "Choose a character (1, 2, 3)"
    print "1. Garfiekins"
    print "2. Evil Ollie"
    print "3. Moo Moo"
    character = raw_input("> ")
    return character

def main():
    # declare the size of the canvas
    width = 900
    height = 900
    blue_color = (97, 159, 182)
    play_area_width = 825
    play_area_height = 825
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Treat Hunting')
    
    #Game initialization
    background_image = pygame.image.load('images/background.png').convert_alpha()
    cat_image = pygame.image.load('images/orange_cat.png').convert_alpha()
    treats_image = pygame.image.load('images/treat_trophy.png').convert_alpha()
    clock = pygame.time.Clock()
    
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
        cat.update(cat_speed)

        # Game display
        cat.render(screen, cat_image)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
