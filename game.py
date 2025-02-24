import pygame

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # Color for player
GRAVITY = 0.5
JUMP_STRENGTH = -10
PLAYER_SPEED = 5

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer Game")

# Player Properties (Rectangle instead of Image)
player = pygame.Rect(100, 500, 40, 40)  # x, y, width, height
velocity_y = 0
on_ground = False

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)  # Clear screen

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit loop when window is closed

    # Get Key Presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED
    if keys[pygame.K_SPACE] and on_ground:  # Jump only if on ground
        velocity_y = JUMP_STRENGTH
        on_ground = False

    # Apply Gravity
    velocity_y += GRAVITY
    player.y += velocity_y

    # Collision with Ground
    if player.y >= 500:
        player.y = 500
        velocity_y = 0
        on_ground = True

    # Draw Player (Rectangle)
    pygame.draw.rect(screen, BLUE, player)

    pygame.display.flip()  # Update display
    clock.tick(60)  # Limit FPS to 60

# Quit Pygame properly
pygame.quit()
