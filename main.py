from kivy.app import App

from gui.MainWindow import MainWindow


class ComparerApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    ComparerApp().run()
