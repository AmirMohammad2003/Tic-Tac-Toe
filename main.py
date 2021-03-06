import pygame

pygame.font.init()

WIDTH = 600
HEIGHT = 700
HOFFSET = 100
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# smallfont = pygame.font.SysFont("comicsans", 20)
font = pygame.font.SysFont("comicsans", 40)
largefont = pygame.font.SysFont("comicsans", 65)


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1
        self.moves = set()

    def checkValid(self, x, y):
        return False if (x, y) in self.moves else True

    def move(self, pos):
        if 0 <= pos[0] <= WIDTH and HOFFSET <= pos[1] <= HEIGHT:
            x = pos[0] * 3 // WIDTH
            y = (pos[1] - HOFFSET) * 3 // (HEIGHT - HOFFSET)
            if self.checkValid(x, y):
                self.moves.add((x, y))
                if self.turn == 1:
                    self.turn = 2
                    self.player1.moves.add((x, y))
                    if self.player1.checkWin():
                        return 1
                else:
                    self.turn = 1
                    self.player2.moves.add((x, y))
                    if self.player2.checkWin():
                        return 2
                if len(self.moves) == 9:
                    return -1

        return False


class Player:
    def __init__(self):
        self.moves = set()

    def checkWin(self):
        for i in range(3):
            ho, ve, ri, li = set(), set(), set(), set()
            for j in range(3):
                if (j, i) in self.moves: ho.add((j, i))
                if (i, j) in self.moves: ve.add((i, j))
                if (j, j) in self.moves: ri.add((j, j))
                if (2 - j, j) in self.moves: li.add((2 - j, j))

            if len(ho) == 3 or len(ve) == 3 or len(ri) == 3 or len(li) == 3:
                return True

        return False


def redrawWindow(surface, game):
    surface.fill(WHITE)
    turn = game.turn
    text = font.render(f"Player {turn} it\'s your turn", 1, BLACK)
    surface.blit(text, (WIDTH // 2 - text.get_width() // 2,
                        HOFFSET // 2 - text.get_height() // 2))
    for i in range(2):
        pygame.draw.line(surface, BLACK, ((i + 1) * WIDTH // 3, HOFFSET),
                         ((i + 1) * WIDTH // 3, HEIGHT))
        pygame.draw.line(surface, BLACK,
                         (0, ((i + 1) * (HEIGHT - HOFFSET) // 3) + HOFFSET),
                         (WIDTH,
                          ((i + 1) * (HEIGHT - HOFFSET) // 3) + HOFFSET))

    for move in game.player1.moves:
        circleMiddle = ((move[0] * WIDTH / 3) + WIDTH / 6,
                        (move[1] * (HEIGHT - HOFFSET) / 3) +
                        (HEIGHT - HOFFSET) / 6 + HOFFSET)
        pygame.draw.circle(surface, BLUE, circleMiddle, 2 * WIDTH // 15, 4)
        del circleMiddle

    radius = 2 * WIDTH // 15
    for move in game.player2.moves:
        circleMiddle = ((move[0] * WIDTH / 3) + WIDTH / 6,
                        (move[1] * (HEIGHT - HOFFSET) / 3) +
                        (HEIGHT - HOFFSET) / 6 + HOFFSET)
        pygame.draw.line(surface, RED,
                         (circleMiddle[0] - radius, circleMiddle[1] - radius),
                         (circleMiddle[0] + radius, circleMiddle[1] + radius),
                         4)
        pygame.draw.line(surface, RED,
                         (circleMiddle[0] - radius, circleMiddle[1] + radius),
                         (circleMiddle[0] + radius, circleMiddle[1] - radius),
                         4)
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
            win.blit(text, (WIDTH // 2 - text.get_width() // 2,
                            HEIGHT // 2 - text.get_height() // 2))
            run = False

        elif winner == 2:
            text = largefont.render("Player 2 Wins, Congrats!!!", 1, RED)
            win.blit(text, (WIDTH // 2 - text.get_width() // 2,
                            HEIGHT // 2 - text.get_height() // 2))
            run = False

        elif winner == -1:
            text = largefont.render("Oops Looks Like a Tie!!!", 1, RED)
            win.blit(text, (WIDTH // 2 - text.get_width() // 2,
                            HEIGHT // 2 - text.get_height() // 2))
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
        win.blit(text, (WIDTH // 2 - text.get_width() // 2,
                        HEIGHT // 2 - text.get_height() // 2))
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
