import pygame
import os
import webbrowser
def exit():
    os._exit(0)
def about():
    info ("About", "Druaga1 Soundboard v0.01a by Will9183.")
def viewcode():
    webbrowser.open('https://github.com/will9183/Druaga1-Soundboard', new=2)
def ssd1():
    pygame.mixer.music.load("ssd1.wav")
    pygame.mixer.music.play()
def ssd2():
    pygame.mixer.music.load("ssd2.wav")
    pygame.mixer.music.play()
def testb3():
    print("Oh, more buttons")
