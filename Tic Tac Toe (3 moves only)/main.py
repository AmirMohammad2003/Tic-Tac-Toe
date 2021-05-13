# Copyright (c) Amir Mohammad Ghadimi
# inspired by the original Tic Tac Toe Game

import pygame

pygame.font.init()
width = 600
height = 700
hoffset = 100
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")
# smallfont = pygame.font.SysFont("comicsans", 20)
font = pygame.font.SysFont("comicsans", 40)
largefont = pygame.font.SysFont("comicsans", 65)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1
        self.moves = list()

    def checkValid(self, x, y):
        return False if (x, y) in self.moves else True

    def move(self, pos):
        if 0 <= pos[0] <= width and hoffset <= pos[1] <= height:
            x = pos[0] * 3 // width
            y = (pos[1] - hoffset) * 3 // (height - hoffset)
            if self.checkValid(x, y):
                self.moves.append((x, y))
                if self.turn == 1:
                    self.turn = 2
                    self.player1.moves.append((x, y))
                    if len(self.player1.moves) > 3:
                        self.player1.moves.pop(0)
                        self.moves.pop(0)

                    if self.player1.checkWin():
                        return 1

                else:
                    self.turn = 1
                    self.player2.moves.append((x, y))
                    if len(self.player2.moves) > 3:
                        self.player2.moves.pop(0)
                        self.moves.pop(0)

                    if self.player2.checkWin():
                        return 2

        return False


class Player:
    def __init__(self):
        self.moves = list()

    def checkWin(self):
        for i in range(3):
            ho = set()
            ve = set()
            ri = set()
            li = set()
            for j in range(3):
                if (j, i) in self.moves:
                    ho.add((j, i))

                if (i, j) in self.moves:
                    ve.add((i, j))

                if (j, j) in self.moves:
                    ri.add((j, j))

                if (2 - j, j) in self.moves:
                    li.add((2 - j, j))

            if len(ho) == 3 or len(ve) == 3 or len(ri) == 3 or len(li) == 3:
                return True

        return False


def redrawWindow(surface, game):
    surface.fill(WHITE)
    turn = game.turn
    text = font.render(f"Player {turn} it\'s your turn", 1, BLACK)
    surface.blit(text, (width // 2 - text.get_width() // 2,
                        hoffset // 2 - text.get_height() // 2))
    for i in range(2):
        pygame.draw.line(surface, BLACK, ((i + 1) * width // 3, hoffset),
                         ((i + 1) * width // 3, height))
        pygame.draw.line(surface, BLACK,
                         (0, ((i + 1) * (height - hoffset) // 3) + hoffset),
                         (width,
                          ((i + 1) * (height - hoffset) // 3) + hoffset))

    for sequence, move in enumerate(game.player1.moves):
        circleMiddle = ((move[0] * width / 3) + width / 6,
                        (move[1] * (height - hoffset) / 3) +
                        (height - hoffset) / 6 + hoffset)
        text = largefont.render(str(sequence + 1), 1, GREY)
        surface.blit(text, ((move[0] * width / 3) + width / 6 - text.get_width() // 2,
                        (move[1] * (height - hoffset) / 3) +
                        (height - hoffset) / 6 + hoffset - text.get_height() // 2))
        pygame.draw.circle(surface, BLUE, circleMiddle, 2 * width // 15, 4)
        del circleMiddle

    radius = 2 * width // 15
    for sequence, move in enumerate(game.player2.moves):
        circleMiddle = ((move[0] * width / 3) + width / 6,
                        (move[1] * (height - hoffset) / 3) +
                        (height - hoffset) / 6 + hoffset)
        pygame.draw.line(surface, RED,
                         (circleMiddle[0] - radius, circleMiddle[1] - radius),
                         (circleMiddle[0] + radius, circleMiddle[1] + radius),
                         4)
        pygame.draw.line(surface, RED,
                         (circleMiddle[0] - radius, circleMiddle[1] + radius),
                         (circleMiddle[0] + radius, circleMiddle[1] - radius),
                         4)
        text = largefont.render(str(sequence + 1), 1, GREY)
        surface.blit(text, ((move[0] * width / 3) + width / 6 - text.get_width() // 2,
                        (move[1] * (height - hoffset) / 3) +
                        (height - hoffset) / 6 + hoffset - text.get_height()))
        del circleMiddle

    del turn


def main():
    clock = pygame.time.Clock()
    run = True
    player1 = Player()
    player2 = Player()
    game = Game(player1, player2)
    winner = 0
    while run:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                winner = game.move(pos)

        redrawWindow(win, game)

        if winner == 1:
            text = largefont.render("Player 1 Wins, Congrats!!!", 1, RED)
            win.blit(text, (width // 2 - text.get_width() // 2,
                            height // 2 - text.get_height() // 2))
            run = False

        elif winner == 2:
            text = largefont.render("Player 2 Wins, Congrats!!!", 1, RED)
            win.blit(text, (width // 2 - text.get_width() // 2,
                            height // 2 - text.get_height() // 2))
            run = False

        pygame.display.update()

    pygame.time.delay(2000)
    del run

def main_menu(surface):
    clock = pygame.time.Clock()
    run = True
    while run:
        win.fill(WHITE)
        clock.tick(20)
        text = largefont.render("Click to start the GAME XD", 1, RED)
        win.blit(text, (width // 2 - text.get_width() // 2,
                        height // 2 - text.get_height() // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.display.quit()

if __name__ == '__main__':
    main_menu(win)
