from guizero import App, PushButton, MenuBar, info
import com
import pygame
pygame.mixer.init()
app = App(title="Druaga1 Soundboard", layout="grid")
menubar = MenuBar(app,
                  toplevel=["File", "Help"],
                  options=[
                      [ ["Exit", com.exit] ],
                      [ ["About", com.about], ["View Code", com.viewcode] ]
                      ] )
ssd1 = PushButton(app, command=com.ssd1, text="SSD1", grid=[0,1])
ssd2 = PushButton(app, command=com.ssd2, text="SSD2", grid=[0,2])
button3 = PushButton(app, command=com.testb3, text="Test2", grid=[1,1])
app.display()
