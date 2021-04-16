# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE,BLACK, BLUE, BG
from checkers.game import Game
from minimax.algorithm import minimax
pygame.init()
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
smallfont = pygame.font.SysFont('Corbel',35)
playText = smallfont.render('PLAY' , True , BLACK)
againText = smallfont.render('Again' , True , WHITE)
quitText = smallfont.render('Quit' , True , WHITE)
winText = smallfont.render('You Won' , True , BLACK)
lossText = smallfont.render('You Lost' , True , BLACK)


gameText = smallfont.render('Game:' , True , BLACK)
diffModeText = smallfont.render('Difficulty:' , True , WHITE)

easyText = smallfont.render('Easy' , True , BLACK)
mediumText = smallfont.render('Medium' , True , BLACK)
diffText = smallfont.render('Hard' , True , BLACK)

count = 0


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    difficulty = 2
    play = 0
    condition = "WON"

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), difficulty, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            # print(game.winner())
            play = 2
            if game.winner() == WHITE:
                condition = "LOSS"

            # run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if play == 0:
                    if pos[0]>=250 and pos[0]<=350 and pos[1]>=200 and pos[1]<=240:
                        play = 1

                    if pos[0]>=200 and pos[0]<=280 and pos[1]>=96 and pos[1]<=140:
                        difficulty = 2
                    if pos[0]>=300 and pos[0]<=430 and pos[1]>=96 and pos[1]<=140:
                        difficulty = 3
                    if pos[0]>=450 and pos[0]<=530 and pos[1]>=96 and pos[1]<=140:
                        difficulty = 4

                else:
                    if play == 1:
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row, col)
                        game_state = game.move_count()
                        # count = count + 1
                        # print(game_state,count)
                        if game_state == False:
                            play = 2
                            if game.board.red_left < game.board.white_left:
                                condition = "LOSS"
                            elif game.board.white_left < game.board.red_left:
                                condition = "WIN"

                    elif play == 2:
                        if pos[0]>=170 and pos[0]<=270 and pos[1]>=300 and pos[1]<=340:
                            difficulty = 2
                            play = 0
                            game = Game(WIN)
                        elif pos[0]>=310 and pos[0]<=410 and pos[1]>=300 and pos[1]<=340:
                            run = False


        if play == 0:
            WIN.blit(BG , (0,0))
            if difficulty == 2:
                pygame.draw.rect(WIN,BLUE,(200,96,80,34))
                WIN.blit(easyText , (210,95))
            else:
                pygame.draw.rect(WIN,WHITE,(200,96,80,34))
                WIN.blit(easyText , (210,95))

            if difficulty == 3:
                pygame.draw.rect(WIN,BLUE,(300,96,130,34))
                WIN.blit(mediumText , (310,100))
            else:
                pygame.draw.rect(WIN,WHITE,(300,96,130,34))
                WIN.blit(mediumText , (310,100))

            if difficulty == 4:
                pygame.draw.rect(WIN,BLUE,(450,96,80,34))
                WIN.blit(diffText , (460,100))
            else:
                pygame.draw.rect(WIN,WHITE,(450,96,80,34))
                WIN.blit(diffText , (460,100)) 

            pygame.draw.rect(WIN,WHITE,(250,200,100,40))
            WIN.blit(playText , (260,205))
            WIN.blit(diffModeText , (40,100))

            pygame.display.update()
        else:
            if play == 1:   
                game.update()
            if play == 2:
                # print("hiii entered")
                
                pygame.draw.rect(WIN,BLUE,(140,190,320,170))
                pygame.draw.rect(WIN,WHITE,(150,200,300,150))

                pygame.draw.rect(WIN,BLACK,(170,300,100,40))
                WIN.blit(againText , (180,305))

                pygame.draw.rect(WIN,BLACK,(310,300,100,40))
                WIN.blit(quitText , (320,305))

                if condition == "WIN":
                    WIN.blit(winText , (240,225))
                elif condition == "LOSS":
                    WIN.blit(lossText , (240,225))
                
                pygame.display.update()


    
    pygame.quit()

main()