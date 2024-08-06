from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from math import sqrt, sin, cos, tan, log

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/', 'sin', 'cos', 'tan', 'sqrt', 'log']
        self.last_was_operator = None
        self.last_button = None
        main_layout = GridLayout(cols=4, spacing=10, padding=10)
        self.solution = TextInput(background_color='black', foreground_color='white', readonly=True, halign='right', font_size=55)
        main_layout.add_widget(self.solution)
        
        buttons = [
            'C', 'sqrt', 'log', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', 'sin', 'cos', 'tan'
        ]

        for button in buttons:
            if button == 'C':
                btn = Button(text=button, pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color='gray', on_press=self.clear)
            elif button == '=':
                btn = Button(text=button, pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color='orange', on_press=self.calculate)
            elif button in self.operators:
                btn = Button(text=button, pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color='orange', on_press=self.add_operator)
            else:
                btn = Button(text=button, pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color='white', on_press=self.add_number)
            
            main_layout.add_widget(btn)
        
        return main_layout

    def clear(self, instance):
        self.solution.text = ""

    def calculate(self, instance):
        text = self.solution.text
        try:
            self.solution.text = str(eval(self.solution.text))
        except Exception as e:
            self.solution.text = "Error"

    def add_operator(self, instance):
        text = self.solution.text
        if text and (self.last_was_operator is False):
            self.solution.text += instance.text
            self.last_was_operator = True
        elif text == "" and instance.text == "-":
            self.solution.text = "-"
            self.last_was_operator = True

    def add_number(self, instance):
        if self.solution.text == "Error":
            self.solution.text = ""
        self.solution.text += instance.text
        self.last_was_operator = False

if __name__ == "__main__":
    CalculatorApp().run()
