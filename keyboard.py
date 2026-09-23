from pynput import keyboard
import pygame


pygame.mixer.init()

sound = pygame.mixer.Sound("Shotgun.wav")

def on_press(key):
    sound.play()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

