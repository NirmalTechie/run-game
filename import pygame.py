import pygame

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
GRAVITY = 0.5
JUMP_STRENGTH = -10
PLAYER_SPEED = 5
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer with Levels")

# Load Player
player_img = pygame.Surface((40, 60))
player_img.fill(BLUE)

# Player Class
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 60)
        self.vel_y = 0
        self.on_ground = False
        self.score = 0

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

    def jump(self, keys):
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False

    def apply_gravity(self, platforms):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        for platform in platforms:
            if self.rect.colliderect(platform):
                self.rect.bottom = platform.top
                self.vel_y = 0
                self.on_ground = True

# Define Levels
levels = [
    {"platforms": [pygame.Rect(200, 500, 400, 20)], "goal": pygame.Rect(700, 450, 40, 40)},  # Easy
    {"platforms": [pygame.Rect(100, 500, 200, 20), pygame.Rect(400, 400, 200, 20)], "goal": pygame.Rect(700, 350, 40, 40)},  # Medium
    {"platforms": [pygame.Rect(50, 500, 150, 20), pygame.Rect(250, 400, 150, 20), pygame.Rect(450, 300, 150, 20)], "goal": pygame.Rect(700, 250, 40, 40)}  # Hard
]

# Initialize Game
player = Player(100, 400)
current_level = 0
running = True
clock = pygame.time.Clock()

# Game Loop
while running:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move(keys)
    player.jump(keys)
    player.apply_gravity(levels[current_level]["platforms"])

    # Draw Platforms
    for platform in levels[current_level]["platforms"]:
        pygame.draw.rect(screen, GREEN, platform)

    # Draw Goal
    goal = levels[current_level]["goal"]
    pygame.draw.rect(screen, RED, goal)

    # Draw Player
    screen.blit(player_img, player.rect.topleft)

    # Score and Level Logic
    if player.rect.colliderect(goal):  # If player reaches goal
        player.score += 10
        if current_level < len(levels) - 1:
            current_level += 1  # Move to next level
            player.rect.x, player.rect.y = 100, 400  # Reset player position
        else:
            print(f"Game Over! Final Score: {player.score}")
            running = False  # End game when all levels are complete

    # Display Score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {player.score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
