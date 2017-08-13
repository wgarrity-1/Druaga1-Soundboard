from guizero import App, PushButton, MenuBar, info
import pygame
import os
pygame.mixer.init()
def exit():
    os._exit(0)
def about():
    info ("About", "Druaga1 Soundboard v0.01a by Will9183.")
def ssd1():
    pygame.mixer.music.load("ssd1.wav")
    pygame.mixer.music.play()
def ssd2():
    pygame.mixer.music.load("ssd2.wav")
    pygame.mixer.music.play()
def testb3():
    print("Oh, more buttons")
app = App(title="Druaga1 Soundboard", layout="grid")
menubar = MenuBar(app,
                  toplevel=["File", "Help"],
                  options=[
                      [ ["Exit", exit] ],
                      [ ["About", about] ]
                      ] )
ssd1 = PushButton(app, command=ssd1, text="SSD1", grid=[0,1])
ssd2 = PushButton(app, command=ssd2, text="SSD2", grid=[0,2])
button3 = PushButton(app, command=testb3, text="Test2", grid=[1,1])
app.display()
