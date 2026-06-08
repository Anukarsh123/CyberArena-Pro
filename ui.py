import pygame

def draw_level(screen, level, xp, xp_needed):

    font = pygame.font.SysFont(None, 35)

    level_text = font.render(
        f"Level: {level}",
        True,
        (255,255,255)
    )

    screen.blit(level_text,(20,110))

    pygame.draw.rect(
        screen,
        (100,100,100),
        (20,150,250,20)
    )

    pygame.draw.rect(
        screen,
        (0,255,255),
        (20,150,250*(xp/xp_needed),20)
    )
