import pygame

# initialize Pygame and screen dimensions:
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# initialize display surface and set title:
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Adding image and background image")

# Load and scale images directly:
'''background_image = pygame.transform.scale(pygame.image.load('b1.jpg').convert(),(SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = pygame.transform.scale(pygame.image.load('penguin.jpeg').convert_alpha(),(200, 200))

penguin_rect = penguin_image.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))'''

# Initialize font, render text, and set position:
text = pygame.font.Font(None, 36).render('Hello World', True, pygame.Color('black'))
text_rect = text.get_rect(center =(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))


# Game loop production

def game_loop():
    clock = pygame.time.Clock()
    running = True

    # Infinite loop:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

     # display_surface.blit(background_image, (0,0))
        # display_surface.blit(penguin_image, penguin_rect)'''
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()