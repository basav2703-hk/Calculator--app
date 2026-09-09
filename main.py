from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorApp(App):

    def build(self):
        main = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.display = TextInput(
            text="",
            font_size=35,
            readonly=True,
            halign="right",
            size_hint_y=0.2
        )
        main.add_widget(self.display)

        buttons = GridLayout(cols=4, spacing=5)

        keys = [
            "7", "8", "9", "÷",
            "4", "5", "6", "×",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C"
        ]

        for key in keys:
            button = Button(text=key, font_size=25)
            button.bind(on_press=self.press)
            buttons.add_widget(button)

        main.add_widget(buttons)

        return main

    def press(self, button):
        key = button.text

        if key == "C":
            self.display.text = ""

        elif key == "=":
            try:
                expression = self.display.text.replace("×", "*").replace("÷", "/")
                self.display.text = str(eval(expression))
            except:
                self.display.text = "Error"

        else:
            self.display.text += key


CalculatorApp().run()
    	       
