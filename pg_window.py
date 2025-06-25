# Import Necesary Libraries:
import pygame 

# Initialize reqiured modules:
pygame.init()

# set up window geometry:
screen = pygame.display.set_mode((400, 500))

# Create a loop until the players quits:
done = False

while not done:

    # clear the event queue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Make the changes visible:
    pygame.display.flip()