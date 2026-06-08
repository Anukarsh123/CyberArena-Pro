import pygame

def draw_score(screen, score):

    font = pygame.font.SysFont(None,40)

    text = font.render(
        f"Score: {score}",
        True,
        (255,255,255)
    )

    screen.blit(text,(20,20))


def draw_health_bar(screen, health, max_health):

    ratio = health / max_health

    pygame.draw.rect(
        screen,
        (255,0,0),
        (20,70,200,25)
    )

    pygame.draw.rect(
        screen,
        (0,255,0),
        (20,70,200 * ratio,25)
    )

    pygame.draw.rect(
        screen,
        (255,255,255),
        (20,70,200,25),
        2
    )
