def creer_quadrillage():
    u=175
    for y in range(1,5):
        pygame.draw.line(screen, (0,0,0), [0,u*y], [700,u*y])
    for x in range(1,5):
        pygame.draw.line(screen, (0,0,0), [u*x,0], [u*x,700])

def find_in_lists(lists, x):
    res = 0
    for l in lists:
        res += l.count(x)
    return res

def clique_sur_patience(board, screen):
    while find_in_lists(board, 1) <= 3:
        if find_in_lists(board, 1) == 0:
            for i in range(2):
                y = randint(0,3)
                x = randint(0,3)
                if board[y][x] == 0:
                    pygame.draw.rect(screen, (0,0,0), pygame.Rect(175,175, y*175, x*175))
                

def creer_carre_aleatoire(tab,x,y):
    if board[y][x] == 0:
        pygame.draw.rect(screen , (0,0,0), pygame.Rect(x*175,y*175,175,175))
        board[y][x] = 1

def put_random_square():
    """
    creat a random black square on the screen so that the player can hit it.
    """
    y = randint(0,3)
    x = randint(0,3)
    while board[y][x] == 1:
        y = randint(0,3)
        x = randint(0,3)
    pygame.draw.rect(screen , (0,0,0), pygame.Rect(x*175,y*175,175,175))
    board[y][x] = 1


def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))