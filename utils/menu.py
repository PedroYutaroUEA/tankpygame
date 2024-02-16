from utils.colors import BLACK, WHITE
from fonts import screen_font, screen_font_bold


def draw_menu(screen, show_credits, mid_w, mid_h):
    screen.fill(BLACK)
    # create title
    title_txt = "TANK - COMBAT" if not show_credits else "CREDITS"
    title = screen_font_bold.render(title_txt, True, WHITE, BLACK)
    title_w = title.get_width()
    title_h = title.get_height()
    if not show_credits:
        # Subtitle
        subtitle_txt = "[Play game (space)] | [Show credits (enter)]"
        subtitle = screen_font.render(subtitle_txt, True, WHITE, BLACK)
        subtitle_w = subtitle.get_width()
        # Draw title and subtitle
        screen.blit(title, (mid_w - title_w // 2, mid_h - title_h // 2))
        screen.blit(subtitle, (mid_w - subtitle_w // 2, mid_h + title_h // 2))
    else:
        # draw title
        screen.blit(title, (mid_w - title_w // 2, (mid_h // 2) - title_h // 2))
        # subtitles
        credit_rows = [
            "<----- DEVELOPERS ----->",
            "Pedro Yutaro Mont Morency Nakamura",
            "Aline Daffiny Ferreira Gomes",
            "Leonardo Melo Crispim",
            "<----- SPRITE SOURCE ----->",
            "Dune 2: TBD",
            "[Back to menu (enter)]"
        ]
        # draw each subtitle
        space = 40
        for row in credit_rows:
            subtitle = screen_font.render(row, True, WHITE, BLACK)
            subtitle_w = subtitle.get_width()
            space += 80 if credit_rows.index(row) in (4, 6) else 40
            screen.blit(subtitle, (mid_w - subtitle_w // 2, (mid_h + title_h) // 2 + space))