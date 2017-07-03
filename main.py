import pygame
import random
from characters import *
import os
#MAIN FILE
def main(): 
    # declare the size of the canvas
    width = 900
    height = 900
    blue_color = (97, 159, 182)
    play_area_width = 825
    play_area_height = 825
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Treat Hunting')
    
    #Game initialization
    #load images
    background_image = pygame.image.load('images/background.png').convert_alpha()
    cat_image = pygame.image.load('images/orange_cat.png').convert_alpha()
    treats_image = pygame.image.load('images/treat_trophy.png').convert_alpha()
    vac_image = pygame.image.load('images/vacuum.png').convert_alpha()
    bag_image = pygame.image.load('images/evil_bag.png').convert_alpha()

    clock = pygame.time.Clock()
    pygame.mixer.music.load(os.path.join('sounds', 'Cowboy_Bebop.mp3'))#load background music
    purr = pygame.mixer.Sound(os.path.join('sounds','Cat_Purring.wav'))  #load purr sound
    scream = pygame.mixer.Sound(os.path.join('sounds','Cat_Scream.wav'))  #load scream sound
    fail = pygame.mixer.Sound(os.path.join('sounds','fail.wav'))  #load fail sound
    pygame.mixer.music.set_volume(0.1)
    purr.set_volume(1)
    pygame.mixer.music.play(-1) #play music nonstop                           


    KEY_UP = 273
    KEY_DOWN = 274
    KEY_LEFT = 276
    KEY_RIGHT = 275

    #initialize treats
    treats = Treats("Treat Trophy", random.randint(50, 800), random.randint(50, 800), play_area_width, play_area_height, treats_image)
    treats_speed = 4
    random_num1 = 1
    change_dir_countdown = 120
    
    #initialize cat
    cat_speed = 5
    cat = Cat("Garfiekins", random.randint(300,500), random.randint(300,500), play_area_width, play_area_height, cat_image)

    #initialize vacuum
    vac = Dodgees("Villainous Vacuum", random.randint(50, 800), random.randint(50, 800), play_area_width, play_area_height, vac_image)
    vac_speed = 3
    random_num2 = 2

    #initialize bag
    bag = Dodgees("Bag Bandit", random.randint(50, 800), random.randint(50, 800), play_area_width, play_area_height, bag_image)
    bag_speed = 3
    random_num3 = 3

    #initialize vac 2
    vac2 = Dodgees("Villainous Vacuum 2", random.randint(50, 800), random.randint(50, 800), play_area_width, play_area_height, vac_image)
    random_num4 = 4

    #inizialize bag 2
    bag2 = Dodgees("Bag Bandit 2", random.randint(50, 800), random.randint(50, 800), play_area_width, play_area_height, bag_image)
    random_num5 = 5


    stop_game = False
    while not stop_game:
        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image,(0,0))

        #move the treats random directions
        if change_dir_countdown == 0:
            change_dir_countdown = 120
            random_num1 = random.randint(1,8)
            random_num2 = random.randint(1,8) 
            random_num3 = random.randint(1,8)
            random_num4 = random.randint(1,8)
            random_num5 = random.randint(1,8)          
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
        treats.update(treats_speed, random_num1)
        vac.update(vac_speed, random_num2)
        bag.update(bag_speed, random_num3) 
        vac2.update(vac_speed, random_num4)
        bag2.update(bag_speed, random_num5) 
        cat.update(cat_speed)
        cat.check_collision(treats, purr)
        

        # Game display
        treats.render(screen, treats_image)
        cat.render(screen, cat_image)
        vac.render(screen, vac_image)
        bag.render(screen, bag_image)
        vac2.render(screen, vac_image)
        bag2.render(screen, bag_image)


        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()

if __name__ == '__main__':
    main()
