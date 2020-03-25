from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy import platform

def last():
    for i in range(9999, 0, -1):
        if platform == 'linux' or platform == 'windows':
            if i >= 1000:
                var = "Screenshot%d.wav" %(i)
                try:
                    with open("%s" %(var), 'r') as file:
                        return str(var)
                except:
                    pass
            if 100 <= i < 1000:
                var = "Screenshot0%d.wav" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass
            if 10 <= i < 100:
                var = "Screenshot00%d.wav" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass
            if i < 10:
                var = "Screenshot000%d.wav" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass
        else:
            if i >= 1000:
                var = "/storage/emulated/0/Pictures/Screenshots/Screenshot%d.wav" %(i)
                try:
                    with open("%s" %(var), 'r') as file:
                        return str(var)
                except:
                    pass
            if 100 <= i < 1000:
                var = "/storage/emulated/0/Pictures/Screenshots/Screenshot0%d.wav" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass
            if 10 <= i < 100:
                var = "/storage/emulated/0/Pictures/Screenshots/Screenshot00%d.wav" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass
            if i < 10:
                var = "/storage/emulated/0/Pictures/Screenshots/Screenshot000%d.wav" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass


class play(Widget):
    def build(self):
        self.Bouton_ScreenShot = Button(text='ScreenShot', font_size=28, size_hint=(0.18, 0.1),
                                        pos_hint={'x': .474, 'y': 0.9}, background_color=[0.7, 0.7, 0.7, 1])

        self.Bouton_ScreenShot.bind()
        self.sound = SoundLoader.load(last())
        if self.sound:
            print("Sound found at %s" % self.sound.source)
            print("Sound is %.3f seconds" % self.sound.length)
            self.sound.play()

class main(App):
    def build(self):
        play().build()

if __name__ == '__main__':
    main().run()
