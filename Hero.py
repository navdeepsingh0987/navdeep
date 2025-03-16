import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)

# Load assets (Make sure you have the images in the same directory as the script)
car_img = pygame.image.load("car.png")
background_img = pygame.image.load("background.png")
obstacle_img = pygame.image.load("obstacle.png")

# Rescale images
car_width = 50
car_height = 100
car_img = pygame.transform.scale(car_img, (car_width, car_height))

obstacle_width = 50
obstacle_height = 50
obstacle_img = pygame.transform.scale(obstacle_img, (obstacle_width, obstacle_height))

# Function to display score
font = pygame.font.SysFont("Arial", 30)

def display_score(score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Car class
class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx):
        self.x += dx
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - car_width:
            self.x = WIDTH - car_width

    def draw(self):
        screen.blit(car_img, (self.x, self.y))

# Obstacle class
class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.y += 5  # Speed of obstacle
        if self.y > HEIGHT:
            self.y = -obstacle_height
            self.x = random.randint(100, WIDTH - 100)

    def draw(self):
        screen.blit(obstacle_img, (self.x, self.y))

# Main game loop
def game_loop():
    car = Car(WIDTH // 2, HEIGHT - car_height - 10)
    obstacles = [Obstacle(random.randint(100, WIDTH - 100), -obstacle_height)]
    score = 0
    clock = pygame.time.Clock()

    run_game = True
    while run_game:
        screen.fill(WHITE)  # Fill the screen with white before drawing

        # Background image
        screen.blit(background_img, (0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        # Keyboard controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.move(-10)  # Move left
        if keys[pygame.K_RIGHT]:
            car.move(10)  # Move right

        # Move obstacles
        for obs in obstacles:
            obs.move()

        # Check collision
        for obs in obstacles:
            car_rect = pygame.Rect(car.x, car.y, car_width, car_height)
            obstacle_rect = pygame.Rect(obs.x, obs.y, obstacle_width, obstacle_height)
            if car_rect.colliderect(obstacle_rect):
                run_game = False

        # Draw the car and obstacles
        car.draw()
        for obs in obstacles:
            obs.draw()

        # Display score
        score += 1
        display_score(score)

        # Update the screen
        pygame.display.update()

        # Add new obstacles randomly
        if random.random() < 0.02:  # Chance to spawn new obstacle
            obstacles.append(Obstacle(random.randint(100, WIDTH - 100), -obstacle_height))

        # Set frame rate
        clock.tick(60)

    pygame.quit()

# Start the game
game_loop()
