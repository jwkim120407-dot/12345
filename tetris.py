import pygame
import random
import sys

pygame.init()

# 화면 설정
CELL = 41
COLS = 10
ROWS = 20
SIDEBAR = 320
HEADER = 70
WIDTH = COLS * CELL + SIDEBAR
HEIGHT = ROWS * CELL + HEADER

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("테트리스 - 어린이용 🎮")
clock = pygame.time.Clock()

# 한글 폰트 (없으면 기본 폰트)
try:
    font_big   = pygame.font.SysFont("malgun gothic", 38, bold=True)
    font_mid   = pygame.font.SysFont("malgun gothic", 28, bold=True)
    font_small = pygame.font.SysFont("malgun gothic", 21)
except Exception:
    font_big   = pygame.font.SysFont(None, 42, bold=True)
    font_mid   = pygame.font.SysFont(None, 32, bold=True)
    font_small = pygame.font.SysFont(None, 26)

# 색상
BG        = (30, 30, 50)
GRID_COL  = (60, 60, 90)
WHITE     = (255, 255, 255)
BLACK     = (0, 0, 0)
YELLOW    = (255, 220, 0)
CYAN      = (0, 220, 220)
SIDEBAR_BG = (20, 20, 40)
GHOST_COL = (180, 180, 180, 80)

# 테트로미노 모양 & 색깔 (밝고 귀여운 색상)
SHAPES = [
    # I
    [[1, 1, 1, 1]],
    # O
    [[1, 1],
     [1, 1]],
    # T
    [[0, 1, 0],
     [1, 1, 1]],
    # S
    [[0, 1, 1],
     [1, 1, 0]],
    # Z
    [[1, 1, 0],
     [0, 1, 1]],
    # J
    [[1, 0, 0],
     [1, 1, 1]],
    # L
    [[0, 0, 1],
     [1, 1, 1]],
]

COLORS = [
    (0, 230, 230),   # I - 하늘색
    (255, 220, 0),   # O - 노랑
    (180, 0, 230),   # T - 보라
    (0, 210, 80),    # S - 초록
    (230, 50, 50),   # Z - 빨강
    (50, 100, 255),  # J - 파랑
    (255, 150, 0),   # L - 주황
]

EMOJIS = ["🩵", "💛", "💜", "💚", "❤️", "💙", "🧡"]


def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]


def new_piece():
    idx = random.randrange(len(SHAPES))
    shape = [row[:] for row in SHAPES[idx]]
    return {
        "shape": shape,
        "color": COLORS[idx],
        "emoji": EMOJIS[idx],
        "x": COLS // 2 - len(shape[0]) // 2,
        "y": 0,
    }


def fits(board, piece, ox=0, oy=0, shape=None):
    s = shape if shape else piece["shape"]
    px, py = piece["x"] + ox, piece["y"] + oy
    for r, row in enumerate(s):
        for c, cell in enumerate(row):
            if cell:
                nx, ny = px + c, py + r
                if nx < 0 or nx >= COLS or ny >= ROWS:
                    return False
                if ny >= 0 and board[ny][nx]:
                    return False
    return True


def place(board, piece):
    for r, row in enumerate(piece["shape"]):
        for c, cell in enumerate(row):
            if cell:
                board[piece["y"] + r][piece["x"] + c] = piece["color"]


def clear_lines(board):
    full = [r for r, row in enumerate(board) if all(row)]
    for r in full:
        del board[r]
        board.insert(0, [None] * COLS)
    return len(full)


def draw_block(surface, color, gx, gy, alpha=255):
    x = gx * CELL + 1
    y = gy * CELL + 1 + HEADER
    rect = pygame.Rect(x, y, CELL - 2, CELL - 2)
    r, g, b = color
    s = pygame.Surface((CELL - 2, CELL - 2), pygame.SRCALPHA)
    s.fill((r, g, b, alpha))
    # 하이라이트
    pygame.draw.rect(s, (min(r+60,255), min(g+60,255), min(b+60,255)), (0, 0, CELL-2, 7))
    pygame.draw.rect(s, (max(r-60,0), max(g-60,0), max(b-60,0)), (0, CELL-9, CELL-2, 7))
    surface.blit(s, (x, y))


def draw_ghost(surface, board, piece):
    ghost = dict(piece)
    ghost["shape"] = [row[:] for row in piece["shape"]]
    while fits(board, ghost, oy=1):
        ghost["y"] += 1
    for r, row in enumerate(ghost["shape"]):
        for c, cell in enumerate(row):
            if cell and ghost["y"] + r != piece["y"] + r:
                x = (ghost["x"] + c) * CELL + 1
                y = (ghost["y"] + r) * CELL + 1 + HEADER
                s = pygame.Surface((CELL-2, CELL-2), pygame.SRCALPHA)
                s.fill((200, 200, 200, 70))
                surface.blit(s, (x, y))


def draw_board(surface, board):
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c]:
                draw_block(surface, board[r][c], c, r)
            else:
                rect = pygame.Rect(c * CELL, r * CELL + HEADER, CELL, CELL)
                pygame.draw.rect(surface, GRID_COL, rect, 1)


def draw_piece(surface, piece):
    for r, row in enumerate(piece["shape"]):
        for c, cell in enumerate(row):
            if cell:
                draw_block(surface, piece["color"], piece["x"]+c, piece["y"]+r)


def draw_sidebar(surface, next_p, score, level, lines, combo):
    sx = COLS * CELL
    pygame.draw.rect(surface, SIDEBAR_BG, (sx, 0, SIDEBAR, HEIGHT))

    # 제목
    title = font_big.render("테트리스", True, YELLOW)
    surface.blit(title, (sx + 12, 18))

    # 점수판
    y = 94
    for label, value in [("점수", score), ("레벨", level), ("줄수", lines)]:
        lbl = font_mid.render(label, True, CYAN)
        val = font_big.render(str(value), True, WHITE)
        surface.blit(lbl, (sx + 12, y))
        surface.blit(val, (sx + 12, y + 32))
        y += 88

    # 콤보
    if combo > 1:
        combo_txt = font_mid.render(f"콤보 x{combo}!", True, YELLOW)
        surface.blit(combo_txt, (sx + 12, y))
    y += 59

    # 다음 블록
    nxt_lbl = font_mid.render("다음 블록", True, CYAN)
    surface.blit(nxt_lbl, (sx + 12, y))
    y += 40
    s = next_p["shape"]
    bw = len(s[0]) * CELL
    bh = len(s) * CELL
    ox = sx + (SIDEBAR - bw) // 2
    for r, row in enumerate(s):
        for c, cell in enumerate(row):
            if cell:
                rx = ox + c * CELL + 1
                ry = y + r * CELL + 1
                rect = pygame.Rect(rx, ry, CELL-2, CELL-2)
                color = next_p["color"]
                cr, cg, cb = color
                pygame.draw.rect(surface, color, rect, border_radius=6)
                pygame.draw.rect(surface, (min(cr+60,255), min(cg+60,255), min(cb+60,255)), rect, 2, border_radius=6)

    # 조작법
    y2 = HEIGHT - 194
    guide = [
        "[ 조작 방법 ]",
        "← → : 이동",
        "↑    : 회전",
        "↓    : 빠르게",
        "Space: 바로 내리기",
        "P    : 일시정지",
    ]
    for line in guide:
        t = font_small.render(line, True, (160, 160, 200))
        surface.blit(t, (sx + 10, y2))
        y2 += 26


def draw_overlay(surface, text, sub=""):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    surface.blit(overlay, (0, 0))
    msg = font_big.render(text, True, YELLOW)
    surface.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 59))
    if sub:
        sub_msg = font_mid.render(sub, True, WHITE)
        surface.blit(sub_msg, (WIDTH//2 - sub_msg.get_width()//2, HEIGHT//2 + 12))


def score_for(lines, level):
    base = [0, 100, 300, 500, 800]
    return base[lines] * level


def main():
    board = [[None] * COLS for _ in range(ROWS)]
    current = new_piece()
    next_p  = new_piece()
    score = 0
    level = 1
    total_lines = 0
    combo = 0
    paused = False
    game_over = False

    fall_speed = 600   # ms
    fall_timer = 0
    fast_fall = False

    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and not game_over:
                    paused = not paused

                if game_over:
                    if event.key == pygame.K_r:
                        main()
                        return
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    continue

                if paused:
                    continue

                if event.key == pygame.K_LEFT:
                    if fits(board, current, ox=-1):
                        current["x"] -= 1
                elif event.key == pygame.K_RIGHT:
                    if fits(board, current, ox=1):
                        current["x"] += 1
                elif event.key == pygame.K_UP:
                    rotated = rotate(current["shape"])
                    if fits(board, current, shape=rotated):
                        current["shape"] = rotated
                elif event.key == pygame.K_DOWN:
                    fast_fall = True
                elif event.key == pygame.K_SPACE:
                    while fits(board, current, oy=1):
                        current["y"] += 1
                    place(board, current)
                    cleared = clear_lines(board)
                    if cleared:
                        combo += 1
                        score += score_for(cleared, level) + (combo - 1) * 50
                        total_lines += cleared
                        level = total_lines // 10 + 1
                        fall_speed = max(100, 600 - (level - 1) * 50)
                    else:
                        combo = 0
                    current = next_p
                    next_p = new_piece()
                    if not fits(board, current):
                        game_over = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    fast_fall = False

        if not paused and not game_over:
            speed = fall_speed // 5 if fast_fall else fall_speed
            fall_timer += dt
            if fall_timer >= speed:
                fall_timer = 0
                if fits(board, current, oy=1):
                    current["y"] += 1
                else:
                    place(board, current)
                    cleared = clear_lines(board)
                    if cleared:
                        combo += 1
                        score += score_for(cleared, level) + (combo - 1) * 50
                        total_lines += cleared
                        level = total_lines // 10 + 1
                        fall_speed = max(100, 600 - (level - 1) * 50)
                    else:
                        combo = 0
                    current = next_p
                    next_p = new_piece()
                    if not fits(board, current):
                        game_over = True

        # 그리기
        screen.fill(BG)
        # 헤더
        pygame.draw.rect(screen, (20, 20, 40), (0, 0, COLS * CELL, HEADER))
        header = font_mid.render(f"점수: {score}   레벨: {level}", True, YELLOW)
        screen.blit(header, (10, 18))

        draw_board(screen, board)
        if not game_over:
            draw_ghost(screen, board, current)
            draw_piece(screen, current)
        draw_sidebar(screen, next_p, score, level, total_lines, combo)

        if paused:
            draw_overlay(screen, "⏸ 일시정지", "P 키를 눌러 계속하기")
        if game_over:
            draw_overlay(screen, "게임 오버!", "R: 다시하기  ESC: 종료")

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
