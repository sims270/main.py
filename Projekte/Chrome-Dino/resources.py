import pygame
import os

RUNNING = [
    pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png"))
]
JUMPING = pygame.image.load(os.path.join("assets/Dino", "DinoJump.png"))

DUCKING = [
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png")),

]

RUNNING2 = [
    pygame.image.load(os.path.join("assets/Stitch", "stitch1run1.png")),
    pygame.image.load(os.path.join("assets/Stitch", "stitch1run2.png"))
]

DUCKING2 = [
    pygame.image.load(os.path.join("assets/Stitch", "stitch1duck1.png")),
    pygame.image.load(os.path.join("assets/Stitch", "stitch1duck2.png"))
]
JUMPING_STITCH =  pygame.image.load(os.path.join("assets/Stitch", "stitch1sprung.png"))

DEAD_STITCH = [
pygame.image.load(os.path.join("assets/Stitch", "stitch1dead.png"))
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join("assets/Bird", "Bird1.png")),
    pygame.image.load(os.path.join("assets/Bird", "Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join("assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("assets/Other", "Track.png"))
