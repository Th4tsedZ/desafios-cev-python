import pygame, time
pygame.mixer.init(44100)
music = pygame.mixer.music
music.load('C:/Users/Edenilson/PycharmProjects/desafios_cursoEmVideo/venv/Scripts/musica.mp3')
music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)