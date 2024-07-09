import pygame
pygame.init()
pygame.mixer.music.load('music21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()