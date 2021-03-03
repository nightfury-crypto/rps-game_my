import pygame
from random import randint

# Initialize pygame
# Solve play sounds latency
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 750, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROCK PAPER SCISSOR")
winLogo = pygame.image.load('WORK/ico.png')
pygame.display.set_icon(winLogo)


pygame.mixer.music.load('WORK/main.mp3')
pygame.mixer.music.play(-1)

# DATA
buttom1 = pygame.image.load('WORK/play.png')
buttom1_rect = buttom1.get_rect()
buttom1_rect.center = (150, 156)
buttom2 = pygame.image.load('WORK/quit.png')
buttom2_rect = buttom2.get_rect()
buttom2_rect.center = (150, 236)
logo = pygame.image.load('WORK/intro2.png')

# Rock , Paper, Scissor
rock1 = pygame.image.load('WORK/rock1.png') # Rock
rock1_rect = rock1.get_rect()
rock1_rect.center= (180, HEIGHT-50)

paper1 = pygame.image.load('WORK/paper1.png') # Paper
paper1_rect = paper1.get_rect()
paper1_rect.center= (380, HEIGHT-50)


scissor1 = pygame.image.load('WORK/scissor1.png') # Scissor
scissor1_rect = scissor1.get_rect()
scissor1_rect.center= (580, HEIGHT-50)


# TEXT
START_FONT_head = pygame.font.SysFont('comicsans', 40)
comp_wins = pygame.font.SysFont('microsoftyibaiti', 20)
player_wins = pygame.font.SysFont('microsoftyibaiti', 20)
comp_pick = pygame.font.SysFont('comicsans', 30)
player_pick = pygame.font.SysFont('comicsans', 30)


base_font = pygame.font.SysFont('microsoftyibaiti', 20)
base_vs = pygame.font.SysFont('comicsans', 40)

# COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
COLOR = (136,212,0)
RED = (255, 0, 0)

# Variables
Computer = ["ROCK", "PAPER", "SCISSOR"]



# listss
comp_lst = []  # Computer
player_lst = []  # Player


def playSound(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()


    
    
# Not edited yet
def game():
    screen.fill(WHITE)
    # pygame.mouse.set_pos(150, 175)
    running = True
    while running:
        playSound('WORK/main.mp3')
        pygame.mixer.music.play(-1)
        
        
        
       

        # game visual screen
        pygame.draw.rect(screen, BLACK, (10, 50, 10, HEIGHT-200))
        pygame.draw.rect(screen, BLACK, (WIDTH-20, 50, 10, HEIGHT-200))
        pygame.draw.rect(screen, BLACK, (WIDTH/2-2.5, 50, 5, HEIGHT-350))
        pygame.draw.rect(screen, BLACK, (0, HEIGHT-10, WIDTH, 60))
        result_rect = pygame.Rect(WIDTH/2-100, 250, 200, 50)
        


        # on screen rock, paper scissor
        pygame.draw.rect(screen, BLACK, (150, HEIGHT-80, 60, 60))
        screen.blit(rock1, (150, HEIGHT-80,))

        pygame.draw.rect(screen, BLACK, (350, HEIGHT-80, 60, 60))
        screen.blit(paper1, (350, HEIGHT-80))

        pygame.draw.rect(screen, BLACK, (550, HEIGHT-80, 60, 60))
        screen.blit(scissor1, (550, HEIGHT-80))

        playSound('WORK/bg_sound.mp3')
        pygame.mixer.music.play(-1)
        

        # Mouse
        # mouse = pygame.mouse.get_pos()

        mx, my = pygame.mouse.get_pos()
        # Analyzes each game event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, WHITE, (10, 20, WIDTH/2-10, 30))
                pygame.draw.rect(screen, WHITE, (WIDTH/2, 20, WIDTH/2-10, 20))
                pygame.draw.rect(screen, WHITE, (30, 130, WIDTH/2-50, 200))
                pygame.draw.rect(screen, WHITE, (WIDTH/2+10, 130, WIDTH/2-50, 200))
                pygame.draw.rect(screen, BLACK, result_rect)

                computer_choice = Computer[randint(0,2)] # Computer choice
                p_player = player_pick.render("PLAYER WON", 1, COLOR)
                pdraw = player_pick.render("OOPS , DRAW", 1, COLOR)
                c_comp = player_pick.render("COMPUTER WON", 1, COLOR)
                # c_comp = player_pick.render("Pls. choose first", 1, COLOR)


                    #  ROCK LOGIC
                if rock1_rect.collidepoint((mx, my)):
                    comp_picks = comp_pick.render(computer_choice, 1, RED)
                    screen.blit(comp_picks , (50 , 150))
                    player_choice = "ROCK"

                    screen.blit(rock1, (WIDTH/2+200 , 200))
                    comp_picks = comp_pick.render(player_choice, 1, RED)
                    screen.blit(comp_picks , (WIDTH/2+200 , 150))

                    if (computer_choice == player_choice):
                        screen.blit(rock1, (50, 200))
                        screen.blit(pdraw , (result_rect.x + 20 , result_rect.y + 15))
                    elif computer_choice == "SCISSOR" and player_choice == "ROCK":
                        screen.blit(scissor1, (50 , 200))
                        screen.blit(p_player , (result_rect.x + 20 , result_rect.y + 15))
                        player_lst.append(1)
                        
                    else:
                        screen.blit(paper1, (50 , 200))
                        screen.blit(c_comp , (result_rect.x + 20 , result_rect.y + 15))
                        comp_lst.append(1)
                    
                        #  PAPER LOGIC
                elif paper1_rect.collidepoint((mx, my)):
                    
                    comp_picks = comp_pick.render(computer_choice, 1, RED)
                    screen.blit(comp_picks , (50 , 150))
                    player_choice = "PAPER" 
                    screen.blit(paper1, (WIDTH/2+200 , 200))
                    comp_picks = comp_pick.render(player_choice, 1, RED)
                    screen.blit(comp_picks , (WIDTH/2+200 , 150))
                    if (computer_choice == player_choice):
                        screen.blit(paper1, (50 , 200))
                        screen.blit(pdraw , (result_rect.x + 20 , result_rect.y + 15))
                    elif computer_choice == "ROCK" and player_choice == "PAPER":
                        screen.blit(rock1, (50 , 200))
                        screen.blit(p_player , (result_rect.x + 20 , result_rect.y + 15))
                        player_lst.append(1)
                    else:
                        screen.blit(scissor1, (50 , 200))
                        screen.blit(c_comp , (result_rect.x + 20 , result_rect.y + 15))
                        comp_lst.append(1)

                        # SCISSOR LOGIC
                elif scissor1_rect.collidepoint((mx, my)):
                    
                    comp_picks = comp_pick.render(computer_choice, 1, RED)
                    screen.blit(comp_picks , (50 , 150))
                    player_choice = "SCISSOR"
                    screen.blit(scissor1, (WIDTH/2+200 , 200))
                    comp_picks = comp_pick.render(player_choice, 1, RED)
                    screen.blit(comp_picks , (WIDTH/2+200 , 150))
                    if (computer_choice == player_choice):
                        screen.blit(scissor1, (50 , 200))
                        screen.blit(pdraw , (result_rect.x + 20 , result_rect.y + 15))
                        
                    elif computer_choice == "PAPER" and player_choice == "SCISSOR":
                        screen.blit(paper1, (50 , 200))
                        screen.blit(p_player , (result_rect.x + 20 , result_rect.y + 15))
                        player_lst.append(1)
                    else:
                        screen.blit(rock1, (50 , 200))
                        screen.blit(c_comp , (result_rect.x + 20 , result_rect.y + 15))
                        comp_lst.append(1)
                # else:
                #     screen.blit(c_comp , (result_rect.x + 20 , result_rect.y + 15))

        a = len(comp_lst)
        b = len(player_lst)   
        
        comp_wins_count = comp_wins.render('Computer - '+ str(a), 1, BLACK)
        screen.blit(comp_wins_count , (20 , 20))
        player_wins_count = player_wins.render('Player - ' + str(b), 1, BLACK)
        screen.blit(player_wins_count , (WIDTH - comp_wins_count.get_width() - 10 , 20))    
        comp_picks = comp_pick.render('Computer Picked- ', 1, BLACK)
        screen.blit(comp_picks , (30 , 100))
        player_picks = player_pick.render('Player Picked- ', 1, BLACK)
        screen.blit(player_picks , (WIDTH/2+30 , 100))

        
        pygame.display.update()

        
# Not edited yet
def menu():
    playing = True
    while playing:
        screen.fill((255,255,255))
        Start_head = START_FONT_head.render('ROCK PAPER SCISSOR', True, BLACK)
        screen.blit(Start_head , (WIDTH/2-160 , 50))

        screen.blit(logo, (200, 90))
        pygame.draw.rect(screen, WHITE, (45, 120, 210, 73))
        screen.blit(buttom1, (50, 125))
        pygame.draw.rect(screen, WHITE, (45, 200, 210, 73))
        screen.blit(buttom2, (50, 205))
        pygame.display.update()

        
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttom1_rect.collidepoint((mx, my)):
                    playSound('WORK/buttonSound.wav')
                    game()
                elif buttom2_rect.collidepoint((mx, my)):
                    playSound('WORK/resetSound.wav')
                    playing=False
        



if __name__ == "__main__":
    menu()
    