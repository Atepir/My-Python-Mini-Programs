from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy import platform


class MyPaintWidget(Widget):
    def build(self):
        # ici on defini des listes et autres utiles au lancement du programme

        self.Couleur = [0, 0, 0, 1]
        self.taille = 1
        self.trait = 0

    def on_touch_down(self, touch):
        # ici on creer les traits

        with self.canvas:
            Couleur = Color(self.Couleur[0], self.Couleur[1], self.Couleur[2], 1)
            d = 30.
            try:
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.taille)
                if self.trait >= 5:
                    touch.ud['line'] = Line(points=(touch.x + self.trait, touch.y + self.trait), width=self.taille)
                    touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.taille)
            except:
                pass

    def on_touch_move(self, touch):
        try:
            touch.ud['line'].points += [touch.x, touch.y]
            if self.trait >= 5:
                touch.ud['line'].points += [touch.x + self.trait, touch.y + self.trait]
                touch.ud['line'].points += [touch.x + self.trait, touch.y + self.trait]
        except:
            pass


class MyPaintApp(App):

    def build(self):
        # ici on creer le floatlayout

        parent = FloatLayout()
        self.painter = MyPaintWidget()
        self.painter.build()
        # Bouton clear:

        clearbtn = Button(text='Clear', font_size=35, size_hint=(0.17, 0.1), pos_hint={'x': .652, 'y': 0.9})
        clearbtn.bind(on_press=self.clear_canvas)
        # Listes :

        self.liste_trait = [1, 5, 10, 15, 20, 40, 50]
        self.liste_trait_nom = ["0", "5", "10", "15", "20", '40', '50']
        self.liste_taille_nom = ["1", '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.liste_taille = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.liste_couleurs = ["Jaune", "Rouge", "Vert", "Bleu", "Violet", "Noir", "Bleu Clair", ]
        self.liste_RGBA = [[1, 0.8, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0.7, 0, 0.7, 1], [0, 0, 0, 1],
                           [0, 1, 1, 1]]
        self.liste_couleur = ["Jaune", "Rouge", "Vert", "Bleu", "Violet", "Noir", "Bleu Clair", "Blanc"]
        self.liste_RGB = [[1, 0.8, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0.7, 0, 0.7, 1], [0, 0, 0, 1],
                          [0, 1, 1, 1], [1, 1, 1, 1]]

        self.Liste_Boutons_Fond = []
        self.Liste_Boutons_couleurs = []
        self.Liste_Boutons_tailles = []
        self.Liste_Boutons_traits = []

        # creation des dropdown:

        self.Bouton_couleur = Button(text='Couleur', font_size=33, size_hint=(0.18, 0.1), pos_hint={'x': .0, 'y': 0.9},
                                     background_color=[0.9, 0.9, 0.9, 1])

        dropdown = DropDown()

        for index in range(0, len(self.liste_couleurs)):
            self.Liste_Boutons_couleurs.append(Button())
            self.Liste_Boutons_couleurs[index].text = self.liste_couleurs[index]
            self.Liste_Boutons_couleurs[index].size_hint_y = None
            self.Liste_Boutons_couleurs[index].height = 60
            self.Liste_Boutons_couleurs[index].id = str(index)
            self.Liste_Boutons_couleurs[index].font_size = 32
            self.Liste_Boutons_couleurs[index].bind(on_release=lambda btn: dropdown.select(btn.text))
            self.Liste_Boutons_couleurs[index].bind(on_press=self.Couleur)

            dropdown.add_widget(self.Liste_Boutons_couleurs[index])

        self.Bouton_couleur.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.Bouton_couleur, 'text', x))

        self.Liste_Boutons_couleurs[0].color = self.liste_RGBA[0]
        self.Liste_Boutons_couleurs[1].color = self.liste_RGBA[1]
        self.Liste_Boutons_couleurs[2].color = self.liste_RGBA[2]
        self.Liste_Boutons_couleurs[3].color = self.liste_RGBA[3]
        self.Liste_Boutons_couleurs[4].color = self.liste_RGBA[4]
        self.Liste_Boutons_couleurs[5].color = self.liste_RGBA[5]
        self.Liste_Boutons_couleurs[6].color = self.liste_RGBA[6]

        self.Bouton_taille = Button(text='Taille', font_size=35, size_hint=(0.15, 0.1), pos_hint={'x': .178, 'y': 0.9},
                                    background_color=[0.9, 0.9, 0.9, 1])

        drop_down = DropDown()

        for index in range(0, len(self.liste_taille_nom)):
            self.Liste_Boutons_tailles.append(Button())
            self.Liste_Boutons_tailles[index].text = self.liste_taille_nom[index]
            self.Liste_Boutons_tailles[index].size_hint_y = None
            self.Liste_Boutons_tailles[index].height = 45
            self.Liste_Boutons_tailles[index].id = str(index)
            self.Liste_Boutons_tailles[index].bind(on_release=lambda btn: drop_down.select(btn.text))
            self.Liste_Boutons_tailles[index].bind(on_press=self.Taille)
            self.Liste_Boutons_tailles[index].font_size = 30
            drop_down.add_widget(self.Liste_Boutons_tailles[index])

        self.Bouton_taille.bind(on_release=drop_down.open)
        drop_down.bind(on_select=lambda instance, x: setattr(self.Bouton_taille, 'text', x))

        self.Bouton_trait = Button(text='Profondeur', font_size=23, size_hint=(0.15, 0.1),
                                   pos_hint={'x': .326, 'y': 0.9}, background_color=[0.9, 0.9, 0.9, 1])

        dropdown2 = DropDown()

        for index in range(0, len(self.liste_trait_nom)):
            self.Liste_Boutons_traits.append(Button())
            self.Liste_Boutons_traits[index].text = self.liste_trait_nom[index]
            self.Liste_Boutons_traits[index].size_hint_y = None
            self.Liste_Boutons_traits[index].height = 50
            self.Liste_Boutons_traits[index].id = str(index)
            self.Liste_Boutons_traits[index].bind(on_release=lambda btn: dropdown2.select(btn.text))
            self.Liste_Boutons_traits[index].bind(on_press=self.Trait)
            self.Liste_Boutons_traits[index].font_size = 30
            dropdown2.add_widget(self.Liste_Boutons_traits[index])

        self.Bouton_trait.bind(on_release=dropdown2.open)
        dropdown2.bind(on_select=lambda instance, x: setattr(self.Bouton_trait, 'text', x))

        self.Bouton_ScreenShot = Button(text='ScreenShot', font_size=28, size_hint=(0.18, 0.1),
                                        pos_hint={'x': .474, 'y': 0.9}, background_color=[0.7, 0.7, 0.7, 1])

        self.Bouton_ScreenShot.bind(on_press=self.photo)

        self.Bouton_Fond = Button(text='Couleur_Fond', font_size=23, size_hint=(0.18, 0.1),
                                  pos_hint={'x': .82, 'y': 0.9}, background_color=[0.9, 0.9, 0.9, 1])

        dropdown3 = DropDown()

        for index in range(0, len(self.liste_couleur)):
            self.Liste_Boutons_Fond.append(Button())
            self.Liste_Boutons_Fond[index].text = self.liste_couleur[index]
            self.Liste_Boutons_Fond[index].size_hint_y = None
            self.Liste_Boutons_Fond[index].height = 55
            self.Liste_Boutons_Fond[index].id = str(index)
            self.Liste_Boutons_Fond[index].bind(on_release=lambda btn: dropdown3.select(btn.text))
            self.Liste_Boutons_Fond[index].bind(on_press=self.Fonds)
            self.Liste_Boutons_Fond[index].font_size = 32

            dropdown3.add_widget(self.Liste_Boutons_Fond[index])

        self.Bouton_Fond.bind(on_release=dropdown3.open)
        dropdown3.bind(on_select=lambda instance, x: setattr(self.Bouton_Fond, 'text', x))

        self.Liste_Boutons_Fond[0].color = self.liste_RGB[0]
        self.Liste_Boutons_Fond[1].color = self.liste_RGB[1]
        self.Liste_Boutons_Fond[2].color = self.liste_RGB[2]
        self.Liste_Boutons_Fond[3].color = self.liste_RGB[3]
        self.Liste_Boutons_Fond[4].color = self.liste_RGB[4]
        self.Liste_Boutons_Fond[5].color = self.liste_RGB[5]
        self.Liste_Boutons_Fond[6].color = self.liste_RGB[6]
        self.Liste_Boutons_Fond[7].color = self.liste_RGB[7]

        # ici on integre tout au widget

        parent.add_widget(self.painter)
        parent.add_widget(self.Bouton_Fond)
        parent.add_widget(self.Bouton_taille)
        parent.add_widget(self.Bouton_couleur)
        parent.add_widget(self.Bouton_trait)
        parent.add_widget(self.Bouton_ScreenShot)
        parent.add_widget(clearbtn)

        self.size = Window.size
        self.Fond_Couleur = [1, 1, 1, 1]

        with parent.canvas.before:
            self.Fond_couleurs = Color(self.Fond_Couleur)
            self.rectangle = Rectangle(size=self.size)

        return parent

    def photo(self, instance):
        # ici on creer le chemin du screenshot
        try:

            if platform == 'android':
                Window.screenshot(name='/storage/emulated/0/Pictures/Screenshots/Screenshot.png')
                content = Button(text='Image enregistre', font_size=50)
                popup = Popup(title='Votre image est enregistre dans Pictures/Screenshots', content=content,
                              size_hint=(0.5, 0.5))
                content.bind(on_press=popup.dismiss)
                popup.open()
            else:
                if platform == 'linux':
                    Window.screenshot(name='Screenshot.png')
                    content = Button(text='Image enregistre', font_size=50)
                    popup = Popup(title='Votre image est enregistre dans le dossier de votre application',
                                  content=content, size_hint=(0.5, 0.5))
                    content.bind(on_press=popup.dismiss)
                    popup.open()
                else:
                    if platform == 'win':
                        Window.screenshot(name='Screenshot.png')
                        content = Button(text='Image enregistre', font_size=50)
                        popup = Popup(title='Votre image est enregistre dans le dossier de votre application',
                                      content=content, size_hint=(0.5, 0.5))
                        content.bind(on_press=popup.dismiss)
                        popup.open()
                    else:
                        if platform == 'macosx':
                            Window.screenshot(name='Screenshot.png')
                            content = Button(text='Image enregistre', font_size=50)
                            popup = Popup(title='Votre image est enregistre dans le dossier de votre application',
                                          content=content, size_hint=(0.5, 0.5))
                            content.bind(on_press=popup.dismiss)
                            popup.open()
                        else:
                            if platform == 'ios':
                                Window.screenshot(name='Screenshot.png')
                                content = Button(text='Image enregistre', font_size=50)
                                popup = Popup(title='Votre image est enregistre dans le dossier de votre application',
                                              content=content, size_hint=(0.5, 0.5))
                                content.bind(on_press=popup.dismiss)
                                popup.open()

                            else:
                                Window.screenshot(name='Screenshot.png')
                                content = Button(text='Image enregistre', font_size=50)
                                popup = Popup(title='Votre image est enregistre dans le dossier de votre application',
                                              content=content, size_hint=(0.5, 0.5))
                                content.bind(on_press=popup.dismiss)
                                popup.open()

        except:
            pass

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

        # ici on fait les changement par rapport aux dropdown

    def Couleur(self, instance):
        if instance.id == "0":
            self.painter.Couleur = self.liste_RGBA[0]
            self.Bouton_couleur.background_color = self.liste_RGBA[0]
        else:
            if instance.id == "1":
                self.painter.Couleur = self.liste_RGBA[1]
                self.Bouton_couleur.background_color = self.liste_RGBA[1]

            else:
                if instance.id == "2":
                    self.painter.Couleur = self.liste_RGBA[2]
                    self.Bouton_couleur.background_color = self.liste_RGBA[2]
                else:
                    if instance.id == "3":
                        self.painter.Couleur = self.liste_RGBA[3]
                        self.Bouton_couleur.background_color = self.liste_RGBA[3]
                    else:
                        if instance.id == "4":
                            self.painter.Couleur = self.liste_RGBA[4]
                            self.Bouton_couleur.background_color = self.liste_RGBA[4]
                        else:
                            if instance.id == "5":
                                self.painter.Couleur = self.liste_RGBA[5]
                                self.Bouton_couleur.background_color = [0.9, 0.9, 0.9, 1]
                            else:
                                if instance.id == "6":
                                    self.painter.Couleur = self.liste_RGBA[6]
                                    self.Bouton_couleur.background_color = self.liste_RGBA[6]
                                else:
                                    if instance.id == "7":
                                        self.painter.Couleur = self.liste_RGBA[7]
                                        self.Bouton_couleur.background_color = self.liste_RGBA[7]

    def Taille(self, instance):
        if instance.id == "0":
            self.painter.taille = self.liste_taille[0]
        else:
            if instance.id == "1":
                self.painter.taille = self.liste_taille[1]
            else:
                if instance.id == "2":
                    self.painter.taille = self.liste_taille[2]
                else:
                    if instance.id == "3":
                        self.painter.taille = self.liste_taille[3]
                    else:
                        if instance.id == "4":
                            self.painter.taille = self.liste_taille[4]
                        else:
                            if instance.id == "5":
                                self.painter.taille = self.liste_taille[5]
                            else:
                                if instance.id == "6":
                                    self.painter.taille = self.liste_taille[6]
                                else:
                                    if instance.id == "7":
                                        self.painter.taille = self.liste_taille[7]
                                    else:
                                        if instance.id == "8":
                                            self.painter.taille = self.liste_taille[8]
                                        else:
                                            if instance.id == "9":
                                                self.painter.taille = self.liste_taille[9]

    def Trait(self, instance):
        if instance.id == "0":
            self.painter.trait = self.liste_trait[0]
        else:
            if instance.id == "1":
                self.painter.trait = self.liste_trait[1]
            else:
                if instance.id == "2":
                    self.painter.trait = self.liste_trait[2]
                else:
                    if instance.id == "3":
                        self.painter.trait = self.liste_trait[3]
                    else:
                        if instance.id == "4":
                            self.painter.trait = self.liste_trait[4]
                        else:
                            if instance.id == "5":
                                self.painter.trait = self.liste_trait[5]
                            else:
                                if instance.id == "6":
                                    self.painter.trait = self.liste_trait[6]

    def Fonds(self, instance):
        if instance.id == "0":
            self.Fond_Couleur = self.liste_RGB[0]
            self.Bouton_Fond.background_color = self.liste_RGB[0]
            with self.painter.parent.canvas.before:
                self.painter.parent.canvas.before.clear()
                self.Fond_couleurs = Color(self.Fond_Couleur[0], self.Fond_Couleur[1], self.Fond_Couleur[2], 1)
                Rectangle(size=self.size)
        else:
            if instance.id == "1":
                self.Fond_Couleur = self.liste_RGB[1]
                self.Bouton_Fond.background_color = self.liste_RGB[1]
                with self.painter.parent.canvas.before:
                    self.painter.parent.canvas.before.clear()
                    self.Fond_couleurs = Color(self.Fond_Couleur[0], self.Fond_Couleur[1], self.Fond_Couleur[2], 1)
                    Rectangle(size=self.size)
            else:
                if instance.id == "2":
                    self.Fond_Couleur = self.liste_RGB[2]
                    self.Bouton_Fond.background_color = self.liste_RGB[2]
                    with self.painter.parent.canvas.before:
                        self.painter.parent.canvas.before.clear()
                        self.Fond_couleurs = Color(self.Fond_Couleur[0], self.Fond_Couleur[1], self.Fond_Couleur[2], 1)
                        Rectangle(size=self.size)
                else:
                    if instance.id == "3":
                        self.Fond_Couleur = self.liste_RGB[3]
                        self.Bouton_Fond.background_color = self.liste_RGB[3]
                        with self.painter.parent.canvas.before:
                            self.painter.parent.canvas.before.clear()
                            self.Fond_couleurs = Color(self.Fond_Couleur[0], self.Fond_Couleur[1], self.Fond_Couleur[2],
                                                       1)
                            Rectangle(size=self.size)
                    else:
                        if instance.id == "4":
                            self.Fond_Couleur = self.liste_RGB[4]
                            self.Bouton_Fond.background_color = self.liste_RGB[4]
                            with self.painter.parent.canvas.before:
                                self.painter.parent.canvas.before.clear()
                                self.Fond_couleurs = Color(self.Fond_Couleur[0], self.Fond_Couleur[1],
                                                           self.Fond_Couleur[2], 1)
                                Rectangle(size=self.size)
                        else:
                            if instance.id == "5":
                                self.Fond_Couleur = self.liste_RGB[5]
                                self.Bouton_Fond.background_color = [0.9, 0.9, 0.9, 1]
                                with self.painter.parent.canvas.before:
                                    self.painter.parent.canvas.before.clear()
                                    self.Fond_couleurs = Color(self.Fond_Couleur[0], self.Fond_Couleur[1],
                                                               self.Fond_Couleur[2], 1)
                                    Rectangle(size=self.size)
                            else:
                                if instance.id == "6":
                                    self.Fond_Couleur = self.liste_RGB[6]
                                    self.Bouton_Fond.background_color = self.liste_RGB[6]
                                    with self.painter.parent.canvas.before:
                                        self.painter.parent.canvas.before.clear()
                                        self.Fond_couleurs = Color(self.Fond_Couleur[0], self.Fond_Couleur[1],
                                                                   self.Fond_Couleur[2], 1)
                                        Rectangle(size=self.size)

                                else:
                                    if instance.id == "7":
                                        self.Fond_Couleur = self.liste_RGB[7]
                                        self.Bouton_Fond.background_color = self.liste_RGB[7]
                                        with self.painter.parent.canvas.before:
                                            self.painter.parent.canvas.before.clear()
                                            self.Fond_couleurs = Color(self.Fond_Couleur[0], self.Fond_Couleur[1],
                                                                       self.Fond_Couleur[2], 1)
                                            Rectangle(size=self.size)


if __name__ == '__main__':
    MyPaintApp().run()

