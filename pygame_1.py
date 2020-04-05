# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
direction = True 
i = 0
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (i, 250), 75)

    # Flip the display
    pygame.display.flip()
    
    if direction == True:
        i += 1
    else:
        i -= 1
    if i == 500:
        direction = False 
    elif i == 0:
        direction = True
    i = (i%500)

# Done! Time to quit.
pygame.quit()