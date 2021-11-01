from pygame.draw import rect
from ..variables.ui_variables import UI_VARIABLES
from .mino import Mino
from pygame import Rect

# screen = pygame.display.set_mode((300, 374))
# 멀티플레이시 screen 만 나눠서 사용 가능할듯
block_size = UI_VARIABLES.init_block_size


# 정사각형 그리는 코드
def draw_rect(x, y, color, screen):
    rect(
        screen,
        color,
        Rect(x, y, block_size, block_size)
    )


# 외곽선을 포함하여 정사각형 그리는 코드
def draw_block(x, y, color, screen):
    # 정사각형
    draw_rect(x, y, color, screen)
    # 외곽선
    rect(
        screen,
        UI_VARIABLES.grey_1,
        Rect(x, y, block_size, block_size),
        1
    )


# Mino 객체의 값을 참조하여 화면에 그림. 다음 미노와 홀드한 미노를 그리는데 사용됨.
def draw_mino(x: int, y: int, mino: Mino, rotate: int, screen):
    for i in range(4):
        for j in range(4):
            dx = x + block_size * j
            dy = y + block_size * i
            if mino.shape[rotate][i][j] != 0:
                draw_rect(dx, dy, mino.color, screen)

def draw_game_instance(game_instance, screen, x_mod=0):
    # sidebar
    rect(
        screen,
        UI_VARIABLES.white,
        Rect(204+x_mod, 0, 96, 374)
    )

    # draw next_mino
    draw_mino(220+x_mod, 140, game_instance.next_mino, 0, screen)

    # draw hold_mino
    if game_instance.hold_mino is not None:
        draw_mino(220+x_mod, 50, game_instance.hold_mino, 0, screen)

    # Set max score
    if game_instance.score > 999999:
        score = 999999

    # Draw texts
    # TODO 하드코딩 수정할것
    text_hold = UI_VARIABLES.h5.render("HOLD", 1, UI_VARIABLES.black)
    text_next = UI_VARIABLES.h5.render("NEXT", 1, UI_VARIABLES.black)
    text_score = UI_VARIABLES.h5.render("SCORE", 1, UI_VARIABLES.black)
    score_value = UI_VARIABLES.h4.render(str(game_instance.score), 1, UI_VARIABLES.black)
    text_level = UI_VARIABLES.h5.render("LEVEL", 1, UI_VARIABLES.black)
    level_value = UI_VARIABLES.h4.render(str(game_instance.level), 1, UI_VARIABLES.black)
    text_goal = UI_VARIABLES.h5.render("GOAL", 1, UI_VARIABLES.black)
    goal_value = UI_VARIABLES.h4.render(str(game_instance.goal), 1, UI_VARIABLES.black)

    # Place texts
    screen.blit(text_hold, (x_mod+215, 14))
    screen.blit(text_next, (x_mod+215, 104))
    screen.blit(text_score, (x_mod+215, 194))
    screen.blit(score_value, (x_mod+220, 210))
    screen.blit(text_level, (x_mod+215, 254))
    screen.blit(level_value, (x_mod+220, 270))
    screen.blit(text_goal, (x_mod+215, 314))
    screen.blit(goal_value, (x_mod+220, 330))

    # Draw board
    for x in range(UI_VARIABLES.init_board_width):
        for y in range(UI_VARIABLES.init_board_height):
            dx = x_mod+17 + block_size * x
            dy = 17 + block_size * y
            draw_block(dx, dy, UI_VARIABLES.t_color[game_instance.board.temp_matrix[x][y + 1]], screen)


# Draw game screen
def draw_in_game_screen(game_instance, screen, multiplayer_instance=None):
    screen.fill(UI_VARIABLES.grey_1)

    draw_game_instance(game_instance=game_instance, screen=screen)
    if multiplayer_instance is not None:
        draw_game_instance(game_instance=multiplayer_instance, screen=screen)
